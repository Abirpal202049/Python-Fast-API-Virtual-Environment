# Virtual Enviroment using `conda`

### **Moving into the Project 1 directory**
```
cd "Project 1"
```

### **Checking the enviroment present in your system**
```
conda info --envs
```

### **Creating a virtual enviroment named `venv` in python**
```
conda create -p venv python==3.9 -y
```

### **Activating your `venv`**
```
conda activate venv/
```

### Downloading the required packages
```
pip install -r requirements.txt
```

### Starting the app
```
python -m uvicorn main:app --reload
```




  

