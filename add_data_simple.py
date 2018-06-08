from sqlalchemy_continuum import versioning_manager

from database import session_scope, query_local_db
from models import Animal


def perform_cud_operation(changed_object, session,  op_type=1, user_info='shashwat'):
        session.add(changed_object)
        uow = versioning_manager.unit_of_work(session)
        tx = uow.create_transaction(session)
        tx.meta = {'user_id': 'shashwat@beautifulcode.in'}
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
            temp_data = animal
            animal.name = 'some_name'+'_e'*j
            perform_cud_operation(animal, session, 1)


# def delete_animal():
    # with session_scope() as session:
        # animal = session.query(Animal).filter_by(id=1).one()
        # perform_cud_operation(animal, session, 2)


def perform_multiple_operations():
    add_and_update_animal()
    # delete_animal()

if __name__ == '__main__':
    perform_multiple_operations()

