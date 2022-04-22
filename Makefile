build-image:
	DOCKER_BUILDKIT=1 docker build -t jmarhee/rss-freeipad-reader:$(TAG) .

publish-image:
	make build-image ; docker push jmarhee/rss-freeipad-reader:$(TAG)

run-all:
	pip3 install -r requirements ; FEED_PATH_YAML=$(FEED_PATH_YAML) SITE_NAME="Running-As-Test" python3 -m flask run --host 0.0.0.0
