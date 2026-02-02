from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
import tensorflow as tf
import io

from model import generator
from utils import preprocess_image, rgb_to_l, reconstruct_rgb

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/colorize")
async def colorize_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    image = np.array(image)

    image = preprocess_image(image)
    L, _ = rgb_to_l(image.numpy())

    L = tf.convert_to_tensor(L)[None, ...]
    AB_pred = generator.predict(L)[0]

    rgb_out = reconstruct_rgb(L[0], AB_pred)

    out_img = Image.fromarray(rgb_out)
    buf = io.BytesIO()
    out_img.save(buf, format="PNG")

    return {
        "image": buf.getvalue().hex()
    }
    