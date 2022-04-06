# Simple RSS Reader

A simple YAML driven RSS reader.

## Setup

Build the Docker image:

```bash
docker build -t rss-reader .
```

or pull `jmarhee/rss-freeipad-reader` from DockerHub, and run the container:

```bash
docker run -d \
--name rss-reader \
-e PORT=8888 \
-e HOST=127.0.0.1 \
-e FEED_YAML_PATH=${YOUR_YAML_FILE} \
-e SITE_NAME=${WHATEVER_DISPLAYED_IN_HEADER} \
--mount type=bind,source=$(pwd)/feeds.yaml,target=/opt/feeds.yaml \
rss-reader
```

## Configuration

Add URLs to a YAML file:

```yaml
feeds:
- "https://some.site/rss"
```

and on the next page load, the new feed will be available.
