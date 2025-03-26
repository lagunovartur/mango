"""chat-name

Revision ID: 5dcce4ef7e4f
Revises: 08e129ceba12
Create Date: 2025-03-26 12:56:06.422271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dcce4ef7e4f'
down_revision = '08e129ceba12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('name', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chat', 'name')
    # ### end Alembic commands ###
