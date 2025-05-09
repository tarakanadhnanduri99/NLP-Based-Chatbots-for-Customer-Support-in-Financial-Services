
# NLP-Based Chatbot for Customer Support in Financial Services

## 📌 Project Overview

**VITAL-D Chat** (Virtual Intelligent Transactional Assistant for Logistics & Dialogue) is an intelligent virtual assistant designed to provide conversational financial assistance to users. It enables users to track expenses, receive financial insights, and manage personal finances through a natural language interface. The system leverages **Natural Language Processing (NLP)** and **machine learning models** with **GloVe word embeddings** for accurate intent recognition and response generation.

## 🎯 Objectives

* To build a chatbot that offers automated financial assistance using NLP.
* To help users track expenses, view analytics, and manage spending via natural conversation.
* To ensure secure, personalized, and intelligent interaction with financial data.

## 🔧 Technologies Used

| Component            | Technology                      |
| -------------------- | ------------------------------- |
| Programming Language | Python                          |
| Web Framework        | Django                          |
| Frontend             | HTML, CSS, JavaScript (AJAX)    |
| Database             | SQLite                          |
| NLP Embeddings       | GloVe (100-dimensional vectors) |
| ML Libraries         | TensorFlow, Keras               |
| Visualization        | Chart.js                        |

## 🧠 System Modules

1. **User Interface**

   * Registration, login, chatbot interaction, and graphical analytics.

2. **NLP Engine**

   * Uses GloVe embeddings to convert text to vectors.
   * Processes intent and context using LSTM-based models.

3. **Intent Classification**

   * Classifies user queries into intents like balance check, spending, savings, etc.

4. **Dialogue Manager**

   * Uses sequence modeling to maintain conversation flow.

5. **Database Management**

   * Stores user credentials, expense details, and transaction history securely.

## 🏗️ System Architecture

```mermaid
graph TD
  A[User Query] --> B[NLP Engine]
  B --> C[Intent Detection (LSTM + GloVe)]
  C --> D[Response Generator]
  D --> E[Frontend Interface]
  C --> F[Database (SQLite)]
```

## ✅ Features

* Natural language expense tracking
* Categorical expense classification (food, transport, healthcare, etc.)
* Visual analytics (Pie Chart)
* Secure user authentication
* Speech-to-text support
* GloVe-based semantic understanding

## 📊 Model Accuracy

| Model             | Accuracy |
| ----------------- | -------- |
| Intent Classifier | 97.59%   |
| Dialogue Model    | 93.33%   |

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/vital-d-chatbot.git
cd vital-d-chatbot

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Download GloVe embeddings
python download_glove.py

# Run the server
python manage.py runserver
```

## 🖥️ Output Screenshots

Below are a few screenshots showcasing the key features and functionality of the **VITAL-D Chatbot** web application:

### 🔐 1. User Registration & Login

Users can register with basic information like name, income, and account balance. Registered users can securely log in using Django's built-in authentication system.

![image](https://github.com/user-attachments/assets/26238dcb-6bc0-484c-ba54-a761fc063f94)

*User registration form for account setup.*

![image](https://github.com/user-attachments/assets/9171265a-3855-4eda-ac34-4e13c089fe6c)

*Login page with secure access.*

---

### 💬 2. Chatbot Interface

The chatbot accepts user queries in both **text and speech** formats. It responds with intelligent financial insights based on user inputs, such as expenses, balances, and suggestions on affordability.

![image](https://github.com/user-attachments/assets/6869bc99-1cf2-4483-a3df-7c9e4b55192c)

*Conversational UI with GloVe-powered NLP backend.*

---

### 📊 3. Expense Analysis Dashboard

The application provides a **pie chart** to visually represent user spending across categories (e.g., Food, Transport, Healthcare).

![image](https://github.com/user-attachments/assets/12fd51f5-080d-44b0-97da-9c003659b780)

*Graphical breakdown of categorized expenditures.*

---

### 🧠 4. Training Logs (Optional)

Console logs during model training using GloVe embeddings and LSTM-based neural networks for **intent classification** and **dialogue flow prediction**.

*NLU training:-
![Screenshot 2025-04-04 165417](https://github.com/user-attachments/assets/f7a559b3-7b14-46d6-93f0-eadb17fcb096)

![Screenshot 2025-04-04 165542](https://github.com/user-attachments/assets/da4cc594-2e0e-46bb-829a-cd3bd7488b1b)

![Screenshot 2025-04-04 165417](https://github.com/user-attachments/assets/854c86ca-71f1-4c9f-ac35-f80bc7524740)

*Snapshot of encoded utterances during intent model training.*

*Dialog training:-
![Screenshot 2025-04-04 170643](https://github.com/user-attachments/assets/64c3b786-af11-4b35-b377-3b8a54bbc8fc)

![Screenshot 2025-04-04 170735](https://github.com/user-attachments/assets/6c84b102-90dd-42e6-aae1-6b299d813b6b)
*Log from dialog model training process.*

## 📈 Future Enhancements

* Integrate real-time banking APIs
* Add multilingual support
* Use transformer-based models like BERT
* Cloud deployment (e.g., AWS/GCP)

## 👥 Team

* **Venkata Taraka Nadh Nanduri** – 21KP1A6153

**Guide:** D. Thirupathamma, M.Tech (Assistant Professor, Dept. of CSE)
