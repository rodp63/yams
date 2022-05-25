REPOSITORY = rodp63


.PHONY: build-image
build-image:
	-docker build . --tag $(REPOSITORY)/yans:latest


.PHONY: upload-image
upload-image:
	-docker push $(REPOSITORY)/yans:latest


.PHONY: lint
lint:
	-black .
