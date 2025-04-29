.PHONY: clean help alembic-init alembic-migrate alembic-upgrade alembic-revision clean-versions

SHELL=/bin/bash

alembic-init:
	alembic init migrations

alembic-migrate:
	alembic migrate

alembic-revision:
	@if [ -z "$(msg)" ]; then \
		echo "Error: Please provide a message using 'make alembic-revision msg=\"your message\"'"; \
		exit 1; \
	fi
	alembic revision --autogenerate -m "$(msg)"

## Upgrade database to latest migration
alembic-upgrade:
	@echo "🔄 Upgrading database to latest migration..."
	@echo "💡 Use this after creating new migrations with 'make alembic-revision'"
	alembic upgrade head
	@echo "✨ Database upgraded successfully"

## Remove Python cache files
clean:
	@echo "🧹 Cleaning Python cache files..."
	find . -name "__pycache__" -type d -exec rm -r {} \+
	@echo "✨ Clean completed"

## Remove all migration version files
clean-versions:
	@echo "🧹 Cleaning migration versions..."
	find migrations/versions -name "*.py" -type f -delete
	@echo "✨ Migration versions cleaned"

## Display help information
help:
	@echo "Available commands:"
	@echo "  make clean        - Remove Python cache files"
	@echo "  make clean-versions - Remove all migration version files"
	@echo "  make help         - Display this help information"
	@echo "  make alembic-init - Initialize Alembic migrations"
	@echo "  make alembic-migrate - Run migrations"
	@echo "  make alembic-revision msg=\"your message\" - Create a new migration with custom message"
	@echo "  make alembic-upgrade - Upgrade database to latest migration (use after creating new migrations)"

# Default target
.DEFAULT_GOAL := help