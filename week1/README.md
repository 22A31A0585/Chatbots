# Emotion-Aware Chatbot 🤖

A simple chatbot built with Python, NLTK, and Streamlit that analyzes emotions from text input.

## Features
- Tokenizes user input into words using ToktokTokenizer.
- Removes stopwords and punctuation to clean the text.
- Lemmatizes words using WordNetLemmatizer (e.g., “missed” → “miss”).
- Performs sentiment analysis with NLTK’s SentimentIntensityAnalyzer.
- Categorizes emotions as:
  - Positive → Happy response
  - Negative → Empathetic response
  - Neutral → Acknowledgment
- Simple UI built with Streamlit to input messages and view bot responses in real-time.
- ## Example Usage
| Input Text | Expected Bot Response | Sentiment |
|------------|---------------------|-----------|
| "I love my job and everything is going great!" | Yay! That’s awesome 😄 | Positive |
| "I am so tired and stressed out today." | Oh no! I hope things get better 😔 | Negative |
| "I went to the store to buy some milk." | Okay, got it 👍 | Neutral |

You can test more sentences in the Streamlit app and see the bot's sentiment analysis in real-time.


Pros (Why people would like it) 
Easy to use: Simple Streamlit interface, no complex setup.
Real-time sentiment analysis: Instantly shows emotions from text input.
Lightweight: Uses only Python and NLTK; no heavy AI models.
Educational: Great for learning text preprocessing, tokenization, lemmatization, and sentiment analysis.
Customizable: Developers can easily expand it with more emotions or responses.
Cons (Limitations / Negative points) ❌

Basic responses: Bot only replies with generic happy, sad, or neutral messages.
Limited understanding: Can’t handle sarcasm, slang, or complex emotions accurately.
No memory: Bot doesn’t remember previous conversations.
UI is simple: Minimal design; not very visually appealing for production use.
Language limitation: Works best with English text; other languages may not be analyzed correctly.
## Live Demo
https://chatbots-emotion-bot.streamlit.app/
