"""add user_info column

Revision ID: c5d1365ead5e
Revises: 7695fca20797
Create Date: 2018-05-31 22:46:06.423368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5d1365ead5e'
down_revision = '7695fca20797'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('transaction', sa.Column('user_info', sa.Text))


def downgrade():
    op.drop_column('transaction', 'user_info')

