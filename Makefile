run:
	docker-compose -f docker/docker-compose.yml up --force-recreate --build

test:
	docker-compose -f docker/docker-compose.yml exec app pytest
