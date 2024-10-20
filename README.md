# VinoVista: Wine Recommendation System using ML 🍷

VinoVista is an interactive web application that helps users discover new wines based on their preferences. By providing input on country and taste, users receive personalized wine recommendations. This project combines a React frontend with a Flask backend and uses machine learning to generate suggestions from a large dataset of wines.

## Features

- **Personalized Wine Suggestions**: Get recommendations based on your country and taste preferences.
- **Wine Details**: Information about wine such as name, region, description, price, and rating.
- **Flask API**: The backend, powered by Flask, processes user input and returns relevant recommendations.

## Tech Stack

- **Frontend**: React
- **Backend**: Flask (Python)
- **Machine Learning**: Content-based filtering
- **Deployment**:
  - Frontend: Vercel
  - Backend: Heroku
- **Data Source**: The wine recommendations are based on the [Wine Reviews](https://www.kaggle.com/datasets/zynicide/wine-reviews) dataset from Kaggle, which contains over 130,000 wine reviews with attributes such as price, country, variety, and rating.

## Machine Learning Overview

VinoVista uses a content-based filtering approach to recommend wines that closely match user preferences. By analyzing attributes such as country, description, and flavor notes from the dataset, the system selects the best wines to recommend. The model processes data from a known wine dataset to generate results based on similarities to the user’s input.

## How It Works

1. **User Input**: The user provides a country and a preferred taste.
2. **Backend Processing**: The Flask API receives the input and uses the wine dataset to find relevant matches.
3. **Machine Learning**: A content-based filtering approach is applied to find wines that closely match the user's preferences.
4. **Recommendations**: The system returns a list of recommended wines with details such as price, region, and rating.

## Setup Instructions

### Backend (Flask API)

1. Clone the repository.
2. Navigate to the `flask-backend/` directory and install the necessary dependencies:
   ```bash
   pip install -r flask-backend/requirements.txt
   ```
3. Run the Flask server locally:
   ```bash
   python flask-backend/app.py
   ```

### Frontend (React)

1. Navigate to the project root directory where the package.json file is located.
2. Install the required dependencies:
   ```bash
    npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
4. The frontend will now be running on http://localhost:3000/.

## Deployment

The backend is deployed using Heroku, while the frontend is hosted on Vercel. The two services communicate through API routes.

## Future Improvements

- **Enhanced Filtering**: Allow users to refine the search by wine type, price range etc.
- **User Authentication**: Let users save their preferences and past recommendations.
- **Better Recommendation Algorithm**: Explore using collaborative filtering or hybrid models to enhance recommendation accuracy.
