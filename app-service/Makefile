.PHONY: build test image deploy

TAG ?= latest
ENV ?= dev

build:
	pip install --no-cache-dir -r requirements.txt

test: build
	python test_app.py

image:
	docker build -t app-service:$(TAG) .

deploy: image
	echo "deploying app-service:$(TAG) to $(ENV)"

