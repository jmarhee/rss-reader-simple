from python:3.8

ENV SITE_NAME ""
ENV HOST ""
ENV PORT ""
ENV FEED_YAML_PATH ""
# --mount source=feed.yaml,target=/

COPY app.py /app.py
COPY reader.py /reader.py
COPY templates/* /templates/
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt
ENTRYPOINT python -m flask run --host=$HOST --port=$PORT
CMD []
