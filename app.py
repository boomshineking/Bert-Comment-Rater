import streamlit as st
from transformers import pipeline

# Load the sentiment analysis model (public one)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

sentiment_pipeline = load_model()

# Streamlit UI
st.title("💬 Comment Sentiment Classifier")
st.write("Enter a comment to see the star rating and whether it's Positive, Neutral, or Negative using a BERT model.")

user_input = st.text_area("Type your comment here")

if st.button("Analyze"):
    if user_input.strip():
        result = sentiment_pipeline(user_input)[0]
        label = result['label']
        score = result['score']
        
        # Extract star rating from label
        stars = int(label.split()[0])
        
        # Convert stars to sentiment
        if stars <= 2:
            sentiment = "Your comment is 👎Negative"
        elif stars == 3:
            sentiment = "Your comment is 😐Neutral"
        else:
            sentiment = "Your comment is Positive👍"
        
        # Display both star rating and sentiment
        st.markdown(f"**⭐ Star Rating:** {stars} out of 5")
        st.markdown(f"**📝 Sentiment:** {sentiment}")
        st.markdown(f"**🧠 Confidence:** `{score:.2f}`")
    else:
        st.warning("Please enter a comment to analyze.")
