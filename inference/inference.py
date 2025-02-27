import re
import nltk
import joblib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure required NLTK data is available
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Preprocessing function (same as used in training)
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-z\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # Rejoin tokens into a single string
    return " ".join(tokens)

# Load the saved TF-IDF vectorizer and SVM model
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")
svm_model = joblib.load("svm_model.pkl")

# Inference function to predict category
def predict_category(input_text):
    # Preprocess the input text
    processed_text = preprocess_text(input_text)
    # Transform the text using the loaded TF-IDF vectorizer
    tfidf_features = tfidf_vectorizer.transform([processed_text])
    # Predict category using the loaded SVM model
    prediction = svm_model.predict(tfidf_features)
    return prediction[0]

# Example usage:
if __name__ == "__main__":
    input_text = "Lewis Capaldi recently released a new song that is taking the charts by storm."
    predicted_category = predict_category(input_text)
    print("Predicted category:", predicted_category)
