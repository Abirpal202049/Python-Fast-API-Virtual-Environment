from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Package to read the extracted ML model
import pickle

# All the Natural Language Processes
import nltk
# ! nltk.download('vader_lexicon')
# ! You need to download vader_lexicon using [python3 -m nltk.downloader vader_lexicon] to run the app
# ! https://rstudio-pubs-static.s3.amazonaws.com/591860_85c76c963bd84f25a197b8438256da9b.html
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

# For the progress bar
from tqdm.notebook import tqdm


# FastAPI app and cors policy 
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Reading the .pkl file for extraction of the ML Model
with open('TwitterSentimentModel', 'rb') as f:
  myModel = pickle.load(f)

# Segrigating the Algo
knn = myModel['knn']
lr = myModel['lr']
rf = myModel['rf']
mlr = myModel['mlr']


# Natural Language Initilization
sia = SentimentIntensityAnalyzer()
task='sentiment'
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
# ! You also need pytorch for AutoModelForSequenceClassification
# ! https://pytorch.org/
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# Test Route
@app.get('/')
def home_route():
    return {"message" : "Your backend server is up and running...", "success" : True}

# Prediction Route
@app.post('/predict')
def predict_route(text: str):
    vadarScore = sia.polarity_scores(text)
    encoded_text = tokenizer(text,return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        "roberta_neg" : scores[0],
        "roberta_neu" : scores[1],
        "roberta_pos" : scores[2]
    }
    vadarList =  [i for i in vadarScore.values()]
    robertaList =[i for i in scores_dict.values()]
    knn_predict = knn.predict([(vadarList + robertaList)])
    linearReggPredict = mlr.predict([(vadarList + robertaList)])
    logisticReggPredict = lr.predict([(vadarList + robertaList)])
    randomForestPredict = rf.predict([(vadarList + robertaList)])
    pred = {
        'TAG' : { 
            "KNN":int(knn_predict[0]),
            "RandomForest":int(randomForestPredict[0]),
            "Logistic Regression":int(logisticReggPredict[0]) 
        }, 
        'SCORE' :  float(linearReggPredict[0]) 
    }

    print("Prediction", pred, type(pred))
    return pred