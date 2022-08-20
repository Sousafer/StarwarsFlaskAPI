"""empty message

Revision ID: 5914aef6ecfd
Revises: df85296b505d
Create Date: 2022-08-20 13:35:45.854888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5914aef6ecfd'
down_revision = 'df85296b505d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('characters')
    # ### end Alembic commands ###