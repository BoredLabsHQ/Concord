# coding: utf-8

from typing import List  # noqa: F401

from concord.bert.concord import concord
from concord.server.apis.channels_api_base import BaseChannelsApi
from concord.server.models.channel_messages_request import ChannelMessagesRequest
from concord.server.models.channel_messages_response import ChannelMessagesResponse
from concord.server.models.channel_related_response import ChannelRelatedResponse
from concord.server.models.channel_topics_response import ChannelTopicsResponse


class ChannelsApiImpl(BaseChannelsApi):
    """Implementation of the BaseChannelsApi with boilerplate responses."""

    async def get_channel_topics(
        self,
        platform_id: str,
        channel_id: str,
    ) -> ChannelTopicsResponse:
        """Returns extracted topics for the specified channel."""
        # TODO Boilerplate/mock implementation
        mock_topics = [
            {
                "topic_id": "1",
                "name": "General Discussion"
            },
            {
                "topic_id": "2",
                "name": "Announcements"
            },
            {
                "topic_id": "3",
                "name": "Feedback"
            },
        ]
        return ChannelTopicsResponse(platform_id=platform_id,
                                     channel_id=channel_id,
                                     topics=mock_topics)

    async def get_related_channels(
        self,
        platform_id: str,
        channel_id: str,
        max_channels: int,
    ) -> ChannelRelatedResponse:
        """Fetches channels discussing topics similar to the specified channel."""
        # TODO Boilerplate/mock implementation
        mock_related_channels = [
            {
                "channel_id": "channel_123",
                "name": "Tech Talk"
            },
            {
                "channel_id": "channel_456",
                "name": "Developer Hub"
            },
            {
                "channel_id": "channel_789",
                "name": "Project Updates"
            },
        ][:max_channels]
        return ChannelRelatedResponse(platform_id=platform_id,
                                      channel_id=channel_id,
                                      related_channels=mock_related_channels)

    async def post_channel_messages(
        self,
        platform_id: str,
        channel_id: str,
        channel_messages_request: ChannelMessagesRequest,
    ) -> ChannelMessagesResponse:
        """Processes a message feed from a specified channel and updates associated topics."""
        processed_count, error = concord(channel_messages_request.messages)
        if processed_count == -1:
            return ChannelMessagesResponse(status="error", error=error)
        return ChannelMessagesResponse(platform_id=platform_id,
                                       channel_id=channel_id,
                                       processed_messages=processed_count,
                                       success=True,
                                       status="success")
