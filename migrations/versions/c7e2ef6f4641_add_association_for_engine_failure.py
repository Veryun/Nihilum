"""add association for engine_failure

Revision ID: c7e2ef6f4641
Revises: 69072bec7cbf
Create Date: 2022-07-31 13:17:58.807889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7e2ef6f4641'
down_revision = '69072bec7cbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('engine_failure_association',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('engine_id', sa.Integer(), nullable=True),
    sa.Column('engine_failure_id', sa.Integer(), nullable=True),
    sa.Column('effect_chance', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['engine_failure_id'], ['engine_failure.id'], ),
    sa.ForeignKeyConstraint(['engine_id'], ['engine.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('engine', 'catastrophic_failure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('engine', sa.Column('catastrophic_failure', sa.VARCHAR(), nullable=False))
    op.drop_table('engine_failure_association')
    # ### end Alembic commands ###