# 💬 BERT Comment Sentiment Rater

This is a lightweight Streamlit web app that uses a pre-trained BERT model to analyze the sentiment of user-entered comments and return a star rating (1 to 5). It's multilingual and powered by the `nlptown/bert-base-multilingual-uncased-sentiment` model via Hugging Face's Transformers library. the application is deployed on Streamlit Community 

🔗 **Live Demo:** [Click here to try the app](https://bert-comment-rater-dgijhprgp75rvoqutpsxsw.streamlit.app/)

---

## 🚀 Features

- Multilingual support using BERT
- Simple UI built with Streamlit
- Star-based sentiment score (1 to 5)
- Confidence score display

---

## 🧠 Model Used

- **Model:** [`nlptown/bert-base-multilingual-uncased-sentiment`](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
- **Task:** Sentiment Analysis
- **Languages Supported:** Multiple (English, French, German, etc.)

---

## 🖥️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/bert-comment-sentiment-rater.git
cd bert-comment-sentiment-rater
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📝 Example

**Input:**  
`"This product is amazing and exceeded my expectations!"`

**Output:**  
⭐ Rating: 5 out of 5  
🧠 Confidence: `0.98`
![image](https://github.com/user-attachments/assets/b6bb8285-f5ee-4de8-a969-64b7a180f456)


---

## 📂 File Structure

```
bert-comment-sentiment-rater/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # List of dependencies
└── README.md             # This file
```

---

## 🤝 Acknowledgements

- Hugging Face Transformers 🤗
- Streamlit for rapid UI development
- `nlptown` for the multilingual sentiment BERT model

---

## 📃 License

This project is licensed under the MIT License.
