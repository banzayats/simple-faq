"""empty message

Revision ID: 192212d60a57
Revises: ab9187cba15
Create Date: 2015-04-29 11:49:59.101520

"""

# revision identifiers, used by Alembic.
revision = '192212d60a57'
down_revision = 'ab9187cba15'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'title')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('title', mysql.VARCHAR(length=255), nullable=True))
    ### end Alembic commands ###
