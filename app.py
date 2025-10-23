import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

import os
model_path = os.path.join(os.path.dirname(__file__), 'pipe.pkl')
pipe = pickle.load(open(model_path,'rb'))
st.title('🏏 IPL Win Probability Predictor')
st.markdown("**Developed by Swaraj** | *Machine Learning Project*")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

st.markdown("### Match Situation")
target = st.number_input('Target (1st innings total + 1)', min_value=1, value=150, help="Enter the target runs (first innings total + 1)")

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score', min_value=0, value=0)
with col4:
    overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, value=0.0, step=0.1)
with col5:
    wickets = st.number_input('Wickets Out', min_value=0, max_value=10, value=0)

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(f"🏆 {batting_team}: {round(win*100)}%")
    st.header(f"🎯 {bowling_team}: {round(loss*100)}%")
    
    # Add some personal touches
    st.markdown("---")
    st.markdown("**Prediction by Swaraj's ML Model** 🤖")
    st.markdown("*Built with Python, Streamlit & Scikit-learn*")