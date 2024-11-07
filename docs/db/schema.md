## Nodes

### Channel

- **channel_id**: Unique identifier
- **platform**: Platform (e.g., Telegram)
- **name**: Name of the channel
- **description**: Description of the channel
- **created_at**: Creation date
- **active_members_count**: Number of active members
- **language**: Language of the channel
- **region**: Geographical region
- **activity_score**: Posting activity score, indicating channel activity level

---

### Topic

- **topic_id**: Unique identifier
- **name**: Summary of the topic
- **keywords**: List of key terms with associated weights (e.g., `[{"term": "AI", "weight": 0.35}, {"term": "neural networks", "weight": 0.28}]`)
- **bertopic_metadata**: BerTopic metadata
- **topic_embedding: Topic embedding
- **updated_at**: Last updated timestamp

---

### TopicUpdate

- **update_id**: Unique identifier
- **channel_id**: Associated channel
- **topic_id**: Associated topic
- **keywords**: Keywords from the update
- **score_delta**: Change in topic score
- **timestamp**: Update time

---

### SemanticVector

- **vector_id**: Unique identifier
- **semantic_vector**: Aggregated representation of recent message semantics in a channel, preserving privacy by summarizing content instead of storing individual messages.
- **created_at**: Creation date

> **Explanation**: The SemanticVector node represents a general semantic profile of recent messages in a channel, supporting dynamic topic relevance without storing each message individually. This approach aligns with privacy requirements while allowing for the adjustment of topic relevance.

---

## Relationships

### ASSOCIATED_WITH (Channel → Topic)

- **topic_score**: Cumulative or weighted score representing a topic’s importance or relevance to the channel
- **keywords_weights**: Channel-specific keywords and their weights, highlighting the unique relationship between the channel and topic
- **message_count**: Number of messages analyzed in relation to the topic
- **last_updated**: Timestamp of the last update
- **trend**: Indicator of topic trend over time within the channel

> **Explanation**: This relationship captures the importance of each topic to specific channels, with channel-specific keyword weights providing additional insight into unique topic-channel dynamics. `trend` enables tracking how each topic's relevance changes over time within the channel.

---

### RELATED_TO (Topic ↔ Topic)

- **similarity_score**: Degree of similarity between two topics
- **temporal_similarity**: Metric to track similarity over time
- **co-occurrence_rate**: Frequency of concurrent discussion of topics across channels
- **common_channels**: Number of shared channels discussing both topics
- **topic_trend_similarity**: Measure of similarity in topic trends across channels
