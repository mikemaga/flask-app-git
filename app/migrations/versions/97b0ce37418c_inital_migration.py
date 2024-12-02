"""inital_migration

Revision ID: 97b0ce37418c
Revises: bb0caa3e71b7
Create Date: 2024-11-26 00:30:48.723030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97b0ce37418c'
down_revision = 'bb0caa3e71b7'
branch_labels = None
depends_on = None



def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('top_competitions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ranking_class', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('unique_tournament_slug', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('unique_tournament_primary_color_hex', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_secondary_color_hex', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_category_name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_category_slug', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_category_sport_name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_category_sport_slug', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_category_sport_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_category_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_category_flag', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_category_alpha2', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_user_count', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('unique_tournament_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('unique_tournament_display_inverse_home_away_teams', sa.Boolean(), nullable=False))
        batch_op.alter_column('id',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('total_teams',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.alter_column('year',
               existing_type=sa.BIGINT(),
               type_=sa.String(),
               nullable=False)
        batch_op.alter_column('type',
               existing_type=sa.BIGINT(),
               type_=sa.String(),
               nullable=False)
        batch_op.alter_column('ranking',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               nullable=False)
        batch_op.alter_column('points',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               nullable=False)
        batch_op.alter_column('country_alpha2',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               nullable=False)
        batch_op.drop_column('uniquetournament_category_sport_name')
        batch_op.drop_column('uniquetournament_category_sport_slug')
        batch_op.drop_column('uniquetournament_slug')
        batch_op.drop_column('uniquetournament_category_slug')
        batch_op.drop_column('uniquetournament_primarycolorhex')
        batch_op.drop_column('uniquetournament_name')
        batch_op.drop_column('rowname')
        batch_op.drop_column('uniquetournament_displayinversehomeawayteams')
        batch_op.drop_column('uniquetournament_category_id')
        batch_op.drop_column('uniquetournament_secondarycolorhex')
        batch_op.drop_column('rankingclass')
        batch_op.drop_column('uniquetournament_category_sport_id')
        batch_op.drop_column('uniquetournament_category_name')
        batch_op.drop_column('uniquetournament_usercount')
        batch_op.drop_column('uniquetournament_id')
        batch_op.drop_column('uniquetournament_category_alpha2')
        batch_op.drop_column('uniquetournament_category_flag')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('top_competitions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uniquetournament_category_flag', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_category_alpha2', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_id', sa.BIGINT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_usercount', sa.BIGINT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_category_name', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_category_sport_id', sa.BIGINT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('rankingclass', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_secondarycolorhex', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_category_id', sa.BIGINT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_displayinversehomeawayteams', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('rowname', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_name', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_primarycolorhex', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_category_slug', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_slug', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_category_sport_slug', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uniquetournament_category_sport_name', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.alter_column('country_alpha2',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('points',
               existing_type=sa.Integer(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.alter_column('ranking',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               nullable=True)
        batch_op.alter_column('type',
               existing_type=sa.String(),
               type_=sa.BIGINT(),
               nullable=True)
        batch_op.alter_column('year',
               existing_type=sa.String(),
               type_=sa.BIGINT(),
               nullable=True)
        batch_op.alter_column('total_teams',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               nullable=True,
               autoincrement=True)
        batch_op.drop_column('unique_tournament_display_inverse_home_away_teams')
        batch_op.drop_column('unique_tournament_id')
        batch_op.drop_column('unique_tournament_user_count')
        batch_op.drop_column('unique_tournament_category_alpha2')
        batch_op.drop_column('unique_tournament_category_flag')
        batch_op.drop_column('unique_tournament_category_id')
        batch_op.drop_column('unique_tournament_category_sport_id')
        batch_op.drop_column('unique_tournament_category_sport_slug')
        batch_op.drop_column('unique_tournament_category_sport_name')
        batch_op.drop_column('unique_tournament_category_slug')
        batch_op.drop_column('unique_tournament_category_name')
        batch_op.drop_column('unique_tournament_secondary_color_hex')
        batch_op.drop_column('unique_tournament_primary_color_hex')
        batch_op.drop_column('unique_tournament_slug')
        batch_op.drop_column('unique_tournament_name')
        batch_op.drop_column('ranking_class')

    # ### end Alembic commands ###
