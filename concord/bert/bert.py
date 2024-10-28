# bert.py

import os

import joblib
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer


def initialize_model():
    """
    Initialize the BERTopic model.
    You can customize the model with different parameters as needed.
    """
    # Using a specific embedding model for better performance
    embedding_model = SentenceTransformer("all-mpnet-base-v2")

    topic_model = BERTopic(
        embedding_model=embedding_model,
        verbose=True,
        # You can add more parameters here
    )
    return topic_model


def save_model(model, path):
    """
    Save the BERTopic model to disk.
    """
    joblib.dump(model, path)
    print(f"Model saved to {path}")


def load_model(path):
    """
    Load the BERTopic model from disk.
    """
    if os.path.exists(path):
        model = joblib.load(path)
        print(f"Model loaded from {path}")
        return model
    else:
        print(f"No existing model found at {path}. Initializing a new model.")
        return None
