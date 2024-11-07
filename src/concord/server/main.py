# coding: utf-8

"""
    Concord API

    API for Concord, an AI-powered semantic extraction and recommendation platform for networked communities.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from fastapi import FastAPI
from concord.server.app_lifespan import lifespan

from concord.server.apis.channels_api import router as ChannelsApiRouter
from concord.server.apis.external_integration_api import router as ExternalIntegrationApiRouter
from concord.server.apis.servers_api import router as ServersApiRouter
from concord.server.apis.trending_api import router as TrendingApiRouter

app = FastAPI(
    title="Concord API",
    description=
    "API for Concord, an AI-powered semantic extraction and recommendation platform for networked communities.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(ChannelsApiRouter)
app.include_router(ExternalIntegrationApiRouter)
app.include_router(ServersApiRouter)
app.include_router(TrendingApiRouter)
