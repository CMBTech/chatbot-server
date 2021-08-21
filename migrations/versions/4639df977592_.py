"""empty message

Revision ID: 4639df977592
Revises: 531d42f4cebb
Create Date: 2021-08-21 17:22:48.184995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4639df977592'
down_revision = '531d42f4cebb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('category', 'name',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('category', 'name',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    # ### end Alembic commands ###
