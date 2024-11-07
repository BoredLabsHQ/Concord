# concord.py
from bert.pre_process import preprocess_documents
from graph.schema import Topic, Channel, Platform


def concord(bert_topic, channel_id, platform_id, documents):
    platform, channel = platform_channel_handler(channel_id, platform_id)

    # Load and preprocess documents
    print(f"Loaded {len(documents)} documents.")
    print("Preprocessing documents...")
    documents = preprocess_documents(documents)

    # Fit the topic model
    print("Fitting the BERTopic model...")
    bert_topic.fit(documents)
    topic_info = bert_topic.get_topic_info()

    # Log main topics
    print("\nMain Topics with Word Importance Scores:")
    for index, row in topic_info.iterrows():
        topic_id = row['Topic']
        if topic_id == -1:
            continue  # Skip outliers
        topic_freq = row['Count']
        topic_words = bert_topic.get_topic(topic_id)

        # Create a list of word-score pairs
        word_score_list = [{
            "term": word,
            "weight": score
        } for word, score in topic_words]

        # Create or update a Topic node
        topic = Topic.create_topic(name=f"Topic {topic_id}",
                                   keywords=word_score_list,
                                   bertopic_metadata={
                                       "frequency": topic_freq
                                   }).save()
        topic.set_topic_embedding(bert_topic.topic_embeddings_[topic_id])
        channel.associate_with_topic(topic, channel_score=0.5, trend="")

        print(f"\nTopic {topic_id} (Frequency: {topic_freq}):")
        print(
            f"  {', '.join([f'{word} ({score:.4f})' for word, score in topic_words])}"
        )

    print("\nTopic modeling and channel update completed.")
    return len(documents), None


def platform_channel_handler(channel_id, platform_id):
    platform = Platform.nodes.get_or_none(platform_id=platform_id)
    if not platform:
        print(
            f"Platform with ID '{platform_id}' not found. Creating new platform..."
        )
        platform = Platform(platform_id=platform_id).save()
    channel = Channel.nodes.get_or_none(channel_id=channel_id)
    if not channel:
        print(
            f"Channel with ID '{channel_id}' not found. Creating new channel..."
        )
        channel = Channel.create_channel(
            channel_id=channel_id,
            name=f"Channel {channel_id}",
            description="",
            language="English",
            activity_score=0.0,
        ).save()
    platform.channels.connect(channel)
    return platform, channel
