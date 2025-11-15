/**
 * Heart Disease Prediction - Frontend JavaScript
 * Handles form submission, API calls, and result display
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize event listeners
    const predictionForm = document.getElementById('predictionForm');
    if (predictionForm) {
        predictionForm.addEventListener('submit', handleFormSubmit);
    }

    // Smooth navigation links
    setupNavigation();
});

/**
 * Handle form submission
 */
function handleFormSubmit(e) {
    e.preventDefault();

    // Get form data
    const formData = new FormData(document.getElementById('predictionForm'));
    const data = Object.fromEntries(formData);

    // Validate form data
    if (!validateFormData(data)) {
        return;
    }

    // Show loading spinner
    showLoadingSpinner();

    // Hide previous results
    document.getElementById('resultContainer').style.display = 'none';

    // Send prediction request
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        hideLoadingSpinner();
        if (data.success) {
            displayResult(data);
        } else {
            displayError(data.error);
        }
    })
    .catch(error => {
        hideLoadingSpinner();
        displayError('Error connecting to server: ' + error.message);
    });
}

/**
 * Validate form data
 */
function validateFormData(data) {
    const errors = [];

    // Check if all fields are filled
    const requiredFields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                           'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'];
    
    for (let field of requiredFields) {
        if (!data[field] && data[field] !== '0') {
            errors.push(`${field} is required`);
        }
    }

    if (errors.length > 0) {
        displayError('Please fill all required fields');
        return false;
    }

    // Validate age
    const age = parseInt(data.age);
    if (age < 20 || age > 100) {
        displayError('Age must be between 20 and 100');
        return false;
    }

    // Validate blood pressure
    const trestbps = parseInt(data.trestbps);
    if (trestbps < 80 || trestbps > 200) {
        displayError('Resting blood pressure must be between 80 and 200');
        return false;
    }

    // Validate cholesterol
    const chol = parseInt(data.chol);
    if (chol < 100 || chol > 600) {
        displayError('Cholesterol must be between 100 and 600');
        return false;
    }

    // Validate max heart rate
    const thalach = parseInt(data.thalach);
    if (thalach < 60 || thalach > 220) {
        displayError('Maximum heart rate must be between 60 and 220');
        return false;
    }

    return true;
}

/**
 * Display prediction result
 */
function displayResult(data) {
    const resultContainer = document.getElementById('resultContainer');
    const resultBox = document.getElementById('resultBox');

    const isDisease = data.prediction === 1;
    const boxClass = isDisease ? 'danger' : 'success';
    const icon = isDisease ? 'fa-heart-crack' : 'fa-heart';
    const iconColor = isDisease ? 'red' : 'green';

    let resultHTML = `
        <div class="result-box ${boxClass}">
            <div class="result-header">
                <div class="result-icon">
                    <i class="fas ${icon}"></i>
                </div>
                <div class="result-diagnosis">${data.diagnosis}</div>
            </div>

            <div class="result-probabilities">
                <div class="probability-item">
                    <div class="probability-label">No Disease Probability</div>
                    <div class="probability-value">${data.no_disease_probability.toFixed(2)}%</div>
                </div>
                <div class="probability-item">
                    <div class="probability-label">Disease Probability</div>
                    <div class="probability-value">${data.disease_probability.toFixed(2)}%</div>
                </div>
            </div>

            <div class="confidence-bar">
                <div class="confidence-fill" style="width: ${data.confidence}%">
                    ${data.confidence.toFixed(2)}% Confidence
                </div>
            </div>

            <div class="result-message">
    `;

    if (isDisease) {
        resultHTML += `
                <strong style="color: var(--danger-color);">⚠️ Heart Disease Risk Detected</strong><br><br>
                The model indicates a potential risk of heart disease based on the provided medical parameters.
                <br><br>
                <strong>Recommended Actions:</strong>
                <ul style="margin-left: 20px; margin-top: 10px;">
                    <li>Consult with a qualified cardiologist for professional evaluation</li>
                    <li>Undergo comprehensive cardiac tests (ECG, Echocardiogram, etc.)</li>
                    <li>Follow medical advice for treatment and management</li>
                    <li>Adopt a heart-healthy lifestyle with regular exercise</li>
                    <li>Monitor your vital signs regularly</li>
                </ul>
        `;
    } else {
        resultHTML += `
                <strong style="color: var(--success-color);">✓ No Heart Disease Detected</strong><br><br>
                The model predicts that the patient is not at immediate risk of heart disease.
                <br><br>
                <strong>Recommendations:</strong>
                <ul style="margin-left: 20px; margin-top: 10px;">
                    <li>Continue regular health check-ups</li>
                    <li>Maintain a healthy lifestyle with balanced diet and exercise</li>
                    <li>Monitor blood pressure and cholesterol levels</li>
                    <li>Manage stress through relaxation techniques</li>
                    <li>Avoid smoking and limit alcohol consumption</li>
                </ul>
        `;
    }

    resultHTML += `
            </div>

            <div class="result-actions">
                <button class="btn btn-primary" onclick="scrollToForm()">
                    <i class="fas fa-redo"></i> New Prediction
                </button>
                <button class="btn btn-secondary" onclick="printResult()">
                    <i class="fas fa-print"></i> Print Report
                </button>
            </div>

            <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid var(--light-color); font-size: 0.9rem; color: var(--gray-color);">
                <i class="fas fa-info-circle"></i> 
                <strong>Disclaimer:</strong> This prediction is for educational purposes only and should not replace professional medical advice. 
                Always consult with qualified healthcare professionals.
            </div>
        </div>
    `;

    resultBox.innerHTML = resultHTML;
    resultContainer.style.display = 'block';

    // Scroll to results
    resultContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/**
 * Display error message
 */
function displayError(message) {
    const resultContainer = document.getElementById('resultContainer');
    const resultBox = document.getElementById('resultBox');

    resultBox.innerHTML = `
        <div class="error-message">
            <i class="fas fa-exclamation-circle"></i> 
            <strong>Error:</strong> ${message}
        </div>
    `;

    resultContainer.style.display = 'block';
    resultContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/**
 * Show loading spinner
 */
function showLoadingSpinner() {
    document.getElementById('loadingSpinner').style.display = 'flex';
}

/**
 * Hide loading spinner
 */
function hideLoadingSpinner() {
    document.getElementById('loadingSpinner').style.display = 'none';
}

/**
 * Scroll to prediction form
 */
function scrollToForm() {
    document.getElementById('predictionForm').scrollIntoView({ behavior: 'smooth' });
    document.getElementById('predictionForm').reset();
}

/**
 * Print result
 */
function printResult() {
    window.print();
}

/**
 * Setup smooth navigation
 */
function setupNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
        });
    });

    // Update active link on scroll
    window.addEventListener('scroll', function() {
        let current = '';
        
        const sections = document.querySelectorAll('section');
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').slice(1) === current) {
                link.classList.add('active');
            }
        });
    });
}

/**
 * Format number with 2 decimal places
 */
function formatNumber(num) {
    return parseFloat(num).toFixed(2);
}

/**
 * Get patient risk level
 */
function getRiskLevel(probability) {
    if (probability < 30) return 'Low Risk';
    if (probability < 60) return 'Moderate Risk';
    return 'High Risk';
}
