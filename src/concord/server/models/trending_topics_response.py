# coding: utf-8

"""
    Concord API

    API for Concord, an AI-powered semantic extraction and recommendation platform for networked communities.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictStr

from src.concord.server.models.trending_topics_response_topics_inner import TrendingTopicsResponseTopicsInner

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TrendingTopicsResponse(BaseModel):
    """
    TrendingTopicsResponse
    """

    # noqa: E501
    time_window: Optional[StrictStr] = Field(
        default=None,
        description="The specified time window for trending topics.")
    topics: Optional[List[TrendingTopicsResponseTopicsInner]] = None
    __properties: ClassVar[List[str]] = ["time_window", "topics"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TrendingTopicsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in topics (list)
        _items = []
        if self.topics:
            for _item in self.topics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['topics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TrendingTopicsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "time_window":
                obj.get("time_window"),
            "topics": [
                TrendingTopicsResponseTopicsInner.from_dict(_item)
                for _item in obj.get("topics")
            ] if obj.get("topics") is not None else None
        })
        return _obj
