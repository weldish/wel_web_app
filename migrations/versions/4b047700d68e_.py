"""empty message

Revision ID: 4b047700d68e
Revises: a06104c858bf
Create Date: 2021-01-02 16:54:42.718354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b047700d68e'
down_revision = 'a06104c858bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('status', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('usertype', sa.String(length=30), nullable=True))
    op.drop_column('user', 'Usertype')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('Usertype', sa.VARCHAR(length=30), nullable=True))
    op.drop_column('user', 'usertype')
    op.drop_column('user', 'status')
    # ### end Alembic commands ###
