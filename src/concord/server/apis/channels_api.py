# coding: utf-8

import importlib
import pkgutil
from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter, Body, Cookie, Depends, Form, Header, HTTPException, Path, Query,
    Response, Security, status,
)

import openapi_server
from src.concord.server.apis.channels_api_base import BaseChannelsApi
from src.concord.server.models.channel_messages_request import ChannelMessagesRequest
from src.concord.server.models.channel_messages_response import ChannelMessagesResponse
from src.concord.server.models.channel_related_response import ChannelRelatedResponse
from src.concord.server.models.channel_topics_response import ChannelTopicsResponse
from src.concord.server.models.extra_models import TokenModel  # noqa: F401

router = APIRouter()

ns_pkg = openapi_server
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/channels/{platform_id}/{channel_id}/topics",
    responses={
        200: {
            "model": ChannelTopicsResponse,
            "description": "List of topics associated with the channel."
        },
        404: {
            "description": "Channel or topics not found."
        },
    },
    tags=["channels"],
    summary="Get extracted topics for a specific channel",
    response_model_by_alias=True,
)
async def get_channel_topics(
        platform_id: str = Path(
            ..., description="Unique identifier for the platform server/group."),
        channel_id: str = Path(...,
                               description="Unique identifier of the channel."),
) -> ChannelTopicsResponse:
    """Returns the list of topics extracted from the specified channel."""
    if not BaseChannelsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseChannelsApi.subclasses[0]().get_channel_topics(
        platform_id, channel_id)


@router.get(
    "/channels/{platform_id}/{channel_id}/related",
    responses={
        200: {
            "model": ChannelRelatedResponse,
            "description": "List of related channels."
        },
        404: {
            "description": "Channel not found."
        },
    },
    tags=["channels"],
    summary="Retrieve channels discussing similar topics",
    response_model_by_alias=True,
)
async def get_related_channels(
        platform_id: str = Path(
            ..., description="Unique identifier for the platform server/group."),
        channel_id: str = Path(...,
                               description="Unique identifier of the channel."),
        max_channels: int = Query(
            10,
            description="Maximum number of related channels to retrieve.",
            alias="max_channels"),
) -> ChannelRelatedResponse:
    """Fetches a list of channels that discuss topics similar to those of the specified channel, with an option to limit the number of channels returned."""
    if not BaseChannelsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseChannelsApi.subclasses[0]().get_related_channels(
        platform_id, channel_id, max_channels)


@router.post(
    "/channels/{platform_id}/{channel_id}/messages",
    responses={
        200: {
            "model": ChannelMessagesResponse,
            "description":
                "Successfully processed messages and updated topics."
        },
        400: {
            "description": "Invalid input data."
        },
    },
    tags=["channels"],
    summary="Upload messages from a specific channel for processing",
    response_model_by_alias=True,
)
async def post_channel_messages(
        platform_id: str = Path(
            ..., description="Unique identifier for the platform server/group."),
        channel_id: str = Path(...,
                               description="Unique identifier of the channel."),
        channel_messages_request: ChannelMessagesRequest = Body(None,
                                                                description=""),
) -> ChannelMessagesResponse:
    """Receives messages or an export of an entire channel from platforms like Matrix, Slack, Telegram, or Discord. Extracts semantics and updates topics associated with the channel."""
    if not BaseChannelsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseChannelsApi.subclasses[0]().post_channel_messages(
        platform_id, channel_id, channel_messages_request)
