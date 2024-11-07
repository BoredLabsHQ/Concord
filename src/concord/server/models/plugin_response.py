# coding: utf-8

"""
    Concord API

    API for Concord, an AI-powered semantic extraction and recommendation platform for networked communities.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class PluginResponse(BaseModel):
    """
    PluginResponse
    """

    # noqa: E501
    plugin_name: StrictStr = Field(
        description="Name of the plugin providing the response.",
        alias="pluginName")
    result: StrictStr = Field(
        description="Result or output from the plugin's processing.")
    status: StrictStr = Field(
        description=
        "Status indicating success or failure of the plugin operation.")
    error: Optional[StrictStr] = Field(
        default=None,
        description="Optional error message if the plugin operation failed.")
    __properties: ClassVar[List[str]] = [
        "pluginName", "result", "status", "error"
    ]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('success', 'failure'):
            raise ValueError(
                "must be one of enum values ('success', 'failure')")
        return value

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
        """Create an instance of PluginResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PluginResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pluginName": obj.get("pluginName"),
            "result": obj.get("result"),
            "status": obj.get("status"),
            "error": obj.get("error")
        })
        return _obj