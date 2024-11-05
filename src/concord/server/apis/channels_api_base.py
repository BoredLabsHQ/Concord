# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from src.concord.server.models.channel_messages_request import ChannelMessagesRequest
from src.concord.server.models.channel_messages_response import ChannelMessagesResponse
from src.concord.server.models.channel_related_response import ChannelRelatedResponse
from src.concord.server.models.channel_topics_response import ChannelTopicsResponse


class BaseChannelsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseChannelsApi.subclasses = BaseChannelsApi.subclasses + (cls,)

    async def get_channel_topics(
            self,
            platform_id: str,
            channel_id: str,
    ) -> ChannelTopicsResponse:
        """Returns the list of topics extracted from the specified channel."""
        ...

    async def get_related_channels(
            self,
            platform_id: str,
            channel_id: str,
            max_channels: int,
    ) -> ChannelRelatedResponse:
        """Fetches a list of channels that discuss topics similar to those of the specified channel, with an option to limit the number of channels returned."""
        ...

    async def post_channel_messages(
            self,
            platform_id: str,
            channel_id: str,
            channel_messages_request: ChannelMessagesRequest,
    ) -> ChannelMessagesResponse:
        """Receives messages or an export of an entire channel from platforms like Matrix, Slack, Telegram, or Discord. Extracts semantics and updates topics associated with the channel."""
        ...
