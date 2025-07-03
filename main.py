import os
import requests
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

DEEPAI_API_KEY = os.getenv("DEEPAI_API_KEY")

@app.post("/moderate")
async def moderate_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    response = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={"image": (file.filename, await file.read())},
        headers={"api-key": DEEPAI_API_KEY},
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error contacting DeepAI API")

    nsfw_score = response.json().get("output", {}).get("nsfw_score", 0)

    if nsfw_score > 0.7:
        return JSONResponse(status_code=200, content={"status": "REJECTED", "reason": "NSFW content"})
    return {"status": "OK"}
