# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from src.concord.server.models.server_register_request import ServerRegisterRequest
from src.concord.server.models.server_register_response import ServerRegisterResponse


class BaseServersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseServersApi.subclasses = BaseServersApi.subclasses + (cls,)

    async def register_server(
            self,
            server_register_request: ServerRegisterRequest,
    ) -> ServerRegisterResponse:
        """Creates a new entry for a server/group, allowing configuration of the platform, server/group name, and an authentication token. Additional metadata fields are provided for further configuration."""
        ...
