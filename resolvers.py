from ariadne import QueryType, MutationType

from models import TestModel

query = QueryType()
mutation = MutationType()
from db_conf import db_session

db = db_session.session_factory()


def resolve_hello(_, info):
    result = db.query(TestModel).first()
    return result.message


def resolve_get_message(_, info, id):
    result = db.query(TestModel).filter(TestModel.id == id).first()
    return result.message


def resolve_create_message(_, info, message):
    test_model = TestModel(message=message)
    db.add(test_model)
    db.commit()
    db.refresh(test_model)
    return test_model


def resolve_update_message(_, info, id, message):
    test_model = db.query(TestModel).filter(TestModel.id == id).first()
    test_model.message = message
    db.commit()
    db.refresh(test_model)
    return test_model


def resolve_delete_message(_, info, id):
    test_model = db.query(TestModel).filter(TestModel.id == id).first()
    db.delete(test_model)
    db.commit()
    return True


query.set_field("hello", resolve_hello)
query.set_field("getMessage", resolve_get_message)
mutation.set_field("createMessage", resolve_create_message)
mutation.set_field("updateMessage", resolve_update_message)
mutation.set_field("deleteMessage", resolve_delete_message)
