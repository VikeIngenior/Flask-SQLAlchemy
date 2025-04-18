"""Delete fake_column from Comment

Revision ID: c859f32f3cd1
Revises: 1a50d24cfff7
Create Date: 2025-04-18 00:06:18.328527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c859f32f3cd1'
down_revision: Union[str, None] = '1a50d24cfff7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'fake_column')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('fake_column', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
