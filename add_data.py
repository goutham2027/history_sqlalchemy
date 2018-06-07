import uuid

from sqlalchemy_continuum import versioning_manager

from database import session_scope, query_local_db
from models import Animal


def perform_cud_operation(changed_object, session,  op_type=1, user_info='shashwat'):
    if op_type !=1:
        if op_type == 0:
            session.add(changed_object)
        else:
            session.delete(changed_object)
        session.commit()
        query = "SELECT transaction_id from {}_version where id={} and operation_type={}".format(changed_object.__tablename__, changed_object.id, op_type)
        trans_id = query_local_db(query)

    elif op_type == 1:
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
        animal_name = 'some_name'
        animal_dict = {
                'name': animal_name
                }
        animal = Animal(**animal_dict)
        perform_cud_operation(animal, session, 0)
        animal = session.query(Animal).filter_by(id=animal.id).one()

        for i in range(0,2):
            j = i+1
            temp_data = animal
            animal.name = 'some_name'+'_e'*j
            import ipdb; ipdb.set_trace()
            perform_cud_operation(animal, session, 1)


def delete_animal():
    with session_scope() as session:
        animal = session.query(Animal).filter_by(id=1).one()
        perform_cud_operation(animal, session, 2)


def perform_multiple_operations():
    add_and_update_animal()
    delete_animal()

if __name__ == '__main__':
    perform_multiple_operations()

