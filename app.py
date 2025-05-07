import streamlit as st
from transformers import pipeline

# Load the sentiment analysis model (public one)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

sentiment_pipeline = load_model()

# Streamlit UI
st.title("💬 Comment Sentiment Rater")
st.write("Enter a comment to get a sentiment rating using a BERT model.")

user_input = st.text_area("Type your comment here")

if st.button("Analyze"):
    if user_input.strip():
        result = sentiment_pipeline(user_input)[0]
        label = result['label']
        score = result['score']
        
        # Extract star rating from label
        stars = int(label.split()[0])
        st.markdown(f"**⭐ Rating:** {stars} out of 5")
        st.markdown(f"**🧠 Confidence:** `{score:.2f}`")
    else:
        st.warning("Please enter a comment to analyze.")
