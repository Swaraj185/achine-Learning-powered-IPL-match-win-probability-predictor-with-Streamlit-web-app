import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# Create a simple mock model for demonstration
# This is a basic version - in reality you'd need the actual IPL data

# Mock data for training
np.random.seed(42)
n_samples = 1000

# Create mock features
batting_teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 
                'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 
                'Rajasthan Royals', 'Delhi Capitals']
bowling_teams = batting_teams.copy()
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# Generate mock data
data = {
    'batting_team': np.random.choice(batting_teams, n_samples),
    'bowling_team': np.random.choice(bowling_teams, n_samples),
    'city': np.random.choice(cities, n_samples),
    'runs_left': np.random.randint(0, 200, n_samples),
    'balls_left': np.random.randint(1, 120, n_samples),
    'wickets': np.random.randint(1, 10, n_samples),
    'total_runs_x': np.random.randint(100, 250, n_samples),
    'crr': np.random.uniform(5, 12, n_samples),
    'rrr': np.random.uniform(5, 15, n_samples),
    'result': np.random.randint(0, 2, n_samples)
}

df = pd.DataFrame(data)

# Prepare features and target
X = df[['batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left', 
        'wickets', 'total_runs_x', 'crr', 'rrr']]
y = df['result']

# Create transformer for categorical variables
trf = ColumnTransformer([
    ('trf', OneHotEncoder(drop='first'), ['batting_team', 'bowling_team', 'city'])
], remainder='passthrough')

# Create pipeline
pipe = Pipeline(steps=[
    ('step1', trf),
    ('step2', LogisticRegression(solver='liblinear', random_state=42))
])

# Train the model
pipe.fit(X, y)

# Save the model
pickle.dump(pipe, open('pipe.pkl', 'wb'))
print("Mock model created and saved as pipe.pkl")
print("Model accuracy on training data:", pipe.score(X, y))
