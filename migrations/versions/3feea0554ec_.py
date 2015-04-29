"""empty message

Revision ID: 3feea0554ec
Revises: 192212d60a57
Create Date: 2015-04-29 14:42:42.781017

"""

# revision identifiers, used by Alembic.
revision = '3feea0554ec'
down_revision = '192212d60a57'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answer_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['answer_id'], ['answer.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vote')
    ### end Alembic commands ###