import uvicorn
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sentiment import analyze_sentiment
from mock_data import get_mock_tweets

# Initialize the FastAPI application
app = FastAPI(title="Social Analytics API")

# --- 1. CONFIGURATION: CORS and Static Files ---

# CORS middleware setup: Allows the frontend to access the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Static Files: This tells FastAPI to treat the 'frontend' folder as a source for CSS/JS files.
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# --- 2. MODELS & UTILITY ---

# Pydantic model for the incoming request
class TextRequest(BaseModel):
    text: str

# Helper to define the path to the frontend index file
FRONTEND_DIR = "frontend"
INDEX_HTML_PATH = os.path.join(FRONTEND_DIR, "index.html")

# --- 3. ROUTES ---

# GET endpoint for the root ("/")
# This serves the index.html file when the user hits the main URL (127.0.0.1:8000).
@app.get("/")
async def serve_frontend():
    if os.path.exists(INDEX_HTML_PATH):
        return FileResponse(INDEX_HTML_PATH, media_type="text/html")
    return {"detail": "Frontend index.html not found"}


# POST endpoint for sentiment analysis
@app.post("/analyze")
async def analyze_sentiment_endpoint(request: TextRequest):
    # Analyze sentiment of the received text
    sentiment = analyze_sentiment(request.text)
    return {"sentiment": sentiment}

# GET endpoint for mock tweets (optional)
@app.get("/api/tweets")
def get_tweets():
    tweets = get_mock_tweets()
    analyzed = [{"text": t, "sentiment": analyze_sentiment(t)} for t in tweets]
    return {"data": analyzed}

# --- 4. SERVER STARTUP ---

# Ensures the server starts correctly on port 8000.
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)