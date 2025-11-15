# Heart Disease Prediction Using Logistic Regression

## 📋 Project Overview

This is an IBM Internship project that implements a **Heart Disease Prediction System** using Machine Learning. The application uses a **Logistic Regression** algorithm trained on the UCI Heart Disease Dataset to predict whether a patient has heart disease based on medical parameters.

### Key Features:
- ✅ Machine Learning model using Logistic Regression
- ✅ Flask REST API for predictions
- ✅ Professional and responsive web interface
- ✅ Real-time prediction with probability scores
- ✅ Input validation and error handling
- ✅ Mobile-friendly design
- ✅ Easy deployment ready

---

## 🏥 Medical Parameters Analyzed

The model analyzes **13 important medical parameters**:

1. **Age** - Patient's age in years (20-100)
2. **Sex** - 0 = Female, 1 = Male
3. **Chest Pain Type** - 0-3 (Typical Angina to Asymptomatic)
4. **Resting Blood Pressure** - mmHg (80-200)
5. **Serum Cholesterol** - mg/dl (100-600)
6. **Fasting Blood Sugar** - > 120 mg/dl (0 = No, 1 = Yes)
7. **Resting Electrocardiographic Result** - 0-2
8. **Maximum Heart Rate Achieved** - bpm (60-220)
9. **Exercise Induced Angina** - 0 = No, 1 = Yes
10. **ST Depression Induced** - 0-7
11. **Slope of ST Segment** - 0-2 (Upsloping to Downsloping)
12. **Number of Major Vessels** - 0-4 (colored by fluoroscopy)
13. **Thalassemia Type** - 0-3 (Normal to Thalassemia)

---

## 🚀 Project Structure

```
Sudipta IBM Project/
│
├── app.py                    # Main Flask application
├── train_model.py            # Model training script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── templates/
│   └── index.html            # Web interface HTML
│
├── static/
│   ├── style.css             # Styling (CSS)
│   └── script.js             # Frontend JavaScript
│
└── models/                   # Trained ML models (created after training)
    ├── heart_disease_model.pkl
    ├── scaler.pkl
    └── feature_names.pkl
```

---

## 📦 Installation & Setup

