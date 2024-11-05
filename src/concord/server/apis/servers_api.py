# coding: utf-8

import importlib
import pkgutil
from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter, Body, Cookie, Depends, Form, Header, HTTPException, Path, Query,
    Response, Security, status,
)

import openapi_server
from src.concord.server.apis.servers_api_base import BaseServersApi
from src.concord.server.models.extra_models import TokenModel  # noqa: F401
from src.concord.server.models.server_register_request import ServerRegisterRequest
from src.concord.server.models.server_register_response import ServerRegisterResponse

router = APIRouter()

ns_pkg = openapi_server
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/servers/register",
    responses={
        201: {
            "model": ServerRegisterResponse,
            "description": "Server/group registered successfully."
        },
        400: {
            "description": "Invalid input data or missing required fields."
        },
        409: {
            "description":
                "Conflict if server/group with the same name exists."
        },
    },
    tags=["servers"],
    summary="Register a new server/group on a specified platform",
    response_model_by_alias=True,
)
async def register_server(
        server_register_request: ServerRegisterRequest = Body(None,
                                                              description=""),
) -> ServerRegisterResponse:
    """Creates a new entry for a server/group, allowing configuration of the platform, server/group name, and an authentication token. Additional metadata fields are provided for further configuration."""
    if not BaseServersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseServersApi.subclasses[0]().register_server(
        server_register_request)
