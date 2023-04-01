import uvicorn
from fastapi import FastAPI



app = FastAPI()

@app.get('/')
def index():
    return {'message' : 'Hello Buddy'}


@app.get('/welcome')
def get_name(name):
    return {'message' : f'{name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.1.10.2', port=8000)