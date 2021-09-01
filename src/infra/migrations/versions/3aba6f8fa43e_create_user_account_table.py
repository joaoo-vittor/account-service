"""create user account table

Revision ID: 3aba6f8fa43e
Revises: 
Create Date: 2021-09-01 00:31:44.482545

"""
from alembic import op
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = "3aba6f8fa43e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        Column("id", Integer, primary_key=True),
        Column("user_name", String(100), nullable=False, unique=True),
        Column("email", String(100), nullable=True, unique=True),
        Column("password", String(200), nullable=False),
        Column("active", Boolean, default=True),
        Column("created_at", DateTime(timezone=True), server_default=func.now()),
        Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
    )


def downgrade():
    op.drop_column("users")
