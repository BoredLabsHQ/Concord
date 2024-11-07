# concord.py

from bert.pre_process import preprocess_documents


def concord(topic_model, documents):
    # Load the dataset and limit to 100 documents
    print(f"Loaded {len(documents)} documents.")

    # Preprocess the documents
    print("Preprocessing documents...")
    documents = preprocess_documents(documents)

    # Fit the model on the documents
    print("Fitting the BERTopic model...")
    topics, probs = topic_model.fit_transform(documents)

    # Get topic information
    topic_info = topic_model.get_topic_info()

    # Print the main topics with importance scores
    print("\nMain Topics with Word Importance Scores:")
    for index, row in topic_info.iterrows():
        topic_id = row['Topic']
        if topic_id == -1:
            continue  # Skip outliers
        topic_freq = row['Count']
        topic_words = topic_model.get_topic(topic_id)

        # Prepare a list of formatted word-score pairs
        word_score_list = [
            f"{word} ({score:.4f})" for word, score in topic_words
        ]

        # Join the pairs into a single string
        word_score_str = ', '.join(word_score_list)

        # Print the topic info and the word-score string
        print(f"\nTopic {topic_id} (Frequency: {topic_freq}):")
        print(f"  {word_score_str}")

    print("\nTopic modeling completed.")
    return len(documents), None
