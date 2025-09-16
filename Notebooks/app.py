import streamlit as st
import joblib

# Load the saved vectorizer and model
try:
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('svm_model.pkl')
except FileNotFoundError:
    st.error("Model files not found. Please train and save the model first.")
    st.stop()

# App title
st.title("Spam Message Classifier")

# Input text area
user_input = st.text_area("Enter a message to classify:")

# Classify button
if st.button("Classify"):
    if user_input:
        # 1. Transform the user input
        message_tfidf = vectorizer.transform([user_input])

        # 2. Predict using the loaded model
        prediction = model.predict(message_tfidf)

        # 3. Display the result
        if prediction[0] == 1:
            st.error("This is a Spam message.")
        else:
            st.success("This is a Ham message.")
    else:
        st.warning("Please enter a message.")