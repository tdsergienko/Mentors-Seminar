TODO_IMAGE = todo-service
SHORTURL_IMAGE = shorturl-service

TODO_CONTAINER = todo-container
SHORTURL_CONTAINER = shorturl-container

TODO_PORT = 8000
SHORTURL_PORT = 8001

TODO_VOLUME = todo_data
SHORTURL_VOLUME = shorturl_data

build-todo:
	docker build -t $(TODO_IMAGE) ./todo-service

build-shorturl:
	docker build -t $(SHORTURL_IMAGE) ./shorturl-service

build: build-todo build-shorturl

volumes:
	docker volume create $(TODO_VOLUME)
	docker volume create $(SHORTURL_VOLUME)

run-todo:
	docker run -d \
		--name $(TODO_CONTAINER) \
		-p $(TODO_PORT):80 \
		-v $(TODO_VOLUME):/app/data \
		$(TODO_IMAGE)

run-shorturl:
	docker run -d \
		--name $(SHORTURL_CONTAINER) \
		-p $(SHORTURL_PORT):80 \
		-v $(SHORTURL_VOLUME):/app/data \
		$(SHORTURL_IMAGE)

run: volumes run-todo run-shorturl

stop:
	-docker stop $(TODO_CONTAINER) $(SHORTURL_CONTAINER)
	-docker rm $(TODO_CONTAINER) $(SHORTURL_CONTAINER)

clean:
	-docker volume rm $(TODO_VOLUME) $(SHORTURL_VOLUME)

test-todo:
	pytest -v todo-service/tests/tests.py

test-shorturl:
	pytest -v shorturl-service/tests/tests.py

test: test-todo test-shorturl

up: stop build run

down: stop clean
