# Simple RSS Reader

A simple YAML driven RSS reader.

![homepage](home.png)
![expanded-view](expanded.png)

This assumes you're running the app/container locally or on a private network. **do not deploy to the public-facing internet particularly if using the filebrowser in the Helm chart**.

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

## Deploying to Kubernetes

In `chart/` create a `values.yaml` file:

```yaml
sitename: "reader.freeipad.internal"
configpath: "/opt"
feedpath: "/opt/feeds.yaml"
feedshostpath: "{YOUR_LOCAL_DIR_HOUSING_FEEDS_YAML}" #This goes into a hostPath PersistentVolume
fqdn: "reader.freeipad.internal"
ingress:
  rules:
    - host: "{{ .Values.fqdn }}"
      http:
        paths:
          - path: /
            pathType: Exact
            backend:
              service:
                name:  rss-reader-service
                port:
                  number: 80
```
customizing with your feeds and `sitename`, and updating the ingress, and apply:

```bash
helm install rss-reader ./
```
then navigate to your `fqdn` (assuming DNS is already configured for your Ingress).

If you'd like to edit the `feeds.yaml` from your browser, in your `values.yaml` set `filebrowser` to `enabled`. After deployment, the file can be edited from your browser using the `/browser` URI, using the default credential for filebrowser, `admin/admin` which will have RW access to anything in the directory containing your feeds.yaml. 

**Note** This assumes you're running the app/container locally or exposed on a private network. **do not deploy to the public-facing internet particularly if using the filebrowser in the Helm chart**.

## Configuration

Add URLs to a YAML file:

```yaml
feeds:
- "https://some.site/rss"
```

This app uses `apscheduler` to update the feeds in the UI periodically (~1 Minute).