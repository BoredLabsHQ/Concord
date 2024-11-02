# concord.py

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# from sklearn.datasets import fetch_20newsgroups
from data_loader import load_element_mock_messages
from bert.bert import fit_and_evaluate_model, initialize_model


def preprocess_documents(documents):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    processed_docs = []

    for doc in documents:
        doc = doc.lower()
        tokens = nltk.word_tokenize(doc)
        tokens = [word for word in tokens if word.isalpha()]
        tokens = [
            word for word in tokens if word not in stop_words and len(word) > 2
        ]
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        processed_doc = ' '.join(tokens)
        processed_docs.append(processed_doc)

    return processed_docs


def main():
    # print("Loading data...")
    # newsgroups = fetch_20newsgroups(subset='all',
    #                                 remove=('headers', 'footers', 'quotes'))
    # documents = newsgroups['data'][:100]
    # print(f"Loaded {len(documents)} documents.")

    print("Loading data from element_mock_messages...")
    documents = load_element_mock_messages()
    print(f"Loaded {len(documents)} documents.")

    print("Preprocessing documents...")
    documents = preprocess_documents(documents)

    # Initialize the BERTopic model with KeyBERTInspired representation
    print("Initializing BERTopic model...")
    topic_model = initialize_model()

    # Fit the model on the documents and get the fitted topic_model
    print("Fitting the BERTopic model...")
    topics, probs, topic_info_df, document_distribution_df, topic_model = fit_and_evaluate_model(
        documents)

    print("\nMain Topics and Their Sizes:")
    print(topic_info_df[['Topic', 'Count', 'Name']])

    # Print the main topics with importance scores
    print("\nMain Topics with Word Importance Scores:")
    for index, row in topic_info_df.iterrows():
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

    print("\nDocument-Topic Distribution:")
    print(document_distribution_df)

    print("\nTopic modeling completed.")


if __name__ == "__main__":
    main()
