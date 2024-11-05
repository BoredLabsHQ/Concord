# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from src.concord.server.models.trending_topics_response import TrendingTopicsResponse


class BaseTrendingApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTrendingApi.subclasses = BaseTrendingApi.subclasses + (cls,)

    async def get_trending_topics(
            self,
            time_window: str,
            topic_limit: int,
            channel_limit: int,
    ) -> TrendingTopicsResponse:
        """Returns a list of trending topics along with the associated channels for a specified time window, such as a week, month, or year. The number of topics and channels can also be customized."""
        ...
