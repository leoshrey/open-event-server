from marshmallow import Schema
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship
from marshmallow_jsonapi.flask import Schema as JSONAPISchema

from app.api.helpers.utilities import dasherize


class SocialLinkSchema(Schema):
    name = fields.String(required=True)
    link = fields.String(required=True)


class ExhibitorSchema(JSONAPISchema):
    class Meta:

        type_ = 'exhibitor'
        self_view = 'v1.exhibitor_detail'
        self_view_kwargs = {'id': '<id>'}
        inflect = dasherize

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    url = fields.Url(allow_none=True)
    position = fields.Integer(allow_none=True, default=0)
    logo_url = fields.Url(allow_none=True)
    banner_url = fields.Url(allow_none=True)
    video_url = fields.Url(allow_none=True)
    slides_url = fields.Url(allow_none=True)
    social_links = fields.Nested(SocialLinkSchema, many=True)
    event = Relationship(
        self_view='v1.exhibitor_event',
        self_view_kwargs={'id': '<id>'},
        related_view='v1.event_detail',
        related_view_kwargs={'exhibitor_id': '<id>'},
        schema='EventSchemaPublic',
        type_='event',
    )
