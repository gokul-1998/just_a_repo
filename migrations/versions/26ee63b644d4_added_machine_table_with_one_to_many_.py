"""added machine table with one to many relationship

Revision ID: 26ee63b644d4
Revises: 760b2136ddb2
Create Date: 2024-11-16 15:16:01.119843

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "26ee63b644d4"
down_revision = "760b2136ddb2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=80), nullable=False),
        sa.Column("password", sa.String(length=120), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_users_username"), ["username"], unique=True
        )

    op.create_table(
        "machines",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("machine_id", sa.String(length=120), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("machines", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_machines_machine_id"), ["machine_id"], unique=True
        )
        batch_op.create_index(
            batch_op.f("ix_machines_user_id"), ["user_id"], unique=False
        )

    op.drop_table("user")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("username", sa.VARCHAR(length=80), nullable=False),
        sa.Column("password", sa.VARCHAR(length=120), nullable=False),
        sa.Column("machine_id", sa.VARCHAR(length=120), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("machine_id"),
        sa.UniqueConstraint("username"),
    )
    with op.batch_alter_table("machines", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_machines_user_id"))
        batch_op.drop_index(batch_op.f("ix_machines_machine_id"))

    op.drop_table("machines")
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_users_username"))

    op.drop_table("users")
    # ### end Alembic commands ###
