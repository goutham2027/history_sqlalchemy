"""add revision tables

Revision ID: 29a955a0f077
Revises: 66d69ace783c
Create Date: 2018-05-30 17:44:00.096870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a955a0f077'
down_revision = '66d69ace783c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animals_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=50), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id'),
    schema='history_sqlalchemy'
    )
    op.create_index(op.f('ix_history_sqlalchemy_animals_version_end_transaction_id'), 'animals_version', ['end_transaction_id'], unique=False, schema='history_sqlalchemy')
    op.create_index(op.f('ix_history_sqlalchemy_animals_version_operation_type'), 'animals_version', ['operation_type'], unique=False, schema='history_sqlalchemy')
    op.create_index(op.f('ix_history_sqlalchemy_animals_version_transaction_id'), 'animals_version', ['transaction_id'], unique=False, schema='history_sqlalchemy')
    op.create_table('transaction',
    sa.Column('issued_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('remote_addr', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['history_sqlalchemy.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='history_sqlalchemy'
    )
    op.create_index(op.f('ix_history_sqlalchemy_transaction_user_id'), 'transaction', ['user_id'], unique=False, schema='history_sqlalchemy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_history_sqlalchemy_transaction_user_id'), table_name='transaction', schema='history_sqlalchemy')
    op.drop_table('transaction', schema='history_sqlalchemy')
    op.drop_index(op.f('ix_history_sqlalchemy_animals_version_transaction_id'), table_name='animals_version', schema='history_sqlalchemy')
    op.drop_index(op.f('ix_history_sqlalchemy_animals_version_operation_type'), table_name='animals_version', schema='history_sqlalchemy')
    op.drop_index(op.f('ix_history_sqlalchemy_animals_version_end_transaction_id'), table_name='animals_version', schema='history_sqlalchemy')
    op.drop_table('animals_version', schema='history_sqlalchemy')
    # ### end Alembic commands ###
