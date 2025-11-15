"""
Test script for Heart Disease Prediction Application
Verifies that the application is working correctly before deployment
"""

import os
import sys
import json
import pickle
from pathlib import Path

def test_project_structure():
    """Test if all required files exist"""
    print("=" * 60)
    print("Testing Project Structure...")
    print("=" * 60)
    
    required_files = [
        'app.py',
        'train_model.py',
        'config.py',
        'requirements.txt',
        'README.md',
        'QUICKSTART.md',
        'DEPLOYMENT.md',
        'Dockerfile',
        'Procfile',
        'runtime.txt',
        '.gitignore',
        '.env.example',
        'templates/index.html',
        'static/style.css',
        'static/script.js'
    ]
    
    all_exist = True
    for file in required_files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        print(f"{status} {file}")
        if not exists:
            all_exist = False
    
    print("\nResult: " + ("PASSED" if all_exist else "FAILED"))
    return all_exist


def test_dependencies():
    """Test if all required dependencies are installed"""
    print("\n" + "=" * 60)
    print("Testing Dependencies...")
    print("=" * 60)
    
    dependencies = [
        'flask',
        'pandas',
        'numpy',
        'sklearn',
        'werkzeug'
    ]
    
    all_installed = True
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✓ {dep} - OK")
        except ImportError:
            print(f"✗ {dep} - NOT INSTALLED")
            all_installed = False
    
    print("\nResult: " + ("PASSED" if all_installed else "FAILED"))
    print("\nTo install missing dependencies, run:")
    print("pip install -r requirements.txt")
    return all_installed


def test_app_import():
    """Test if Flask app can be imported"""
    print("\n" + "=" * 60)
    print("Testing Flask App Import...")
    print("=" * 60)
    
    try:
        from app import app
        print("✓ Flask app imported successfully")
        print("✓ App name:", app.name)
        return True
    except Exception as e:
        print(f"✗ Error importing app: {e}")
        return False


def test_model_files():
    """Test if trained model files exist"""
    print("\n" + "=" * 60)
    print("Testing Model Files...")
    print("=" * 60)
    
    model_files = [
        'models/heart_disease_model.pkl',
        'models/scaler.pkl',
        'models/feature_names.pkl'
    ]
    
    all_exist = True
    for file in model_files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        print(f"{status} {file}")
        if not exists:
            all_exist = False
    
    if not all_exist:
        print("\nModel files not found!")
        print("Run: python train_model.py")
    
    print("\nResult: " + ("PASSED" if all_exist else "NEEDS TRAINING"))
    return all_exist


def test_model_prediction():
    """Test if model can make predictions"""
    print("\n" + "=" * 60)
    print("Testing Model Prediction...")
    print("=" * 60)
    
    try:
        model = pickle.load(open('models/heart_disease_model.pkl', 'rb'))
        scaler = pickle.load(open('models/scaler.pkl', 'rb'))
        
        # Test data
        test_input = [[45, 1, 1, 130, 200, 0, 1, 150, 0, 1.5, 1, 0, 2]]
        
        scaled = scaler.transform(test_input)
        prediction = model.predict(scaled)
        probability = model.predict_proba(scaled)
        
        print(f"✓ Test Input: {test_input[0]}")
        print(f"✓ Prediction: {prediction[0]}")
        print(f"✓ Probability: {probability[0]}")
        print(f"✓ Model is working correctly!")
        
        return True
    except Exception as e:
        print(f"✗ Error testing model: {e}")
        return False


def test_html_structure():
    """Test if HTML file is properly structured"""
    print("\n" + "=" * 60)
    print("Testing HTML Structure...")
    print("=" * 60)
    
    try:
        # Read HTML as UTF-8 to support unicode characters
        with open('templates/index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            
        checks = {
            'DOCTYPE': '<!DOCTYPE html>' in content,
            'Flask Templates': '{{ url_for' in content,
            'Form': '<form' in content,
            'Prediction Section': 'predictionForm' in content,
            'Footer': '<footer' in content
        }
        
        all_ok = True
        for check, result in checks.items():
            status = "✓" if result else "✗"
            print(f"{status} {check}")
            if not result:
                all_ok = False
        
        print("\nResult: " + ("PASSED" if all_ok else "FAILED"))
        return all_ok
    except Exception as e:
        print(f"✗ Error reading HTML: {e}")
        return False


def test_css_file():
    """Test if CSS file exists and is valid"""
    print("\n" + "=" * 60)
    print("Testing CSS File...")
    print("=" * 60)
    
    try:
        # Read CSS as UTF-8
        with open('static/style.css', 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = {
            'Root variables': '--primary-color' in content,
            'Navbar styles': '.navbar' in content,
            'Hero section': '.hero' in content,
            'Form styles': '.form-' in content,
            'Responsive design': '@media' in content
        }
        
        all_ok = True
        for check, result in checks.items():
            status = "✓" if result else "✗"
            print(f"{status} {check}")
            if not result:
                all_ok = False
        
        print("\nResult: " + ("PASSED" if all_ok else "FAILED"))
        return all_ok
    except Exception as e:
        print(f"✗ Error reading CSS: {e}")
        return False


def test_javascript_file():
    """Test if JavaScript file exists and is valid"""
    print("\n" + "=" * 60)
    print("Testing JavaScript File...")
    print("=" * 60)
    
    try:
        # Read JS as UTF-8 to support emoji and unicode
        with open('static/script.js', 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = {
            'Form submission': 'handleFormSubmit' in content,
            'Validation': 'validateFormData' in content,
            'Result display': 'displayResult' in content,
            'Error handling': 'displayError' in content,
            'API call': 'fetch' in content
        }
        
        all_ok = True
        for check, result in checks.items():
            status = "✓" if result else "✗"
            print(f"{status} {check}")
            if not result:
                all_ok = False
        
        print("\nResult: " + ("PASSED" if all_ok else "FAILED"))
        return all_ok
    except Exception as e:
        print(f"✗ Error reading JavaScript: {e}")
        return False


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  Heart Disease Prediction - Project Test Suite".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    
    results = {}
    
    # Run tests
    results['Structure'] = test_project_structure()
    results['Dependencies'] = test_dependencies()
    results['App Import'] = test_app_import()
    results['Model Files'] = test_model_files()
    
    if results['Model Files']:
        results['Model Prediction'] = test_model_prediction()
    
    results['HTML'] = test_html_structure()
    results['CSS'] = test_css_file()
    results['JavaScript'] = test_javascript_file()
    
    # Print summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY".center(60))
    print("=" * 60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test, result in results.items():
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status}: {test}")
    
    print("=" * 60)
    print(f"Total: {passed}/{total} tests passed")
    print("=" * 60)
    
    if passed == total:
        print("\n✓ All tests PASSED! Application is ready to run.")
        print("\nNext steps:")
        print("1. If you haven't trained the model, run: python train_model.py")
        print("2. Start the application: python app.py")
        print("3. Open browser: http://localhost:5000")
        return 0
    else:
        print("\n✗ Some tests FAILED. Please fix the issues above.")
        if not results['Dependencies']:
            print("   Run: pip install -r requirements.txt")
        if not results['Model Files']:
            print("   Run: python train_model.py")
        return 1


if __name__ == '__main__':
    sys.exit(main())
