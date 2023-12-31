"""role remove perm col

Revision ID: 126beff21185
Revises: 317ee5b85208
Create Date: 2023-06-23 09:55:05.436481

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '126beff21185'
down_revision = '317ee5b85208'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'permissions')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('permissions', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False, comment="example: [perm1, perm2, perm3]. All perm's is string"))
    # ### end Alembic commands ###
