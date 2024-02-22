REPOSITORY = rodp63


.PHONY: build-image
build-image:
	-docker build . --tag $(REPOSITORY)/yams:latest


.PHONY: upload-image
upload-image:
	-docker push $(REPOSITORY)/yams:latest


.PHONY: lint
lint:
	-isort .
	-black .

.PHONY: run-app
run-app:
	-python app/manage.py runserver


.PHONY: migrate
migrate:
	-python app/manage.py makemigrations
	-python app/manage.py migrate