from fastapi import FastAPI
import pickle
import nltk
# nltk.download('vader_lexicon')
# !You need to download vader_lexicon using [python3 -m nltk.downloader vader_lexicon] to run the app
# * https://rstudio-pubs-static.s3.amazonaws.com/591860_85c76c963bd84f25a197b8438256da9b.html

from tqdm.notebook import tqdm
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax


app = FastAPI()
with open('TwitterSentimentModel', 'rb') as f:
  myModel = pickle.load(f)

knn = myModel['knn']
lr = myModel['lr'] # Logistic Regression
rf = myModel['rf']
mlr = myModel['mlr']

sia = SentimentIntensityAnalyzer()
task='sentiment'
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
# ! You also need pytorch for AutoModelForSequenceClassification
# * https://pytorch.org/
model = AutoModelForSequenceClassification.from_pretrained(MODEL)


@app.get('/home')
def home_route():
    return {"message" : "Your backend server is up and running...", "success" : True}

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