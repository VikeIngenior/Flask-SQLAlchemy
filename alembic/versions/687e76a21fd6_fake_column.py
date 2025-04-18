"""fake column

Revision ID: 687e76a21fd6
Revises: ea120b6c3053
Create Date: 2025-04-17 23:54:10.709227

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '687e76a21fd6'
down_revision: Union[str, None] = 'ea120b6c3053'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
