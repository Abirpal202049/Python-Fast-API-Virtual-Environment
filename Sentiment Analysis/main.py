from fastapi import FastAPI
import pickle


app = FastAPI()


@app.get('/home')
def home_route():
    return {"message" : "Your backend server is up and running...", "success" : True}