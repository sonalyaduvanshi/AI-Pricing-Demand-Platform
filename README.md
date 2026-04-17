# AI-Powered Pricing & Demand Intelligence Platform with QA Testing

# Overview

An end-to-end data science project enhanced with comprehensive software testing. The system analyzes sales data, predicts demand using machine learning, and is rigorously tested across UI, API, and model layers.


# Objective

To ensure the reliability, accuracy, and robustness of an AI-based pricing and demand prediction system through structured QA practices.

# Testing Scope

# 1. UI Testing (Flask Web App)

- Validated input fields (price, product, region)
- Tested invalid, empty, and boundary inputs
- Verified correct display of predictions



# 2. API Testing

Performed API validation using Postman

- Tested prediction endpoints (GET/POST)
- Validated status codes (200, 400, 500)
- Verified JSON response structure



# 3. Machine Learning Model Testing (🔥 Unique)

- Tested model with edge cases (very high/low values)
- Checked consistency of predictions
- Validated handling of invalid inputs



# 4. Data Validation Testing

- Checked dataset for missing values and duplicates
- Verified preprocessing steps



# 5. Functional Testing

- End-to-end validation (UI → API → Model output)


# Sample Bugs Identified

- Model produced unrealistic predictions for extreme values
- API failed on null input
- UI did not validate negative pricing input

# Tools Used

- Python (Pandas, NumPy, Scikit-learn)
- Flask
-  Postman
-   GitHub

# Key Outcome

- Ensured system reliability through multi-layer testing
- Improved model robustness by identifying edge-case failures
- Delivered a production-ready AI system with QA validation



# Conclusion

This project demonstrates strong QA capabilities applied to modern AI systems, including API, UI, and ML validation.
