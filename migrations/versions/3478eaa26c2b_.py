"""empty message

Revision ID: 3478eaa26c2b
Revises: e3447d270d12
Create Date: 2023-08-26 15:17:22.039057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3478eaa26c2b'
down_revision = 'e3447d270d12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wish',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('rarity', sa.String(length=150), nullable=True),
    sa.Column('size', sa.String(length=150), nullable=True),
    sa.Column('release_date', sa.String(length=200), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wish')
    # ### end Alembic commands ###
