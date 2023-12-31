"""remove date emp

Revision ID: 15d0e61d70a3
Revises: 0845a394ba0e
Create Date: 2023-06-22 17:48:09.469593

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '15d0e61d70a3'
down_revision = '0845a394ba0e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_employee_signed_at', table_name='employee')
    op.drop_column('employee', 'last_promotion')
    op.drop_column('employee', 'next_promotion')
    op.drop_column('employee', 'signed_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('signed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('employee', sa.Column('next_promotion', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('employee', sa.Column('last_promotion', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.create_index('ix_employee_signed_at', 'employee', ['signed_at'], unique=False)
    # ### end Alembic commands ###
