"""Add composer to media

Revision ID: 25a58a1c2898
Revises: fa23fc78f0cc
Create Date: 2020-12-13 19:56:39.087807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25a58a1c2898'
down_revision = 'fa23fc78f0cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('media', sa.Column('composer', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('media', 'composer')
    # ### end Alembic commands ###