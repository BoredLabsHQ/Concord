import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from typing import Any, List


def extract_text_segments(data: Any) -> List[str]:
    texts = []

    def extract_text(value):
        if isinstance(value, dict):
            for k, v in value.items():
                extract_text(v)
        elif isinstance(value, list):
            for item in value:
                extract_text(item)
        elif isinstance(value, str):
            texts.append(value)

    extract_text(data)
    return texts


def preprocess_documents(documents):
    """
    Preprocess the documents by:
    - Lowercasing
    - Removing punctuation
    - Removing stop words
    - Lemmatizing
    """
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    processed_docs = []

    for doc in documents:
        # Lowercase
        doc = doc.lower()
        # Tokenize
        tokens = nltk.word_tokenize(doc)
        # Remove punctuation and non-alphabetic tokens
        tokens = [word for word in tokens if word.isalpha()]
        # Remove stop words and short words
        tokens = [
            word for word in tokens if word not in stop_words and len(word) > 2
        ]
        # Lemmatize
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        # Rejoin tokens to form the cleaned document
        processed_doc = ' '.join(tokens)
        processed_docs.append(processed_doc)

    return processed_docs
