from fastapi import FastAPI
from transformers import pipeline

## Create a new FASTAPI app instance
app = FASTAPI()

## Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")
def home():
    return {"message": "Hello World"}


## Define a function to handle the GET request at '/generate'
## 'get' is for taking request
@app.get("/generate")  
def generate(text: str):
    ## use the pipeline to generate txt from given input text
    output = pipe(text)

    ## return the generate text in JSON response
    return {"output": output[0]['generated_text']}    