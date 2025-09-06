import streamlit as st
from nltk.tokenize import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
import string
import nltk

# Download NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# Initialize NLP tools
tokenizer = ToktokTokenizer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
sia = SentimentIntensityAnalyzer()

# Function to process text
def get_bot_response(user_text):
    words = tokenizer.tokenize(user_text)
    filtered_words = [w for w in words if w.lower() not in stop_words]
    final_words = [w for w in filtered_words if w not in string.punctuation]
    lemmatized_words = [lemmatizer.lemmatize(w, pos='v') for w in final_words]
    clean_text = " ".join(lemmatized_words)
    
    sentiment = sia.polarity_scores(clean_text)
    compound = sentiment['compound']
    
    if compound >= 0.05:
        response = "Yay! That’s awesome 😄"
        color = "green"
    elif compound <= -0.05:
        response = "Oh no! I hope things get better 😔"
        color = "red"
    else:
        response = "Okay, got it 👍"
        color = "orange"
    
    return response, sentiment, color

# Streamlit UI
st.set_page_config(page_title="Week 1 Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Week 1: Emotion-Aware Chatbot")
st.markdown("Type something in the box below, and the bot will respond based on your emotions!")

# User input
user_input = st.text_input("Your message:")

if user_input:
    response, sentiment, color = get_bot_response(user_input)
    
    # Show bot response with color
    st.markdown(f"**Bot Response:** <span style='color:{color}; font-weight:bold;'>{response}</span>", unsafe_allow_html=True)
    
    # Show sentiment scores in a box
    st.markdown("**Sentiment Scores:**")
    st.json(sentiment)
