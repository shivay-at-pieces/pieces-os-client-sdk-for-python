# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from pieces_os_client.models.classification_generic_enum import ClassificationGenericEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.model import Model

class CodeAnalysis(BaseModel):
    """
    This is the ML Analysis object Specific to code.  prediction and similarity are custom types {[string]: number}. ** please dont not modify **  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    tokenized: Optional[conlist(StrictStr)] = None
    language: Optional[StrictStr] = None
    type: ClassificationGenericEnum = Field(...)
    prediction: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = None
    similarity: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = None
    top5_colors: Optional[conlist(StrictInt)] = Field(None, alias="top5Colors")
    top5_sorted: Optional[conlist(StrictStr)] = Field(None, alias="top5Sorted")
    id: StrictStr = Field(...)
    analysis: StrictStr = Field(..., description="this is just a reference to the analysis parent object.")
    model: Model = Field(...)
    __properties = ["schema", "tokenized", "language", "type", "prediction", "similarity", "top5Colors", "top5Sorted", "id", "analysis", "model"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CodeAnalysis:
        """Create an instance of CodeAnalysis from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CodeAnalysis:
        """Create an instance of CodeAnalysis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CodeAnalysis.parse_obj(obj)

        _obj = CodeAnalysis.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "tokenized": obj.get("tokenized"),
            "language": obj.get("language"),
            "type": obj.get("type"),
            "prediction": obj.get("prediction"),
            "similarity": obj.get("similarity"),
            "top5_colors": obj.get("top5Colors"),
            "top5_sorted": obj.get("top5Sorted"),
            "id": obj.get("id"),
            "analysis": obj.get("analysis"),
            "model": Model.from_dict(obj.get("model")) if obj.get("model") is not None else None
        })
        return _obj


