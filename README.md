# 🏏 IPL Win Probability Predictor

A machine learning-powered web application that predicts the win probability of IPL (Indian Premier League) matches in real-time based on current match situation.

## 🚀 Features

- **Real-time Predictions**: Get win probabilities based on current match state
- **8 IPL Teams**: All major IPL franchises supported
- **29 Venues**: Comprehensive city selection
- **Interactive Dashboard**: User-friendly Streamlit interface
- **Machine Learning Model**: Logistic Regression trained on match data

## 🛠️ Technical Stack

- **Python 3.13**
- **Streamlit** - Web framework
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning
- **Pickle** - Model serialization

## 📊 How It Works

The application uses a Logistic Regression model trained on historical IPL data to predict match outcomes based on:

- **Batting Team** vs **Bowling Team**
- **Venue** (city)
- **Target** (runs needed to win)
- **Current Score** (runs scored so far)
- **Overs Completed** (progress in innings)
- **Wickets Out** (wickets fallen)

## 🚀 Quick Start

### Prerequisites
```bash
pip install streamlit pandas numpy scikit-learn
```

### Running the Application
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## 📱 Usage

1. **Select Teams**: Choose batting and bowling teams
2. **Choose Venue**: Select the host city
3. **Enter Match Details**:
   - Target (1st innings total + 1)
   - Current score
   - Overs completed
   - Wickets out
4. **Get Prediction**: Click "Predict Probability" to see win percentages

## 🎯 Example

- **Target**: 180 (if 1st innings was 179)
- **Current Score**: 120
- **Overs**: 15.0
- **Wickets**: 2
- **Result**: Win probability percentages for both teams

## 📈 Model Performance

- **Algorithm**: Logistic Regression
- **Features**: Team, venue, runs left, balls left, wickets, CRR, RRR
- **Preprocessing**: One-hot encoding for categorical variables
- **Pipeline**: Automated data transformation and prediction

## 🔧 Project Structure

```
ipl-win-probability-predictor/
├── app.py                 # Main Streamlit application
├── pipe.pkl              # Trained machine learning model
├── create_mock_model.py  # Model training script
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── setup.sh              # Streamlit configuration
└── README.md             # Project documentation
```

## 🌟 Key Highlights

- **End-to-end ML Pipeline**: From data preprocessing to web deployment
- **Real-time Predictions**: Live match situation analysis
- **Sports Analytics**: Domain-specific machine learning application
- **Interactive UI**: User-friendly web interface
- **Production Ready**: Deployable web application

## 🎓 Learning Outcomes

This project demonstrates:
- Machine learning model development
- Web application development with Streamlit
- Data preprocessing and feature engineering
- Model deployment and web hosting
- Sports analytics and predictive modeling

## 📝 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for IPL fans and data science enthusiasts!**