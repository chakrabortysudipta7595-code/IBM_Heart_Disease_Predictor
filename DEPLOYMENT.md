# Deployment Guide - Heart Disease Prediction Application

Complete guide to deploy your Heart Disease Prediction application to production servers.

---

## 📋 Table of Contents
1. [Deployment on PythonAnywhere](#deployment-on-pythonanywhere)
2. [Deployment on Heroku](#deployment-on-heroku)
3. [Deployment with Docker](#deployment-with-docker)
4. [Deployment on AWS](#deployment-on-aws)
5. [Deployment on DigitalOcean](#deployment-on-digitalocean)
6. [General Production Tips](#general-production-tips)

---

## 🌐 Deployment on PythonAnywhere

**PythonAnywhere** is the easiest option for beginners. It requires no command line knowledge.

### Step 1: Create Account
1. Go to https://www.pythonanywhere.com
2. Click "Sign up" and create a free account
3. Verify your email

### Step 2: Upload Project Files
1. Go to "Files" tab
2. Create a new directory: `heartdisease`
3. Upload all files from your local project (except `venv` and `__pycache__`)
4. Include: `app.py`, `train_model.py`, `requirements.txt`, `templates/`, `static/`

### Step 3: Create Virtual Environment
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration" → "Python 3.9"
4. Note the path shown (usually `/home/yourusername/mysite`)

In "Files", navigate to your home directory and create virtual environment:
1. Open Bash console (in Web tab)
2. Run:
```bash
cd /home/yourusername
mkvirtualenv --python=/usr/bin/python3.9 heartdisease
pip install -r /home/yourusername/heartdisease/requirements.txt
python /home/yourusername/heartdisease/train_model.py
```

### Step 4: Configure WSGI File
1. Go to "Web" tab
2. Click on your web app
3. Click "WSGI configuration file" in the "Code" section
4. Replace content with:

```python
import sys
path = '/home/yourusername/heartdisease'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

### Step 5: Reload Application
1. Go to "Web" tab
2. Click "Reload" button
3. Your app is live! (URL will be shown)

---

## 🚀 Deployment on Heroku

**Heroku** provides free tier deployment with automatic scaling.

### Prerequisites
- Git installed (https://git-scm.com)
- Heroku CLI installed (https://devcenter.heroku.com/articles/heroku-cli)
- GitHub account (optional but recommended)

### Step 1: Prepare Project
Your project should already have:
- ✅ `requirements.txt` (created)
- ✅ `Procfile` (created)
- ✅ `runtime.txt` (created)

### Step 2: Initialize Git Repository
```bash
cd "d:\Sudipta IBM Project"
git init
git config user.email "your-email@example.com"
git config user.name "Your Name"
git add .
git commit -m "Initial commit - Heart Disease Prediction App"
```

### Step 3: Create Heroku App
```bash
heroku login
heroku create your-app-name
```
(Replace `your-app-name` with a unique name like `heart-disease-sudipta`)

### Step 4: Deploy to Heroku
```bash
git push heroku main
# or if your branch is master:
git push heroku master
```

### Step 5: Train Model on Heroku
```bash
heroku run python train_model.py
```

### Step 6: View Your App
```bash
heroku open
```

Your app is now live! URL format: `https://your-app-name.herokuapp.com`

### Monitor Logs
```bash
heroku logs --tail
```

---

## 🐳 Deployment with Docker

**Docker** packages your app with all dependencies for consistent deployment anywhere.

### Prerequisites
- Docker Desktop installed (https://www.docker.com/products/docker-desktop)

### Step 1: Build Docker Image
```bash
cd "d:\Sudipta IBM Project"
docker build -t heart-disease-pred .
```

### Step 2: Train Model in Container
```bash
docker run -v "$(pwd)/models:/app/models" heart-disease-pred python train_model.py
```

### Step 3: Run Application
```bash
docker run -p 5000:5000 -v "$(pwd)/models:/app/models" heart-disease-pred
```

Access at: `http://localhost:5000`

### Step 4: Deploy to Docker Hub
```bash
docker login
docker tag heart-disease-pred yourusername/heart-disease-pred
docker push yourusername/heart-disease-pred
```

### Step 5: Deploy to Cloud with Docker
Options like **AWS ECS**, **Google Cloud Run**, **Azure Container Instances** support Docker containers.

---

## ☁️ Deployment on AWS

### Using AWS Elastic Beanstalk

#### Prerequisites
- AWS account (https://aws.amazon.com)
- AWS CLI installed
- Elastic Beanstalk CLI installed

#### Step 1: Prepare Project
Create `.ebextensions/python.config`:
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app:app
  aws:autoscaling:launchconfiguration:
    InstanceType: t2.micro
```

#### Step 2: Initialize EB Project
```bash
pip install awsebcli --upgrade
eb init -p "Python 3.9" heartdisease --region us-east-1
```

#### Step 3: Create Environment
```bash
eb create heartdisease-env
```

#### Step 4: Deploy
```bash
git add .
git commit -m "Deploy to AWS"
eb deploy
```

#### Step 5: Open Application
```bash
eb open
```

---

## 💧 Deployment on DigitalOcean

### Using DigitalOcean App Platform (Easiest)

#### Step 1: Push to GitHub
1. Create GitHub repository
2. Push your code:
```bash
git remote add origin https://github.com/yourusername/heart-disease-pred.git
git branch -M main
git push -u origin main
```

#### Step 2: Connect to DigitalOcean
1. Go to https://cloud.digitalocean.com
2. Go to "Apps" → "Create Apps"
3. Select GitHub repository
4. DigitalOcean will detect `Procfile` automatically
5. Click "Deploy"

#### Step 3: Set Build Command
- Build command: `pip install -r requirements.txt && python train_model.py`

Your app will be live at a DigitalOcean URL!

---

## 🔧 General Production Tips

### 1. Environment Variables
Create `.env` file in production:
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

Update `app.py` to use environment variables:
```python
from dotenv import load_dotenv
import os

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')
```

### 2. Update requirements.txt for Production
```bash
pip install gunicorn python-dotenv
pip freeze > requirements.txt
```

### 3. Use Gunicorn Instead of Flask Debug Server
```bash
gunicorn app:app --workers=4 --bind=0.0.0.0:5000
```

### 4. Enable HTTPS/SSL
- PythonAnywhere: Automatic with free Let's Encrypt
- Heroku: Automatic HTTPS
- AWS: Use AWS Certificate Manager
- DigitalOcean: Enable auto-renewal

### 5. Setup Database Backup
- Keep model files backed up
- Consider AWS S3 for model storage
- Regular backups of training data

### 6. Monitor Application
- Setup error logging (Sentry, DataDog)
- Monitor performance metrics
- Setup alerts for errors

### 7. Security Best Practices
```python
# In production
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
```

### 8. Rate Limiting
```bash
pip install Flask-Limiter
```

Add to app.py:
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/predict', methods=['POST'])
@limiter.limit("10 per minute")
def predict():
    # ... existing code
```

### 9. Setup Custom Domain
1. Register domain on GoDaddy, Namecheap, etc.
2. Point DNS to your hosting provider
3. Setup SSL certificate

### 10. Performance Optimization
```python
# Cache model loading
from functools import lru_cache

@lru_cache(maxsize=1)
def get_model():
    return pickle.load(open('models/heart_disease_model.pkl', 'rb'))
```

---

## 🚨 Troubleshooting Deployment

### Issue: Model not found in production
**Solution**: 
- Ensure model training runs during deployment
- Store models in persistent storage
- Check file paths in app.py

### Issue: Application timeout
**Solution**:
- Optimize model prediction (pre-load in memory)
- Use caching
- Increase timeout limits

### Issue: High memory usage
**Solution**:
- Use smaller ML models
- Implement request queuing
- Use autoscaling

### Issue: Database connection errors
**Solution**:
- Check connection strings
- Verify firewall rules
- Use connection pooling

---

## 📊 Recommended Hosting for Scale

| Provider | Best For | Cost | Ease |
|----------|----------|------|------|
| PythonAnywhere | Beginners | Free/$5/mo | ⭐⭐⭐ |
| Heroku | Quick deployment | Free/$50/mo | ⭐⭐⭐ |
| AWS | Large scale | Pay-as-you-go | ⭐ |
| DigitalOcean | Balance | $5+/mo | ⭐⭐ |
| Docker + VPS | Full control | $5+/mo | ⭐ |

---

## ✅ Deployment Checklist

Before deploying to production:

- [ ] All files committed to Git
- [ ] requirements.txt updated
- [ ] .env.example created (no secrets in code)
- [ ] Model training verified locally
- [ ] All tests passing
- [ ] Error handling in place
- [ ] Logging configured
- [ ] HTTPS enabled
- [ ] Rate limiting configured
- [ ] Database backups setup
- [ ] Monitoring alerts configured
- [ ] Documentation updated
- [ ] GDPR/privacy compliance checked

---

## 📞 Support

For deployment help:
- PythonAnywhere Help: https://www.pythonanywhere.com/forums/
- Heroku Support: https://devcenter.heroku.com
- Docker Docs: https://docs.docker.com
- AWS Help: https://docs.aws.amazon.com

---

**Happy Deploying!** 🚀
