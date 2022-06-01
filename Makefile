REPOSITORY = rodp63


.PHONY: build-image
build-image:
	-docker build . --tag $(REPOSITORY)/yams:latest


.PHONY: upload-image
upload-image:
	-docker push $(REPOSITORY)/yams:latest


.PHONY: lint
lint:
	-black .
