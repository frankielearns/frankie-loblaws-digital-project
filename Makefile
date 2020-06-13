SHELL := /bin/bash -e

PROJECT_NAME = frankie-loblaws
IMAGES_DIRECTORY = $(PWD)
.PHONY: *

export IMAGES_DIRECTORY
help: ## This help message
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

build: ## Build Docker Image
	docker build -t $(PROJECT_NAME):latest .

compare-images: build ## Builds and runs the Docker image
	docker run -it -v $(IMAGES_DIRECTORY):/code $(PROJECT_NAME):latest
