# Quick Start Guide for Heart Disease Prediction Project

## Windows Users - Step by Step Setup

### Step 1: Open PowerShell or Command Prompt
Press `Win + R`, type `powershell` or `cmd`, and press Enter.

### Step 2: Navigate to Project Directory
```powershell
cd "d:\Sudipta IBM Project"
```

### Step 3: Create Virtual Environment
```powershell
python -m venv venv
```

### Step 4: Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```
(If you get an error about execution policy, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)

### Step 5: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 6: Train the Model
```powershell
python train_model.py
```
Wait for completion. You should see:
- Dataset loaded
- Model trained
- Accuracy displayed
- Model files saved in `models/` folder

### Step 7: Run the Application
```powershell
python app.py
```

### Step 8: Open in Browser
Open your web browser and go to: `http://localhost:5000`

---

## Linux/Mac Users - Step by Step Setup

### Step 1: Open Terminal

### Step 2: Navigate to Project Directory
```bash
cd "path/to/Sudipta IBM Project"
```

### Step 3: Create Virtual Environment
```bash
python3 -m venv venv
```

### Step 4: Activate Virtual Environment
```bash
source venv/bin/activate
```

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 6: Train the Model
```bash
python train_model.py
```

### Step 7: Run the Application
```bash
python app.py
```

### Step 8: Open in Browser
Open your web browser and go to: `http://localhost:5000`

---

## Troubleshooting

### Problem: Python command not found
**Solution**: 
- Make sure Python is installed: `python --version`
- If not installed, download from python.org

### Problem: pip install fails
**Solution**:
- Update pip first: `python -m pip install --upgrade pip`
- Then try installing requirements again

### Problem: Virtual environment won't activate
**Solution** (Windows):
- Run PowerShell as Administrator
- Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Then try activating again

### Problem: Port 5000 already in use
**Solution**:
- Change port in app.py (last line): `app.run(debug=True, host='0.0.0.0', port=5001)`
- Or stop other applications using port 5000

### Problem: Module not found error
**Solution**:
- Make sure you've activated the virtual environment
- Make sure you've run `pip install -r requirements.txt`

---

## After Running Successfully

1. **Access the Application**: Go to http://localhost:5000
2. **Test Prediction**: Fill in patient data and click "Predict"
3. **View Results**: See the prediction with probabilities
4. **Print Report**: Use the print function to save results

---

## Stop the Application

Press `Ctrl + C` in the terminal/command prompt

---

## Deactivate Virtual Environment

```powershell
# Windows
deactivate

# Linux/Mac
deactivate
```

---

## Next Steps

### For Development:
- Modify HTML in `templates/index.html`
- Update styles in `static/style.css`
- Enhance JavaScript in `static/script.js`
- Improve model in `train_model.py`

### For Deployment:
- See README.md for deployment options
- Options: PythonAnywhere, Heroku, Docker, AWS, etc.

### For Learning:
- Read through all files to understand the project
- Modify parameters to see how they affect predictions
- Experiment with different ML algorithms

---

## Project Features

✅ Machine Learning model (Logistic Regression)
✅ Professional web interface
✅ Real-time predictions
✅ Mobile responsive design
✅ Input validation
✅ Error handling
✅ Beautiful UI with animations
✅ Deployment ready

---

## Questions?

Refer to README.md for:
- Detailed project information
- API documentation
- Deployment guides
- Technology stack details

Happy Coding! 🚀
