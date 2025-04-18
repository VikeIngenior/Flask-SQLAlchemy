"""nothing's done

Revision ID: ea120b6c3053
Revises: 600cd643061d
Create Date: 2025-04-17 23:47:28.229098

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea120b6c3053'
down_revision: Union[str, None] = '600cd643061d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
