"""Renaming students to scholars

Revision ID: b91a1f2d5f7d
Revises: 791279dd0760
Create Date: 2023-12-05 14:20:43.574284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b91a1f2d5f7d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
