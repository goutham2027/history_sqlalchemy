import uuid

from sqlalchemy_continuum import versioning_manager

from database import session_scope, query_local_db
from models import Animal


def perform_cud_operation(changed_object, session, op_type=1, user_info='gp'):
    if op_type !=1:
        if op_type == 0:
            session.add(changed_object)
        elif op_type == 2:
            session.delete(changed_object)
        session.commit()
        query = "SELECT transaction_id from {}_version where id={} and operation_type={}".format(changed_object.__tablename__, changed_object.id, op_type)
        trans_id = query_local_db(query)

    else:
        random_string = uuid.uuid4().hex
        changed_object.uuids = random_string
        session.add(changed_object)
        session.commit()
        query = "SELECT transaction_id from {}_version where id={} and uuids='{}'".format(changed_object.__tablename__, changed_object.id, random_string)
        trans_id = query_local_db(query)

    query = "update transaction set user_info = '{}', remote_addr = NULL where id={}".format(user_info, trans_id.first()[0])
    query_local_db(query)


def add_and_update_animal():
    with session_scope() as session:
        animal = session.query(Animal).filter_by(id=1).one()
        for i in range(0,2):
            j = i+1
            animal.name = 'different_name'+'_1'*j
            perform_cud_operation(animal, session, 1)


def perform_multiple_operations():
    add_and_update_animal()

if __name__ == '__main__':
   perform_multiple_operations()
