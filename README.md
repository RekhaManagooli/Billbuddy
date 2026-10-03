# 🧾 BillBuddy – Bill Tracker & Splitter

##  Project Overview

BillBuddy is a web-based bill tracking and splitting application developed using Python and Streamlit.

The application allows users to upload a bill image, automatically read the bill details using AI, display the extracted information, and split the total bill among multiple people.

It supports both:

- Equal bill splitting
- Custom bill splitting

BillBuddy is designed to make bill sharing faster, easier, and more convenient.

---

##  Objectives

The main objectives of BillBuddy are:

- To extract bill information automatically from an uploaded image.
- To reduce manual entry of bill details.
- To display items, quantity, price, GST, subtotal, and total amount.
- To calculate the amount each person should pay.
- To support equal and custom bill splitting.
- To provide an option to send the bill split information through WhatsApp using Twilio.

---

##  How BillBuddy Works

The application works in the following steps:

### 1. Upload Bill

The user uploads a bill image in JPG, JPEG, or PNG format.

### 2. AI Bill Recognition

The uploaded image is processed using Google's Gemini AI model.

The AI reads the bill and extracts information such as:

- Item name
- Quantity
- Price
- GST
- Subtotal
- Total bill amount

### 3. Display Bill Details

The extracted information is displayed in a table so that the user can easily check the bill details.

### 4. Select Split Method

The user can choose between:

**Equal Split**

The total bill is divided equally among the selected number of people.

**Custom Split**

The user can enter a different amount for each person.

The application checks whether the entered custom amounts match the total bill.

### 5. WhatsApp

BillBuddy also includes Twilio WhatsApp integration.

The application can send the bill information through WhatsApp using the configured Twilio service.

---

##  System Workflow

```text
User
  ↓
Upload Bill Image
  ↓
Streamlit Application
  ↓
Gemini AI
  ↓
Extract Bill Information
  ↓
Display Bill Details
  ↓
Choose Split Method
  ↓
Equal Split / Custom Split
  ↓
WhatsApp Integration using Twilio