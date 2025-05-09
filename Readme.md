
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

## Training images

*NLU training:-
![Screenshot 2025-04-04 165417](https://github.com/user-attachments/assets/854c86ca-71f1-4c9f-ac35-f80bc7524740)

*Dialog training:-
![Screenshot 2025-04-04 170643](https://github.com/user-attachments/assets/64c3b786-af11-4b35-b377-3b8a54bbc8fc)

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

## 📈 Future Enhancements

* Integrate real-time banking APIs
* Add multilingual support
* Use transformer-based models like BERT
* Cloud deployment (e.g., AWS/GCP)

## 👥 Project Members

* **Venkata Taraka Nadh Nanduri** – 21KP1A6153
* **Kothuri Leela Siva Sai** – 21KP1A6132
* **Chinthabathini Vijay Kumar** – 21KP1A6107

**Guide:** D. Thirupathamma, M.Tech (Assistant Professor, Dept. of CSE)
