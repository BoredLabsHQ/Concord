# coding: utf-8

from fastapi.testclient import TestClient

from src.concord.server.models.trending_topics_response import TrendingTopicsResponse  # noqa: F401


def test_get_trending_topics(client: TestClient):
    """Test case for get_trending_topics

    Retrieve trending topics within a specific time window
    """
    params = [("time_window", 'time_window_example'), ("topic_limit", 10),
              ("channel_limit", 5)]
    headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "GET",
    #    "/trending/topics",
    #    headers=headers,
    #    params=params,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
