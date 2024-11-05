# coding: utf-8

import importlib
import pkgutil
from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter, Body, Cookie, Depends, Form, Header, HTTPException, Path, Query,
    Response, Security, status,
)

import openapi_server
from src.concord.server.apis.trending_api_base import BaseTrendingApi
from src.concord.server.models.extra_models import TokenModel  # noqa: F401
from src.concord.server.models.trending_topics_response import TrendingTopicsResponse

router = APIRouter()

ns_pkg = openapi_server
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/trending/topics",
    responses={
        200: {
            "model": TrendingTopicsResponse,
            "description":
                "List of trending topics and their associated channels."
        },
        400: {
            "description": "Invalid time window or parameters."
        },
    },
    tags=["trending"],
    summary="Retrieve trending topics within a specific time window",
    response_model_by_alias=True,
)
async def get_trending_topics(
        time_window: str = Query(None,
                                 description="Time window for trending topics.",
                                 alias="time_window"),
        topic_limit: int = Query(
            10,
            description="Maximum number of trending topics to retrieve.",
            alias="topic_limit"),
        channel_limit: int = Query(
            5,
            description="Maximum number of channels per topic to retrieve.",
            alias="channel_limit"),
) -> TrendingTopicsResponse:
    """Returns a list of trending topics along with the associated channels for a specified time window, such as a week, month, or year. The number of topics and channels can also be customized."""
    if not BaseTrendingApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrendingApi.subclasses[0]().get_trending_topics(
        time_window, topic_limit, channel_limit)
