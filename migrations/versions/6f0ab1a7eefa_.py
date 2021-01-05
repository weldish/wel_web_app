"""empty message

Revision ID: 6f0ab1a7eefa
Revises: 7e88d27d459a
Create Date: 2021-01-02 16:50:23.476514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f0ab1a7eefa'
down_revision = '7e88d27d459a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('status', sa.String(length=20), nullable=False))
    op.alter_column('user', 'Usertype',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'Usertype',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
    op.drop_column('user', 'status')
    # ### end Alembic commands ###