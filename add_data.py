import random
import string
import time

from sqlalchemy_continuum import versioning_manager

from database import session_scope, query_stpos_cache
from models import Animal


def add_whodunnit(changed_object, table_name, session):
    t_data = session.query(versioning_manager.transaction_cls).filter_by(id=changed_object.versions.distinct()[-1].transaction_id).one()
    query = "update {} set user_info = '{}', remote_addr = NULL where id={}".format(table_name,'shashwat', t_data.id)
    query_stpos_cache(query)


def add_and_update_user():
    with session_scope() as session:
        animal_name = 'dsgfdsmilewgah'
        animal_dict = {
                'name': animal_name
                }
        animal = Animal(**animal_dict)
        session.add(animal)
        session.commit()
        add_whodunnit(animal, 'transaction', session)
        animal = session.query(Animal).filter_by(id=animal.id).one()

        for i in range(0,2):
            animal.name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            session.add(animal)
            session.commit()
            add_whodunnit(animal, 'transaction', session)


def perform_multiple_operations():
    add_and_update_user()

if __name__ == '__main__':
   perform_multiple_operations()

