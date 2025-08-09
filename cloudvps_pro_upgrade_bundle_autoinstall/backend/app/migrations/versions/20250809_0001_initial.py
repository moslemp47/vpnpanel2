from alembic import op
import sqlalchemy as sa

revision = '20250809_0001_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('is_verified', sa.Boolean, default=False),
        sa.Column('twofa_secret', sa.String(64)),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )
    op.create_table('sessions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete="CASCADE")),
        sa.Column('user_agent', sa.String(255)),
        sa.Column('ip', sa.String(45)),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

def downgrade():
    op.drop_table('sessions')
    op.drop_table('users')
