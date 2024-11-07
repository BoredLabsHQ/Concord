## Nodes

### Channel

- **channel_id**: Unique identifier for the channel.
- **name**: Name of the channel.
- **description**: Brief description of the channel.
- **created_at**: Timestamp indicating when the channel was created.
- **language**: Language predominantly used in the channel.
- **activity_score**: Numerical score representing the activity level in the channel.

**Methods**:
- `create_channel`: Creates a new channel with specified details.
- `associate_with_topic`: Connects a topic to the channel, setting scores and trend.
- `add_semantic_vector`: Adds a semantic vector to the channel.

---

### Topic

- **topic_id**: Unique identifier for the topic.
- **name**: Summary name of the topic.
- **keywords**: List of key terms and associated weights (e.g., `[{"term": "AI", "weight": 0.35}]`).
- **bertopic_metadata**: Metadata from BerTopic processing.
- **topic_embedding**: Vector embedding for the topic.
- **updated_at**: Timestamp of the last update.

**Methods**:
- `create_topic`: Creates a new topic with specified keywords and metadata.
- `relate_to_topic`: Relates this topic to another, setting similarity metrics.
- `add_update`: Adds a topic update with score change and keywords.
- `set_topic_embedding`: Sets the embedding vector for the topic.
- `get_topic_embedding`: Retrieves the embedding as a numpy array.

---

### TopicUpdate

- **update_id**: Unique identifier for the update.
- **keywords**: Keywords associated with this update.
- **score_delta**: Numerical change in the topic score.
- **timestamp**: Time when the update was made.
- **topic_embedding**: Vector embedding for the topic.

**Methods**:
- `create_topic_update`: Creates a new update for a topic.
- `link_to_channel`: Links this update to a channel.

---

### SemanticVector

- **vector_id**: Unique identifier for the semantic vector.
- **semantic_vector**: Aggregated vector summarizing recent message semantics.
- **created_at**: Timestamp indicating creation.

**Methods**:
- `create_semantic_vector`: Creates a new semantic vector.

---

## Relationships

### ASSOCIATED_WITH (Channel → Topic)

- **topic_score**: Weighted score indicating a topic's relevance to the channel.
- **last_updated**: Last time the relationship was updated.
- **trend**: Trend indication for the topic within the channel.

---

### RELATED_TO (Topic ↔ Topic)

- **similarity_score**: Similarity metric between topics.
- **temporal_similarity**: Measure of similarity persistence over time.
- **co_occurrence_rate**: Rate of joint appearance in discussions.
- **common_channels**: Count of shared channels discussing both topics.
- **topic_trend_similarity**: Trend similarity between topics across channels.

---

### HasRel (General Relationship)

This relationship can be used as a generic placeholder for relationships that do not have specific attributes.

> **Note**: The relationships provide both dynamic and static metrics, such as similarity scores and temporal similarity, enabling analytical insights into evolving topic relationships.

