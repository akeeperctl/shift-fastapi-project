"""job title unique

Revision ID: a8f927a55329
Revises: 15d0e61d70a3
Create Date: 2023-06-22 18:04:38.437166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8f927a55329'
down_revision = '15d0e61d70a3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_job_title', table_name='job')
    op.create_index(op.f('ix_job_title'), 'job', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_job_title'), table_name='job')
    op.create_index('ix_job_title', 'job', ['title'], unique=False)
    # ### end Alembic commands ###