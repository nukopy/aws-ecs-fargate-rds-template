# CloudFormation
.PHONY: validate changeset deploy delete
validate:
	aws cloudformation validate-template --template-body file:///$(shell pwd)/templates/stack.yml --profile test-metheus-cfn 

changeset:
	sh ./scripts/deploy.sh changeset

deploy:
	sh ./scripts/deploy.sh deploy

delete:
	sh ./scripts/delete-stack.sh

# Docker Compose
.PHONY: up app db
up:
	docker-compose up

app:
	docker-compose exec app /bin/bash

db:
	docker-compose exec db mysql -umyuser -pmypass mydb
