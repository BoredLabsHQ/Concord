# coding: utf-8

from fastapi.testclient import TestClient

from src.concord.server.models.channel_messages_request import ChannelMessagesRequest  # noqa: F401
from src.concord.server.models.channel_messages_response import ChannelMessagesResponse  # noqa: F401
from src.concord.server.models.channel_related_response import ChannelRelatedResponse  # noqa: F401
from src.concord.server.models.channel_topics_response import ChannelTopicsResponse  # noqa: F401


def test_get_channel_topics(client: TestClient):
    """Test case for get_channel_topics

    Get extracted topics for a specific channel
    """

    headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "GET",
    #    "/channels/{platform_id}/{channel_id}/topics".format(platform_id='platform_id_example', channel_id='channel_id_example'),
    #    headers=headers,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_get_related_channels(client: TestClient):
    """Test case for get_related_channels

    Retrieve channels discussing similar topics
    """
    params = [("max_channels", 10)]
    headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "GET",
    #    "/channels/{platform_id}/{channel_id}/related".format(platform_id='platform_id_example', channel_id='channel_id_example'),
    #    headers=headers,
    #    params=params,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_post_channel_messages(client: TestClient):
    """Test case for post_channel_messages

    Upload messages from a specific channel for processing
    """
    channel_messages_request = {"messages": ["messages", "messages"]}

    headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "POST",
    #    "/channels/{platform_id}/{channel_id}/messages".format(platform_id='platform_id_example', channel_id='channel_id_example'),
    #    headers=headers,
    #    json=channel_messages_request,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
