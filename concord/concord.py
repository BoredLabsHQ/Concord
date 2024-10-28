# concord.py

from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups

from bert.bert import load_model, save_model

# Configuration
MODEL_SAVE_PATH = "bertopic_model.pkl"
INITIAL_BATCH_SIZE = 100  # Number of documents in the initial batch
BATCH_SIZE = 50  # Number of documents per new batch
TOTAL_BATCHES = 10  # Total number of batches to simulate


def load_data(batch_number, batch_size):
    """
    Simulate loading a batch of data.
    For demonstration, we're using the 20 Newsgroups dataset.
    In a real-world scenario, replace this with your data loading mechanism.
    """
    newsgroups = fetch_20newsgroups(subset="all",
                                    remove=("headers", "footers", "quotes"))
    start = batch_number * batch_size
    end = start + batch_size
    if start >= len(newsgroups.data):
        return []
    return newsgroups.data[start:end]


def setup():
    # Load existing model or initialize a new one
    topic_model = load_model(MODEL_SAVE_PATH)

    # Initialize data storage
    all_documents = []

    if topic_model is None:
        # Initial batch
        print("Processing initial batch...")
        initial_batch = load_data(batch_number=0,
                                  batch_size=INITIAL_BATCH_SIZE)
        all_documents.extend(initial_batch)

        # Fit the model with the initial batch
        topic_model = BERTopic()
        topics, probs = topic_model.fit_transform(all_documents)

        # Save the model
        save_model(topic_model, MODEL_SAVE_PATH)
    else:
        # If model exists, load existing documents if stored
        # For simplicity, we're not storing all_documents. In a real application, consider storing them.
        print("Existing model loaded. Starting incremental updates...")
        # Optionally, load existing documents from a file or database
        # all_documents = load_existing_documents()

    # Simulate incremental updates with new batches
    for batch_num in range(1, TOTAL_BATCHES + 1):
        print(f"\nProcessing batch {batch_num}...")
        new_batch = load_data(batch_number=batch_num, batch_size=BATCH_SIZE)

        if not new_batch:
            print("No more data to process.")
            break

        all_documents.extend(new_batch)

        # Refit the model with all documents (existing + new)
        print("Refitting the BERTopic model with the updated dataset...")
        topic_model = BERTopic()
        topics, probs = topic_model.fit_transform(all_documents)

        # Optionally, analyze topics
        print(
            f"Number of topics after batch {batch_num}: {len(set(topics)) - (1 if -1 in topics else 0)}"
        )

        # Save the updated model
        save_model(topic_model, MODEL_SAVE_PATH)

        # Optional: Integrate with Neo4j to store/update topics
        # store_topics_in_neo4j(topic_model, batch_num)

    print("\nTopic modeling completed.")
