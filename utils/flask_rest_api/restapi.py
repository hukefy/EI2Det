"""
Run a rest API exposing the yolov5s object detection model
"""
import argparse
import io

import torch
from PIL import Image
from flask import Flask, request

app = Flask(__name__)

DETECTION_URL = "/v1/object-detection/yolov5s"


@app.route(DETECTION_URL, methods=["POST"])
def predict():
    if not request.method == "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()

        img = Image.open(io.BytesIO(image_bytes))

        results = model(img, size=640)  # reduce size=320 for faster inference
        return results.pandas().xyxy[0].to_json(orient="records")

