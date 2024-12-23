"""Initial migration

Revision ID: bc4dffa0d07d
Revises: 
Create Date: 2024-11-25 19:04:09.179735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc4dffa0d07d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    
    with op.batch_alter_table('data', schema=None) as batch_op:
        batch_op.drop_column('uniquetournament_displayinversehomeawayteams')
        batch_op.drop_column('uniquetournament_id')
        batch_op.drop_column('uniquetournament_user_count')
        batch_op.drop_column('uniquetournament_category_alpha2')
        batch_op.drop_column('uniquetournament_category_flag')
        batch_op.drop_column('uniquetournament_category_id')
        batch_op.drop_column('uniquetournament_category_sport_id')
        batch_op.drop_column('uniquetournament_category_sport_slug')
        batch_op.drop_column('uniquetournament_category_sport_name')
        batch_op.drop_column('uniquetournament_category_slug')
        batch_op.drop_column('uniquetournament_category_name')
        batch_op.drop_column('uniquetournament_secondary_color_hex')
        batch_op.drop_column('uniquetournament_primary_color_hex')
        batch_op.drop_column('uniquetournament_slug')
        batch_op.drop_column('unique_tournament_name')
        batch_op.drop_column('ranking_class')
        batch_op.drop_column('row_name')
        batch_op.drop_column('total_teams')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('value', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('key', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
        batch_op.drop_column('standings')
        batch_op.drop_column('team_id')

    op.drop_table('unique_tournament_seasons')
    op.drop_table('competition_standings')
    # ### end Alembic commands ###
