# tests/test_schema.py
import os

import pytest
from neomodel import config
from neomodel import db, clear_neo4j_database

from concord.graph.schema import Channel, Topic, TopicUpdate, SemanticVector


@pytest.fixture(scope='session', autouse=True)
def setup_and_teardown_db():
    """
    Fixture to handle database setup before tests and teardown after tests.
    Ensures that the database is cleaned even if tests are interrupted.
    """
    # Construct the DATABASE_URL using environment variables
    neo4j_user = os.getenv('NEO4J_USER', 'neo4j')
    neo4j_password = os.getenv('NEO4J_PASSWORD', 'test-password')
    neo4j_host = os.getenv('NEO4J_HOST', 'localhost')
    neo4j_port = os.getenv('NEO4J_PORT', '7688')
    config.DATABASE_URL = f'bolt://{neo4j_user}:{neo4j_password}@{neo4j_host}:{neo4j_port}'

    try:
        # Setup code: Clear the database before running tests
        clear_neo4j_database(db)
        yield
    finally:
        # Teardown code: Clear the database after tests, even if interrupted
        clear_neo4j_database(db)


def test_create_channel():
    channel = Channel.create_channel(platform='YouTube',
                                     name='TechChannel',
                                     description='A channel about tech',
                                     active_members_count=1000,
                                     language='English',
                                     region='US',
                                     activity_score=75.5)
    assert channel.platform == 'YouTube'
    assert channel.name == 'TechChannel'
    assert channel.active_members_count == 1000


def test_associate_channel_with_topic():
    channel = Channel.create_channel(platform='YouTube',
                                     name='TechChannel',
                                     description='A channel about tech',
                                     active_members_count=1000,
                                     language='English',
                                     region='US',
                                     activity_score=75.5)
    topic = Topic.create_topic(name='Artificial Intelligence',
                               keywords=['AI', 'Machine Learning'],
                               overall_score=85.0,
                               bertopic_metadata={'some_key': 'some_value'})
    channel.associate_with_topic(topic=topic,
                                 channel_score=90.0,
                                 keywords_weights=['0.8', '0.2'],
                                 message_count=500,
                                 score_decay_rate=0.01,
                                 trend='upward')
    rel = channel.topics.relationship(topic)
    assert rel is not None
    assert rel.channel_score == 90.0
    assert rel.trend == 'upward'


def test_add_semantic_vector_to_channel():
    channel = Channel.create_channel(platform='YouTube',
                                     name='TechChannel',
                                     description='A channel about tech',
                                     active_members_count=1000,
                                     language='English',
                                     region='US',
                                     activity_score=75.5)
    semantic_vector_values = [0.1, 0.2, 0.3]
    semantic_vector = channel.add_semantic_vector(semantic_vector_values)
    assert semantic_vector is not None
    assert semantic_vector.semantic_vector == semantic_vector_values
    connected_channel = semantic_vector.channel.single()
    assert connected_channel.element_id == channel.element_id  # Use element_id


def test_create_topic():
    topic = Topic.create_topic(name='Artificial Intelligence',
                               keywords=['AI', 'Machine Learning'],
                               overall_score=85.0,
                               bertopic_metadata={'some_key': 'some_value'})
    assert topic.name == 'Artificial Intelligence'
    assert topic.overall_score == 85.0


def test_relate_topics():
    topic1 = Topic.create_topic(name='Artificial Intelligence',
                                keywords=['AI', 'Machine Learning'],
                                overall_score=85.0,
                                bertopic_metadata={'some_key': 'some_value'})
    topic2 = Topic.create_topic(
        name='Deep Learning',
        keywords=['Neural Networks', 'AI'],
        overall_score=80.0,
        bertopic_metadata={'another_key': 'another_value'})
    topic1.relate_to_topic(other_topic=topic2,
                           similarity_score=0.95,
                           temporal_similarity=0.9,
                           co_occurrence_rate=0.85,
                           common_channels=5,
                           topic_trend_similarity=0.8)
    rel = topic1.related_topics.relationship(topic2)
    assert rel is not None
    assert rel.similarity_score == 0.95
    assert rel.common_channels == 5


def test_add_update_to_topic():
    topic = Topic.create_topic(name='Artificial Intelligence',
                               keywords=['AI', 'Machine Learning'],
                               overall_score=85.0,
                               bertopic_metadata={'some_key': 'some_value'})
    update = topic.add_update(update_keywords=['Deep Learning'],
                              score_delta=5.0)
    assert update is not None
    assert update.score_delta == 5.0
    connected_topic = update.topic.single()
    assert connected_topic.element_id == topic.element_id  # Use element_id


def test_create_topic_update():
    update = TopicUpdate.create_topic_update(keywords=['Deep Learning'],
                                             score_delta=5.0)
    assert update.keywords == ['Deep Learning']
    assert update.score_delta == 5.0


def test_link_topic_update_to_channel():
    channel = Channel.create_channel(platform='YouTube',
                                     name='TechChannel',
                                     description='A channel about tech',
                                     active_members_count=1000,
                                     language='English',
                                     region='US',
                                     activity_score=75.5)
    update = TopicUpdate.create_topic_update(keywords=['Deep Learning'],
                                             score_delta=5.0)
    update.link_to_channel(channel)
    connected_channel = update.channel.single()
    assert connected_channel.element_id == channel.element_id  # Use element_id


def test_create_semantic_vector():
    semantic_vector_values = [0.1, 0.2, 0.3]
    semantic_vector = SemanticVector.create_semantic_vector(
        semantic_vector_values)
    assert semantic_vector.semantic_vector == semantic_vector_values
