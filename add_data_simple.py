import sqlalchemy as sa
from sqlalchemy_continuum import versioning_manager

from database import session_scope, query_local_db, engine
from models import Animal


def check_if_object_updated(changed_object):
    obj_dict = changed_object.__dict__.copy()
    obj_dict.pop('_sa_instance_state', None)
    for column_name in obj_dict.keys():
        if sa.orm.attributes.get_history(changed_object, column_name)[2]:
            return True
    return False


def perform_cud_operation(changed_object, session, op_type=1, user_info='shashwat'):
    update_or_insert_done = False
    if (op_type ==1 and check_if_object_updated(changed_object)) or op_type == 0:
        session.add(changed_object)
        update_or_insert_done = True
    elif op_type == 2:
        session.delete(changed_object)

    if op_type == 2 or update_or_insert_done:
        uow = versioning_manager.unit_of_work(session)
        tx = uow.create_transaction(session)
        tx.meta = {'user_info': user_info}
        session.commit()


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
            animal.name = 'some_name'+'_e'*j
            perform_cud_operation(animal, session, 1)
        animal.name = animal.name
        perform_cud_operation(animal, session, 1)


def delete_animal():
    with session_scope() as session:
        animal = session.query(Animal).filter_by(id=1).one()
        perform_cud_operation(animal, session, 2)


def perform_multiple_operations():
    add_and_update_animal()
    #  delete_animal()

if __name__ == '__main__':
    perform_multiple_operations()

