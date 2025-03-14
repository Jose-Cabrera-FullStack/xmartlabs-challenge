run:
	docker-compose -f docker/docker-compose.yml up --force-recreate --build

test:
	docker-compose -f docker/docker-compose.yml exec app pytest

add-migration:
	@read -p  "Enter the name of the migration: " name; \
	docker-compose -f docker/docker-compose.yml exec app bash -c "alembic revision --autogenerate -m \"$$name\""

migrate:
	@echo "Migrating database"
	docker-compose -f docker/docker-compose.yml exec app bash -c "alembic upgrade head"
