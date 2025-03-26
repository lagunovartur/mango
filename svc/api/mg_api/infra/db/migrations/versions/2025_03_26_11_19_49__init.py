"""init

Revision ID: 08e129ceba12
Revises: 9236448c0c6b
Create Date: 2025-03-26 11:19:49.819423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08e129ceba12'
down_revision = '9236448c0c6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('message',
    sa.Column('chat_id', sa.UUID(), nullable=False),
    sa.Column('sender_id', sa.UUID(), nullable=False),
    sa.Column('text', sa.String(length=500), nullable=False),
    sa.Column('id', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_chat_id'), 'message', ['chat_id'], unique=False)
    op.create_index(op.f('ix_message_sender_id'), 'message', ['sender_id'], unique=False)
    op.create_table('user_chat',
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('chat_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'chat_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_chat')
    op.drop_index(op.f('ix_message_sender_id'), table_name='message')
    op.drop_index(op.f('ix_message_chat_id'), table_name='message')
    op.drop_table('message')
    op.drop_table('user')
    op.drop_table('chat')
    # ### end Alembic commands ###
