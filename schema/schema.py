from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene import relay
import graphene
from . import schema_department
from . import schema_role
from . import schema_employee


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    employee = relay.Node.Field(schema_employee.Employee)
    employee_list = SQLAlchemyConnectionField(schema_employee.Employee)
    department = relay.Node.Field(schema_department.Department)
    department_list = SQLAlchemyConnectionField(schema_department.Department)
    role = relay.Node.Field(schema_role.Role)
    role_list = SQLAlchemyConnectionField(schema_role.Role)


schema = graphene.Schema(query=Query)