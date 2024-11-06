# model_manager.py
from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired
from sentence_transformers import SentenceTransformer


class ModelManager:
    _model = None

    @classmethod
    def initialize_model(cls):
        """
        Initialize the BERTopic model with a specified embedding model and KeyBERTInspired representation.
        """
        # Use a pre-trained SentenceTransformer model for embeddings
        embedding_model = SentenceTransformer("all-mpnet-base-v2")

        # Initialize KeyBERTInspired representation model
        representation_model = KeyBERTInspired()

        cls._model = BERTopic(
            embedding_model=embedding_model,
            verbose=True,
            representation_model=representation_model,
            min_topic_size=2,  # Adjusted to allow smaller topics
            n_gram_range=(1, 2)  # Consider unigrams and bigrams
        )
        print("BERTopic model initialized and ready for usage.")

    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls.initialize_model()  # Initialize only once
        return cls._model
