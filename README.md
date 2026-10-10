 BillBuddy – AI-Powered Bill Tracker & Splitter

* Project Overview

BillBuddy is an AI-powered web application that helps users easily understand and split their bills. Users enter their name and email, upload a bill image, and BillBuddy uses Google Gemini AI to extract the bill details such as items, quantity, price, GST, subtotal, and total amount.

The user can then choose between equal splitting or custom splitting. After the split is calculated, the complete bill summary can be sent to the user's email.

---


* Objectives

- To automatically extract bill information from an image using AI.
- To reduce manual calculation of bills.
- To provide easy equal and custom bill splitting.
- To send the final bill and split summary to the user's email.
- To provide a simple and user-friendly bill management system.

---


* System Workflow

User enters Name & Email
          ↓
    Upload Bill Image
          ↓
   Google Gemini AI
          ↓
   Extract Bill Details
          ↓
 Display Items, Quantity,
 Price, GST & Total
          ↓
   Choose Split Method
          ↓
 Equal Split / Custom Split
          ↓
 Calculate Amount to Pay
          ↓
 Send Bill Summary to Email

---


* How BillBuddy Works

1. The user enters their name and email ID.
2. The user uploads a bill image.
3. Google Gemini AI analyzes the image and extracts the bill information.
4. BillBuddy displays the extracted items, quantity, price, GST, subtotal, and total.
5. The user selects Equal Split or Custom Split.
6. BillBuddy calculates how much each person should pay.
7. The final bill and split details are sent to the user's email ID.

---



* Project Information

Component| Technology
Frontend| Streamlit
Backend| Python
AI / Bill Recognition| Google Gemini Vision AI
Image Processing| Pillow (PIL)
Data Format| JSON
Email Service| SMTP / Gmail
Version Control| Git & GitHub
Deployment| Streamlit Community Cloud

---


* Main Files

BillBuddy/
│
├── streamlit_app.py    # Main application
├── prompts.py          # Gemini bill-reading prompt
├── requirements.txt    # Required Python libraries
├── README.md           # Project documentation
└── .streamlit/
    └── secrets.toml    # API keys and email credentials

---


* Key Features

-  AI-based bill recognition
-  Bill image upload
-  Automatic bill detail extraction
-  Equal bill splitting
-  Custom bill splitting
-  Email bill summary
-  Cloud deployment

---


* Future Scope

BillBuddy can be extended with bill history, expense tracking, item-wise splitting, spending analytics, PDF reports, mobile application support, and online payment integration.

---


* Project

Project Name: BillBuddy
Domain: Artificial Intelligence & Expense Management
Application Type: AI-Powered Web Application
