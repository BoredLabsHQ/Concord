# bert.py

from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired
from sentence_transformers import SentenceTransformer


def initialize_model():
    """
    Initialize the BERTopic model with a specified embedding model and KeyBERTInspired representation.
    """
    # Use a pre-trained SentenceTransformer model for embeddings
    embedding_model = SentenceTransformer("all-mpnet-base-v2")

    # Initialize KeyBERTInspired representation model
    representation_model = KeyBERTInspired()

    topic_model = BERTopic(
        embedding_model=embedding_model,
        verbose=True,
        representation_model=representation_model,
        min_topic_size=2,  # Adjusted to allow smaller topics
        n_gram_range=(1, 2)  # Consider unigrams and bigrams
    )
    return topic_model
