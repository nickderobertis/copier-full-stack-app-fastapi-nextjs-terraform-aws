# generated by datamodel-codegen:
#   filename:  sentry-list-event-schema.json
#   timestamp: 2022-09-05T10:27:01+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Tag(BaseModel):
    value: Optional[str] = None
    key: Optional[str] = None


class Data(BaseModel):
    isStaff: Optional[bool] = None


class User(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    ip_address: Optional[str] = None
    email: Optional[str] = None
    data: Optional[Data] = None
    id: Optional[str] = None


class SentryListEventResponseItem(BaseModel):
    eventID: Optional[str] = None
    tags: Optional[List[Tag]] = None
    dateCreated: Optional[str] = None
    user: Optional[User] = None
    message: Optional[str] = None
    id: Optional[str] = None
    platform: Optional[str] = None
    event_type: Optional[str] = Field(None, alias="event.type")
    groupID: Optional[str] = None
    title: Optional[str] = None


class SentryListEventResponse(BaseModel):
    __root__: Optional[List[SentryListEventResponseItem]] = None
