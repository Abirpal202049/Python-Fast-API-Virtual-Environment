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


# **`nohup`**
## **How to run uvicorn in background**
To run Uvicorn in the background, you can use the following command:

```bash
nohup uvicorn app_name:app --host 0.0.0.0 --port 8000 > uvicorn.log 2>&1 &
```
Here's what each part of the command does:

- `nohup`: This command is used to run a command in the background and ignore the hangup (HUP) signal. This prevents the command from being terminated when you log out of the shell.
- `uvicorn app_name:app`: This command starts the Uvicorn server for the app named `app_name` using the ASGI application object named `app`.
- `--host 0.0.0.0`: This command tells Uvicorn to bind to all available network interfaces, allowing external access to the server.
- `--port 8000`: This command specifies the port number to use for the server. You can replace 8000 with any available port number.
- `> uvicorn.log 2>&1`: This command redirects the output of the Uvicorn server to a log file named `uvicorn.log`. The `2>&1` part of the command redirects standard error (stderr) to standard output (stdout), which is then redirected to the log file.
- `&`: This command runs the command in the background.
With this command, Uvicorn will start running in the background, and you can log out of the shell without stopping the server. You can view the server logs by checking the uvicorn.log file.



## **And how to stop this**
To stop a Uvicorn server that is running in the background, you can use the ps and kill commands to find and kill the process.

1. Use the ps command to find the process ID (PID) of the Uvicorn process that is running in the background. You can use the following command to do this:
```perl
ps aux | grep uvicorn
```
This command will list all processes that contain the word "uvicorn". Look for the process that corresponds to your Uvicorn server.

2. Once you have identified the PID of the Uvicorn process, use the kill command to stop it. You can use the following command to do this:
```bash
kill <PID>
```
Replace `<PID>` with the actual process ID that you obtained in the previous step.

Alternatively, you can use the `pkill` command to kill all processes that match a certain pattern. You can use the following command to do this:
```shell
pkill -f "uvicorn app_name:app"
```
Replace `app_name:app` with the name of your Uvicorn application.

After running the `kill` or `pkill` command, the Uvicorn server will stop running in the background. You can verify that the server has stopped by checking the server logs and ensuring that no requests are being served.



## **What is `nohup`**
`nohup` is a command that is used to run a command or shell script in the background even after you log out of the shell. The name `nohup` stands for "no hangup", and it is used to prevent the hangup (HUP) signal from terminating the command when you log out of the shell.

When you run a command with `nohup`, the output of the command is redirected to a file named `nohup.out` in the current directory. This allows you to check the output of the command at a later time.

Here's an example of how to use `nohup`:

```bash
nohup python my_script.py > my_script.log &
```
This command runs the Python script `my_script.py` in the background using nohup. The output of the script is redirected to a file named my_script.log, and the & symbol is used to run the command in the background.

By using `nohup`, you can start long-running processes that continue to run even after you log out of the shell, which is particularly useful when you need to run a process that takes a long time to complete.

## **Is it good to use nohup**
Yes, using `nohup` can be a good option for running long-running processes or commands in the background. By using `nohup`, you can ensure that the process or command continues to run even after you log out of the shell, and you can redirect the output to a log file for later review.

Using `nohup` can also be useful when running commands that may be interrupted by a hangup (HUP) signal. By default, when you log out of a shell, any processes that are running in that shell are sent a HUP signal, which can cause them to terminate. However, when you run a command with `nohup`, the HUP signal is ignored, and the command continues to run.

That being said, there may be other ways to run long-running processes or commands, such as using a process manager or running the command in a screen or tmux session. The best option for running a long-running process will depend on the specific use case and requirements.


## **How to redirect the output to a log file**
To redirect the output of a command or process to a log file, you can use the redirection operator > followed by the name of the log file. Here's an example:

```BASH
python my_script.py > my_script.log
```
In this example, the output of the python my_script.py command is redirected to a file named my_script.log. Any output that would normally appear in the terminal will instead be written to the log file.

If you want to append the output to the log file rather than overwrite it, you can use the >> operator instead of >:

```c
python my_script.py >> my_script.log
```
In this case, any output will be added to the end of the log file rather than overwriting the existing contents.

You can also combine nohup with output redirection to run a command or process in the background and redirect the output to a log file:

```bash
nohup python my_script.py > my_script.log 2>&1 &
```
This command runs the python my_script.py command in the background using nohup, and redirects both standard output (stdout) and standard error (stderr) to the my_script.log file. The 2>&1 portion of the command redirects stderr to the same place as stdout. The & symbol is used to run the command in the background.

With this command, any output that would normally appear in the terminal will instead be written to the log file, and the process will continue running even after you log out of the shell.