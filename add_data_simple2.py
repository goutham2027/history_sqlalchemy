from sqlalchemy_continuum import versioning_manager

from database import session_scope, query_local_db
from models import Animal


def perform_cud_operation(changed_object, session,  op_type=1, user_info='gp'):
    if op_type != 2:
        session.add(changed_object)
    else:
        session.delete(changed_object)
    uow = versioning_manager.unit_of_work(session)
    tx = uow.create_transaction(session)
    tx.meta = {'user_info': user_info}
    session.commit()


def update_animal():
    with session_scope() as session:
        animal = session.query(Animal).filter_by(id=1).one()
        for i in range(0,2):
            j = i+1
            temp_data = animal
            animal.name = 'different_name'+'_e'*j
            perform_cud_operation(animal, session, 1)


#  def delete_animal():
#      with session_scope() as session:
#          animal = session.query(Animal).filter_by(id=1).one()
#          perform_cud_operation(animal, session, 2)
#

def perform_multiple_operations():
    update_animal()

if __name__ == '__main__':
    perform_multiple_operations()


