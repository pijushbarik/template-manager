"""added success and failure tables

Revision ID: ff92122278f7
Revises: 991fb1677aa1
Create Date: 2019-08-21 20:29:53.674214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff92122278f7'
down_revision = '991fb1677aa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=True)
    op.create_table('template_failure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=64), nullable=True),
    sa.Column('data', sa.BLOB(), nullable=True),
    sa.ForeignKeyConstraint(['company_name'], ['company.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('template_success',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=64), nullable=True),
    sa.Column('data', sa.BLOB(), nullable=True),
    sa.ForeignKeyConstraint(['company_name'], ['company.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_template_name', table_name='template')
    op.drop_table('template')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('template',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('data', sa.BLOB(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_template_name', 'template', ['name'], unique=1)
    op.drop_table('template_success')
    op.drop_table('template_failure')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_table('company')
    # ### end Alembic commands ###