"""Add parameters for movies

Revision ID: 52c28508acf0
Revises: 84be2faa347e
Create Date: 2021-02-13 13:30:54.335350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52c28508acf0'
down_revision = '84be2faa347e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('media', sa.Column('movie_director', sa.String(), nullable=True))
    op.add_column('media', sa.Column('production_company', sa.String(), nullable=True))
    op.add_column('media', sa.Column('staring', sa.String(), nullable=True))
    op.add_column('media', sa.Column('starting_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('media', 'starting_date')
    op.drop_column('media', 'staring')
    op.drop_column('media', 'production_company')
    op.drop_column('media', 'movie_director')
    # ### end Alembic commands ###
