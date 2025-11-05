# Social Analytics Dashboard (Full Stack)

This project is a decoupled full-stack application designed to analyze user-submitted text for sentiment (positive, negative, or neutral). It uses a Python FastAPI backend for high-performance analysis and a simple, vanilla HTML/CSS/JavaScript frontend for the user interface.

This architecture showcases skills in building RESTful APIs, static file serving, and dependency management for both the client and server sides.

## Key Technologies

### Backend (Python)
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (For high-speed API development and automatic documentation).
* **Analysis:** [TextBlob](https://textblob.readthedocs.io/en/dev/) (For sentiment scoring).
* **Server:** [Uvicorn](https://www.uvicorn.org/) (Asynchronous Server Gateway Interface/ASGI server).

### Frontend (Web Client)
* **Structure:** HTML5
* **Styling:** Custom CSS
* **Logic:** Vanilla JavaScript (ES6+), responsible for fetching and displaying data from the API.

## Local Setup and Installation

Follow these steps to clone the repository and install all necessary dependencies for both the Python and JavaScript environments.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/social-analytics-dashboard.git](https://github.com/your-username/social-analytics-dashboard.git)
cd social-analytics-dashboard

### 2. Set up Python Backend Dependencies

The project uses a virtual environment (`.venv`) for isolation.

```bash
# Activate the virtual environment (Windows/PowerShell)
.\.venv\Scripts\Activate.ps1

# Install required Python packages (FastAPI, TextBlob, Uvicorn, etc.)
pip install -r requirements.txt

cd frontend
npm install
cd ..

#To run the Application
python backend/main.py


