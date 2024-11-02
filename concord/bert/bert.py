# bert.py

from bertopic import BERTopic
from sentence_transformers import SentenceTransformer


def initialize_model():
    """
    Initialize the BERTopic model with a specified embedding model and custom parameters.
    """
    # Use a pre-trained SentenceTransformer model for embeddings
    embedding_model = SentenceTransformer("all-mpnet-base-v2")

    topic_model = BERTopic(
        embedding_model=embedding_model,
        verbose=True,
        min_topic_size=3,  # Adjusted to allow smaller topics
        n_gram_range=(1, 2)  # Consider unigrams and bigrams
    )
    return topic_model
