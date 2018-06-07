"""add user_info column

Revision ID: d9bb0c6cbea0
Revises: 279051ff19cd
Create Date: 2018-06-07 17:01:04.590268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9bb0c6cbea0'
down_revision = '279051ff19cd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('transaction', sa.Column('user_info', sa.Text))


def downgrade():
    op.drop_column('transaction', 'user_info')
