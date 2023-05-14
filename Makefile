runlocal:
	docker-compose -f docker-compose.dev.yaml up --build

shell:
	docker-compose -f docker-compose.dev.yaml exec web bash