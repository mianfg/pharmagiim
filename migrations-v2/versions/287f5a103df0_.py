"""empty message

Revision ID: 287f5a103df0
Revises: 
Create Date: 2021-01-07 17:53:06.109467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '287f5a103df0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empleados',
    sa.Column('dni', sa.String(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('puesto', sa.String(), nullable=True),
    sa.Column('sueldo', sa.String(), nullable=True),
    sa.Column('duracion', sa.String(), nullable=True),
    sa.Column('fechaInicio', sa.String(), nullable=True),
    sa.Column('actividad', sa.Enum('ACTIVO', 'INACTIVO', name='empleadoestados070101'), nullable=True),
    sa.PrimaryKeyConstraint('dni')
    )
    op.create_table('proyecto',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('descripcion', sa.String(), nullable=True),
    sa.Column('categoria', sa.String(), nullable=True),
    sa.Column('estado', sa.Enum('INICIAL', 'EN_PROCESO', 'EN_PAUSA', 'FINALIZADO', 'FRACASO', name='proyectoestados070101'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('evaluaciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('dni', sa.String(), nullable=False),
    sa.Column('fechaIni', sa.String(), nullable=True),
    sa.Column('fechaFin', sa.String(), nullable=True),
    sa.Column('conclusion', sa.String(), nullable=True),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dni'], ['empleados.dni'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('descripcion', sa.String(), nullable=True),
    sa.Column('cod_distribucion', sa.String(), nullable=True),
    sa.Column('precio_venta', sa.Float(), nullable=True),
    sa.Column('origen', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['origen'], ['proyecto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proceso_productivo',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('descripcion', sa.String(), nullable=True),
    sa.Column('fecha_inicio', sa.Date(), nullable=True),
    sa.Column('fecha_fin', sa.Date(), nullable=True),
    sa.Column('ctd_producida', sa.Float(), nullable=True),
    sa.Column('fabrica', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['fabrica'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('proceso_productivo')
    op.drop_table('producto')
    op.drop_table('evaluaciones')
    op.drop_table('proyecto')
    op.drop_table('empleados')
    # ### end Alembic commands ###