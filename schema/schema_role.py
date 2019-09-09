from database.model_role import ModelRole
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class RoleAttribute:
    name = graphene.String(description='Name of Role')


class Role(SQLAlchemyObjectType, RoleAttribute):
    class Meta:
        model = ModelRole
        interfaces = (relay.Node,)
