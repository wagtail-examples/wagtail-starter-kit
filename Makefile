# Makefile for Docker Compose commands

# --- Un-comment to suite your needs --- #

# Default SQLite Database
# DC = docker compose -f compose.yaml

# MySQL Database
# DC = docker compose -f compose.yaml -f compose.mysql.override.yaml

# PostgreSQL Database
DC = docker compose -f compose.yaml -f compose.postgresql.override.yaml

# Default target
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo " Docker Compose commands"
	@echo "  build      Build the Docker containers"
	@echo "  up         Start the Docker containers"
	@echo "  down       Stop and remove the Docker containers"
	@echo "  destroy    Stop and remove the Docker containers, networks, and volumes"
	@echo "  run		Run the Django development server"
	@echo ""
	@echo " Container commands"
	@echo "  migrate    Run Django migrations"
	@echo "  superuser  Create a superuser"
	@echo "  restoredb  Restore the database from a backup"
	@echo "  sh			Execute a command in a running container"
	@echo "  restart    Restart the containers"
	@echo ""
	@echo " Quckstart"
	@echo "  quickstart Build, start, and run the containers"
	@echo ""

# Build the containers
.PHONY: build
build:
	$(DC) build

# Start the containers
.PHONY: up
up:
	$(DC) up -d

# Stop and remove containers, networks, and volumes
.PHONY: down
down:
	$(DC) down

# Restart the containers
.PHONY: restart
restart:
	$(DC) restart

# Execute a command in a running container
.PHONY: sh
sh:
	$(DC) exec app bash

# Run the Django development server
.PHONY: run
run:
	$(DC) exec app python manage.py runserver 0.0.0.0:8000

# Stop and remove the Docker containers, networks, and volumes
.PHONY: destroy
destroy:
	$(DC) down -v

# Run migrations
.PHONY: migrate
migrate:
	$(DC) exec app python manage.py migrate

# Create a superuser
.PHONY: superuser
superuser:
	$(DC) exec app python manage.py createsuperuser

# Qucikstart
.PHONY: quickstart
quickstart: build up migrate run
