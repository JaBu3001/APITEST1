from fastapi import File, UploadFile, FastAPI
from PIL import Image 
import numpy as np
from PIL import Image, ImageOps
import tensorflow.keras
from typing import List


app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}
