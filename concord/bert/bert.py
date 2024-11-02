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
        min_topic_size=2,  # Allow smaller topic clusters
        n_gram_range=(1, 2),  # Include bigrams - changed from (1, 3) to (1, 2)
        # calculate_probabilities=True,
        # umap_model=UMAP(n_neighbors=5,
        #                 n_components=5,
        #                 min_dist=0.05,
        #                 metric='cosine'),  # Tighter clusters
        # hdbscan_model=HDBSCAN(
        #     min_cluster_size=3,
        #     prediction_data=True)  # Smaller clusters in HDBSCAN
    )
    return topic_model


def fit_and_evaluate_model(documents):
    topic_model = initialize_model()
    topics, probs = topic_model.fit_transform(documents)

    # Generate topic info
    topic_info_df = topic_model.get_topic_info()
    # print("\nMain Topics and Their Sizes:")
    # print(topic_info_df[['Topic', 'Count', 'Name']])

    # Document-topic distribution
    document_info = topic_model.get_document_info(documents)
    document_distribution_df = document_info[['Document', 'Topic', 'Name']]
    # print("\nDocument-Topic Distribution:")
    # print(document_distribution_df)

    return topics, probs, topic_info_df, document_distribution_df, topic_model
