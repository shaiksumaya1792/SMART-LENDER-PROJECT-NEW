#  SMART LENDER - Loan Approval Prediction System

A Machine Learning-based web application that predicts whether a loan application is likely to be approved based on the applicant's financial and personal details. This project helps automate the loan approval process, making it faster, more accurate, and consistent.

---

##  Table of Contents

- About the Project
- Features
- Technologies Used
- Project Structure
- Installation
- Usage
- Machine Learning Workflow
- Screenshots
- Live Demo
- GitHub Repository
- Future Enhancements
- Contributors
- License

---

##  About the Project

Loan approval is one of the most important tasks in the banking sector. Manual verification of loan applications is time-consuming and may lead to errors.

The SMART LENDER application uses a trained Machine Learning model to analyze applicant information such as:

- Gender
- Marital Status
- Education
- Employment Status
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

Based on these details, the application predicts whether the loan should be **Approved** or **Rejected**.

---

##  Features

- User-friendly web interface
- Instant loan approval prediction
- Machine Learning-based decision making
- Responsive design
- Fast prediction results
- Easy deployment using Render
- Simple and clean UI

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Pickle

### Deployment
- Render

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
SMART-LENDER-PROJECT-NEW
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── model.pkl
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/shaiksumaya1792/SMART-LENDER-PROJECT-NEW.git
```

### Go to the project folder

```bash
cd SMART-LENDER-PROJECT-NEW
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🚀 Usage

1. Open the application.
2. Enter the applicant details.
3. Click on **Predict**.
4. The system analyzes the information.
5. The prediction result (Approved/Rejected) is displayed.

---

## 🤖 Machine Learning Workflow

- Data Collection
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Model Saving using Pickle
- Flask Integration
- Web Deployment

---

## 📊 Input Parameters

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

## 📈 Output

The application predicts:

✅ Loan Approved

or

❌ Loan Rejected

---

## 🌐 Live Demo

https://smart-lender-116.onrender.com

---

## 💻 GitHub Repository

https://github.com/shaiksumaya1792/SMART-LENDER-PROJECT-NEW

---

## 🔮 Future Enhancements

- User Authentication
- Loan Eligibility Score
- Admin Dashboard
- Database Integration
- PDF Report Generation
- Email Notifications
- Cloud Deployment with CI/CD
- Model Performance Dashboard

---

## 🤝 Contributors

**Shaik Sumaya**

---

## 📄 License

This project is developed for educational and academic purposes.

---







