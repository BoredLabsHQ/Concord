# coding: utf-8

from fastapi.testclient import TestClient

from src.concord.server.models.server_register_request import ServerRegisterRequest  # noqa: F401
from src.concord.server.models.server_register_response import ServerRegisterResponse  # noqa: F401


def test_register_server(client: TestClient):
    """Test case for register_server

    Register a new server/group on a specified platform
    """
    # server_register_request = {
    #     "webhook_url": "https://openapi-generator.tech",
    #     "name": "name",
    #     "description": "description",
    #     "auth_token": "auth_token",
    #     "platform": "matrix",
    #     "contact_email": "contact_email"
    # }
    #
    # headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "POST",
    #    "/servers/register",
    #    headers=headers,
    #    json=server_register_request,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
