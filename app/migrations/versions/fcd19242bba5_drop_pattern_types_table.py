"""Drop pattern types table

Revision ID: fcd19242bba5
Revises: e118cf5215ad
Create Date: 2025-04-09 19:31:08.737172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcd19242bba5'
down_revision = 'e118cf5215ad'
branch_labels = None
depends_on = None


def upgrade():
    # Drop Pattern Types table
    op.drop_table('pattern_types')


def downgrade():
    # Create Pattern Types table
    # Pulled from Revision ID: 4ded6755b829
    op.create_table('pattern_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pattern_type', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'manufacturers', ['id'])
    op.create_unique_constraint(None, 'racquets', ['id'])
