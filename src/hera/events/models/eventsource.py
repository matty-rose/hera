# generated by datamodel-codegen:
#   filename:  argo-workflows-3.4.4.json

from __future__ import annotations

from typing import Optional

from hera.shared._pydantic import BaseModel, Field

from .io.argoproj.events import v1alpha1
from .io.k8s.apimachinery.pkg.apis.meta import v1


class EventSourceDeletedResponse(BaseModel):
    pass


class LogEntry(BaseModel):
    event_name: Optional[str] = Field(
        default=None, alias="eventName", title="optional - the event name (e.g. `example`)"
    )
    event_source_name: Optional[str] = Field(default=None, alias="eventSourceName")
    event_source_type: Optional[str] = Field(
        default=None, alias="eventSourceType", title="optional - the event source type (e.g. `webhook`)"
    )
    level: Optional[str] = None
    msg: Optional[str] = None
    namespace: Optional[str] = None
    time: Optional[v1.Time] = None


class CreateEventSourceRequest(BaseModel):
    event_source: Optional[v1alpha1.EventSource] = Field(default=None, alias="eventSource")
    namespace: Optional[str] = None


class EventSourceWatchEvent(BaseModel):
    object: Optional[v1alpha1.EventSource] = None
    type: Optional[str] = None


class UpdateEventSourceRequest(BaseModel):
    event_source: Optional[v1alpha1.EventSource] = Field(default=None, alias="eventSource")
    name: Optional[str] = None
    namespace: Optional[str] = None
