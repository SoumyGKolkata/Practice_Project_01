from fastapi import FastAPI
from pydantic import BaseModel 
from app.ai_logic import simple_ai_response


app = FastAPI()

class requestdata(BaseModel):
    text : str

@app.get("/")
def home():
    return{"message":"API is running"}

@app.post("/predict")
def predict(data: requestdata):
    result = simple_ai_response(data.text)
    return {"response": result}