### Step 1: Install Python
Make sure you have Python 3.8 or higher installed. Download from [python.org](https://www.python.org)

### Step 2: Clone/Download Project
Navigate to your project folder using command prompt or PowerShell.

### Step 3: Create Virtual Environment (Recommended)
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🏋️ Training the Model

The model needs to be trained before running the application. The training script will download the UCI Heart Disease Dataset and train the logistic regression model.

### Run the training script:
```bash
python train_model.py
```

This will:
1. Download the UCI Heart Disease Dataset
2. Train a Logistic Regression model
3. Scale the features using StandardScaler
4. Save the model, scaler, and feature names to the `models/` directory
5. Display model accuracy and classification metrics

**Expected Output:**
- Model saved successfully in `models/` folder
- Accuracy typically around 85-90%

---

## 🌐 Running the Application

### Start the Flask development server:
```bash
python app.py
```

### Open your browser and navigate to:
```
http://localhost:5000
```

The application will be running on your local machine!

---

## 📝 Using the Application

1. **Access the Web Interface**: Open http://localhost:5000 in your browser
2. **Fill Patient Information**: Enter all 13 medical parameters
3. **Click Predict Button**: The model will analyze the data
4. **View Results**: Get prediction with:
   - Disease/No Disease diagnosis
   - Probability percentages
   - Confidence score
   - Recommendations

---

## 🔌 API Endpoints

### POST /predict
Makes a heart disease prediction based on patient data.

**Request Body (JSON):**
```json
{
    "age": 45,
    "sex": 1,
    "cp": 1,
    "trestbps": 130,
    "chol": 200,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.5,
    "slope": 1,
    "ca": 0,
    "thal": 2
}
```

**Response (JSON):**
```json
{
    "success": true,
    "prediction": 0,
    "disease_probability": 23.45,
    "no_disease_probability": 76.55,
    "diagnosis": "No Heart Disease",
    "confidence": 76.55
}
```

### GET /api/info
Returns information about the model.

**Response:**
```json
{
    "model_name": "Heart Disease Prediction",
    "algorithm": "Logistic Regression",
    "features_count": 13,
    "features": [...]
}
```

---

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: Scikit-learn (Logistic Regression)
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: Flask REST API
- **Server**: Gunicorn (for production)

---

## 📊 Model Performance

The Logistic Regression model is trained with:
- **Dataset**: UCI Heart Disease Dataset (303 patients)
- **Training/Testing Split**: 80/20
- **Features**: 13 medical parameters
- **Typical Accuracy**: 85-90%
- **Algorithm**: Logistic Regression with feature scaling

---

## 🚀 Deployment Guide

### Option 1: Deploy on PythonAnywhere

1. Create account at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your project files
3. Create a virtual environment
4. Install dependencies from `requirements.txt`
5. Configure WSGI file
6. Set domain and enable HTTPS
7. Your app will be live!

### Option 2: Deploy on Heroku

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Create `Procfile`:
```
web: gunicorn app:app
```
3. Create `runtime.txt`:
```
python-3.9.16
```
4. Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Option 3: Deploy with Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
```

Build and run:
```bash
docker build -t heart-disease-pred .
docker run -p 5000:5000 heart-disease-pred
```

---

## ⚠️ Important Disclaimer

**This application is for educational and research purposes only.**

- It should NOT be used as a substitute for professional medical advice
- Always consult with qualified healthcare professionals
- Machine learning models can have errors and limitations
- The predictions may not be 100% accurate
- Medical decisions should be made by licensed physicians

---

## 📚 Dataset Reference

**UCI Machine Learning Repository - Heart Disease Dataset**
- Source: https://archive.ics.uci.edu/ml/datasets/heart+disease
- Donors: David W. Aha & Gilbert Cichanowski
- Records: 303 patients
- Classes: 2 (Disease / No Disease)
- Features: 13

---

## 🔒 Privacy & Security

- Patient data is processed locally
- No data is stored on the server
- HTTPS should be enabled in production
- Consider GDPR/HIPAA compliance for production use

---

## 📝 Project Files Explanation

### `app.py`
- Main Flask application
- API endpoints for predictions
- Input validation
- Model loading and prediction logic

### `train_model.py`
- Downloads UCI Heart Disease Dataset
- Trains Logistic Regression model
- Performs feature scaling
- Saves model artifacts
- Displays model metrics

### `templates/index.html`
- Professional web interface
- Multi-section design (Hero, About, Prediction, Info)
- Responsive form with all 13 parameters
- Result display with visualizations
- Mobile-friendly layout

### `static/style.css`
- Modern and professional styling
- Responsive design for all devices
- Smooth animations and transitions
- Color scheme optimized for healthcare app
- Gradient backgrounds and shadows

### `static/script.js`
- Form validation
- API communication
- Result rendering
- Loading states
- Error handling
- Navigation functionality

---

## 🐛 Troubleshooting

### Issue: Model not found error
**Solution**: Run `python train_model.py` first

### Issue: Module not found (e.g., Flask, scikit-learn)
**Solution**: Run `pip install -r requirements.txt`

### Issue: Port 5000 already in use
**Solution**: Change port in `app.py` or kill process on port 5000

### Issue: Form not submitting
**Solution**: Check browser console for errors (F12 → Console tab)

---

## 📞 Support & Documentation

For more information on the technologies used:
- Flask: https://flask.palletsprojects.com
- Scikit-learn: https://scikit-learn.org
- UCI Dataset: https://archive.ics.uci.edu

---

## ✅ Checklist for Project Submission

- [x] Machine Learning model created and trained
- [x] Flask API with prediction endpoint
- [x] Professional web interface
- [x] Input validation and error handling
- [x] Responsive design (mobile-friendly)
- [x] Complete documentation
- [x] Requirements.txt for dependencies
- [x] Deployment ready
- [x] Privacy & security considerations
- [x] Medical disclaimer

---

## 📄 License

This project is created for educational purposes as part of IBM Internship.

---

## 👨‍💻 Author

**Your Name**  
Created as part of IBM Internship Project - Heart Disease Prediction using Machine Learning

**Date**: November 2025

---

**Last Updated**: November 15, 2025  
**Version**: 1.0
#   I B M _ H e a r t _ D i s e a s e _ P r e d i c t o r  
 