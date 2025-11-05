#  Social Analytics Dashboard: Real-time Sentiment Analysis

This is a full-stack web application developed to analyze and visualize the sentiment (Positive, Negative, or Neutral) of user-provided text, simulating real-time social media messages. The project demonstrates proficiency in data analysis, machine learning integration, and full-stack development.

## Key Features
* **Text Classification:** Implements a pre-trained machine learning model (e.g., [Mention your specific model, like Naive Bayes or Logistic Regression]) to determine sentiment with high accuracy.
* **RESTful API:** Developed a clean, Python-based API (using Flask) to expose the sentiment analysis function to the frontend.
* **Secure Configuration:** Utilizes environment variables (`.env`) for secure management of sensitive keys and tokens.
* **Responsive Frontend:** Built with standard web technologies (HTML, CSS, JavaScript) to provide a clear and interactive user interface.

## Tech Stack
* **Backend:** Python 3.x, Flask, [Your Sentiment Library, e.g., NLTK/TextBlob], scikit-learn
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS)
* **Package Management:** `requirements.txt` (Python), `package.json` (Node/JS)

## Local Setup and Installation

Follow these steps to run the application locally.

### Prerequisites
* Python 3.x installed
* Node.js and npm installed (for frontend dependencies)

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [Your-Repo-URL]
    cd social-analytics-dashboard
    ```

2.  **Backend Setup (Python):**
    * **Activate Environment:** (Uses the `.venv` folder)
        ```bash
        .\.venv\Scripts\Activate.ps1
        ```
    * **Install Dependencies:**
        ```bash
        pip install -r requirements.txt
        ```

3.  **Frontend Setup (JavaScript):**
    * Navigate to the frontend folder:
        ```bash
        cd frontend
        npm install
        ```
    * Return to the root directory:
        ```bash
        cd ..
        ```

4.  **Security/Environment:**
    * Create a file named **`.env`** in the root directory and add any necessary API keys (Refer to a `.env.example` file if created).

### Running the Application

1.  **Start the Backend API:**
    ```bash
    .\.venv\Scripts\python main.py
    ```
2.  **Access:** Open your browser to the URL displayed by Flask (typically `http://127.0.0.1:5000/`).