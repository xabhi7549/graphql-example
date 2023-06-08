"""New Migration

Revision ID: a2b05861fae2
Revises: 
Create Date: 2023-06-08 07:27:18.986031

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a2b05861fae2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=True),
                    sa.Column('author', sa.String(), nullable=True),
                    sa.Column('content', sa.String(), nullable=True),
                    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'),
                              nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_post_id'), 'post', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_id'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
