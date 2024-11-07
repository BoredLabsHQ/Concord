# coding: utf-8

from fastapi.testclient import TestClient

from concord.server.models.channel_messages_request import ChannelMessagesRequest  # noqa: F401
from concord.server.models.channel_related_response import ChannelRelatedResponse  # noqa: F401
from concord.server.models.setup_complete200_response import SetupComplete200Response  # noqa: F401


def test_process_memory(client: TestClient):
    """Test case for process_memory

    Process memory data and retrieve related channels
    """
    # channel_messages_request = {"messages": ["messages", "messages"]}

    # headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "POST",
    #    "/process-memory",
    #    headers=headers,
    #    json=channel_messages_request,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_setup_complete(client: TestClient):
    """Test case for setup_complete

    Confirm setup completion for Concord Channel Finder
    """

    # headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "GET",
    #    "/setup-complete",
    #    headers=headers,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
