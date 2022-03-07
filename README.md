# Trends APIs
Green Hydrogen FastAPI apis

This project contain API which will get data from twitter and google news related to Green Hydrogen which was in trend before some days.
It will also analyse the sentiment score of content using Huggingface trained model.


To access this APIs locally follow below steps:

**First,** Install pipenv if you don't have it on your system

```
pip install pipenv
```

**Sencond,** Activate pipenv virtual environment

```
pipenv shell

```

**Third,** Install all the dependencies

```
pipenv install

```
Now your App is almost ready,

To run the **Local Server**

```
uvicorn index:app --reload

```

To access the API you will have to go to 

```
http://127.0.0.1:8000/docs

```

