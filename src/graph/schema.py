# schema.py
from datetime import datetime
from typing import List, Dict, Any

from neomodel import (StructuredNode, StructuredRel, StringProperty,
                      IntegerProperty, FloatProperty, DateTimeProperty,
                      ArrayProperty, UniqueIdProperty, JSONProperty,
                      RelationshipTo, RelationshipFrom, Relationship)


# Relationship Models
class AssociatedWithRel(StructuredRel):
    topic_score = FloatProperty()
    keywords_weights = ArrayProperty()
    message_count = IntegerProperty()
    last_updated = DateTimeProperty()
    trend = StringProperty()


class RelatedToRel(StructuredRel):
    similarity_score = FloatProperty()
    temporal_similarity = FloatProperty()
    co_occurrence_rate = FloatProperty()
    common_channels = IntegerProperty()
    topic_trend_similarity = FloatProperty()


# Nodes
class Channel(StructuredNode):
    channel_id = UniqueIdProperty()
    platform = StringProperty()
    name = StringProperty()
    description = StringProperty()
    created_at = DateTimeProperty(default_now=True)
    active_members_count = IntegerProperty()
    language = StringProperty()
    region = StringProperty()
    activity_score = FloatProperty()

    # Relationships
    topics = RelationshipTo('Topic',
                            'ASSOCIATED_WITH',
                            model=AssociatedWithRel)
    semantic_vectors = RelationshipFrom('SemanticVector', 'BELONGS_TO')
    updates = RelationshipFrom('TopicUpdate', 'UPDATED_FROM')

    # Wrapper Functions
    @classmethod
    def create_channel(cls, platform: str, name: str, description: str,
                       active_members_count: int, language: str, region: str,
                       activity_score: float) -> 'Channel':
        return cls(platform=platform,
                   name=name,
                   description=description,
                   active_members_count=active_members_count,
                   language=language,
                   region=region,
                   activity_score=activity_score).save()

    def associate_with_topic(self, topic: 'Topic', channel_score: float,
                             keywords_weights: List[str], message_count: int,
                             trend: str) -> None:
        self.topics.connect(
            topic, {
                'channel_score': channel_score,
                'keywords_weights': keywords_weights,
                'message_count': message_count,
                'last_updated': datetime.utcnow(),
                'trend': trend
            })

    def add_semantic_vector(
            self, semantic_vector_values: List[float]) -> 'SemanticVector':
        semantic_vector = SemanticVector.create_semantic_vector(
            semantic_vector_values)
        semantic_vector.channel.connect(self)
        return semantic_vector


class Topic(StructuredNode):
    topic_id = UniqueIdProperty()
    name = StringProperty()
    keywords = ArrayProperty()
    bertopic_metadata = JSONProperty()
    topic_embedding = ArrayProperty()
    updated_at = DateTimeProperty(default_now=True)

    # Relationships
    channels = RelationshipFrom('Channel',
                                'ASSOCIATED_WITH',
                                model=AssociatedWithRel)
    related_topics = Relationship('Topic', 'RELATED_TO', model=RelatedToRel)
    updates = RelationshipFrom('TopicUpdate', 'UPDATE_OF')

    # Wrapper Functions
    @classmethod
    def create_topic(cls, name: str, keywords: List[str],
                     bertopic_metadata: Dict[str, Any]) -> 'Topic':
        """
        Create a new topic node with the given properties.
        """
        return cls(name=name,
                   keywords=keywords,
                   bertopic_metadata=bertopic_metadata).save()

    def relate_to_topic(self, other_topic: 'Topic', similarity_score: float,
                        temporal_similarity: float, co_occurrence_rate: float,
                        common_channels: int,
                        topic_trend_similarity: float) -> None:
        """
        Create a relationship to another topic with various similarity metrics.
        """
        if not isinstance(other_topic, Topic):
            raise ValueError("The related entity must be a Topic instance.")
        self.related_topics.connect(
            other_topic, {
                'similarity_score': similarity_score,
                'temporal_similarity': temporal_similarity,
                'co_occurrence_rate': co_occurrence_rate,
                'common_channels': common_channels,
                'topic_trend_similarity': topic_trend_similarity
            })

    def add_update(self, update_keywords: List[str],
                   score_delta: float) -> 'TopicUpdate':
        """
        Add an update to the topic with keyword changes and score delta.
        """
        update = TopicUpdate.create_topic_update(update_keywords, score_delta)
        update.topic.connect(self)
        return update

    def set_topic_embedding(self, embedding: List[float]) -> None:
        """
        Set the topic embedding vector, ensuring all values are floats.
        """
        if not all(isinstance(val, float) for val in embedding):
            raise ValueError("All elements in topic_embedding must be floats.")
        self.topic_embedding = embedding
        self.save()


class TopicUpdate(StructuredNode):
    update_id = UniqueIdProperty()
    keywords = ArrayProperty()
    score_delta = FloatProperty()
    timestamp = DateTimeProperty(default_now=True)

    # Relationships
    channel = RelationshipTo('Channel', 'UPDATED_FROM')
    topic = RelationshipTo('Topic', 'UPDATE_OF')

    # Wrapper Functions
    @classmethod
    def create_topic_update(cls, keywords: List[str],
                            score_delta: float) -> 'TopicUpdate':
        return cls(keywords=keywords, score_delta=score_delta).save()

    def link_to_channel(self, channel: 'Channel') -> None:
        self.channel.connect(channel)


class SemanticVector(StructuredNode):
    vector_id = UniqueIdProperty()
    semantic_vector = ArrayProperty()
    created_at = DateTimeProperty(default_now=True)

    # Relationships
    channel = RelationshipTo('Channel', 'BELONGS_TO')

    # Wrapper Functions
    @classmethod
    def create_semantic_vector(
            cls, semantic_vector_values: List[float]) -> 'SemanticVector':
        return cls(semantic_vector=semantic_vector_values).save()
