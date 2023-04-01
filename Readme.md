# Creating a virtual enviroment with `conda` 
**Run all the code in `CMD`**

## Create a enviroment using `conda`
```
conda create -p venv python==3.8 -y
```

## Check all the enviroments present in your system and in that particular directory which you are working
```
conda info --envs
```

## Activating your virtual environment
```
conda activate venv/
```

## Deactivating your virtual enviroment
```
conda deactivate
```





# Creating a API using Fast API

<!-- ----------------------------------- -->

## **How to download the packages in python ?**
`pip install numpy` or `pip install numpy --user`

The packages which we need for creating fastAPI app are `fastapi` and `uvicorn`

```
pip install fastapi uvicorn
```


#### ***Issue and Error that may occur***
- [**Showing error while downloading packages using pip**](https://stackoverflow.com/questions/66322049/could-not-install-packages-due-to-an-oserror-winerror-2-no-such-file-or-direc)

<!-- ----------------------------------- -->

## **Writing a simple API using `Fast API`**
```py
import uvicorn
from fastapi import FastAPI



app = FastAPI()

@app.get('/')
def index():
    return {'message' : 'Hello World'}


@app.get('/welcome')
def get_name(name):
    return {'message' : f'{name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
```
#### ***Docs Link***
- [Fast API](https://fastapi.tiangolo.com/)
<!-- ----------------------------------- -->

## **How to start the `Fast API` app ?**

`python -m uvicorn main:app --reload` or `uvicorn main:app --reload`

#### ***Issue and Error that may occur***
- [**`uvicorn` doesen't work**](https://stackoverflow.com/questions/64936440/python-uvicorn-the-term-uvicorn-is-not-recognized-as-the-name-of-a-cmdlet-f)


<!-- ---------------------------------- -->



# How to create a `requiremnt.txt` ?
```
pip freeze > requirements.txt

pip install -r requirements.txt
```



# Create a Virtual Enviroment using `venv` package
## First install the `venv` package
```
pip install venv
```

## Creating the virtual environment
```
python -m venv myenv
```

## Activating your virtual environment
```
myenv\Scripts\activate
```

## Deactivating your virtual enviroment
```
deactivate
```

#### *Issues and Error*
- [**Issue in activating virtual enviroment in windows**](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)


# Resources 
- [Deployment of ML app using FAST API and Creating virtual enviroment using `conda`](https://www.youtube.com/playlist?list=PLZoTAELRMXVPgsojPOHF9i0u2L83-m9P7)
- [Hitesh Choudhary - Fast API](https://www.youtube.com/watch?v=TQfIUS52QHA&t=20s&pp=ygUIZmFzdCBhcGk%3D)
- [CodeWithHarry - Virtual environment using `venv`](https://www.youtube.com/watch?v=nt6LlFTWOkg&ab_channel=CodeWithHarry)
- [Nicholas Renotte - Setting up a API using Fast API and pretrained ML Model](https://www.youtube.com/watch?v=C82lT9cWQiA&ab_channel=NicholasRenotte)
