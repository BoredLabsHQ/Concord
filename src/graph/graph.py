# graph.py
import os

from neo4j import GraphDatabase


# Initialize Neo4j driver
def initialize_neo4j():
    # Get uri username and password from ENV
    user = os.environ.get("NEO4J_USERNAME")
    password = os.environ.get("NEO4J_PASSWORD")
    uri = os.environ.get("NEO4J_URI")

    return GraphDatabase.driver(uri, auth=(user, password))


# Function to store topics in Neo4j
def store_topics_in_neo4j(model, batch_num):
    """
    Store topics and their relationships in Neo4j.
    """
    driver = initialize_neo4j()
    with driver.session() as session:
        topics = model.get_topics()
        for topic_num, words in topics.items():
            if topic_num == -1:
                continue  # -1 is usually the outlier/noise topic
            # Create Topic node
            session.run(
                "MERGE (t:Topic {id: $id}) "
                "SET t.keywords = $keywords, t.batch = $batch",
                id=topic_num,
                keywords=words,
                batch=batch_num,
            )
    driver.close()
    print("Topics stored in Neo4j.")
