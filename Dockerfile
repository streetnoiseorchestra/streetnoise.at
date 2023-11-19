# Use an official Python runtime as a parent image
FROM docker.io/library/python:3.11
LABEL maintainer="Casey Link"

ARG BUILD_DATE=unknown
ARG VERSION=unknown


# Install nodejs
RUN set -e; \
  echo "deb https://deb.nodesource.com/node_20.x buster main" > /etc/apt/sources.list.d/nodesource.list; \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -; \
  apt-get update; \
  apt-get install -yqq nodejs; \
  pip install -U pip; \
  npm i -g npm@^20; \
  rm -rf /var/lib/apt/lists/*

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production

RUN pip install --upgrade pip
COPY requirements.frozen.txt /code/requirements.frozen.txt
# Install any needed packages specified in requirements.txt
RUN set -ex; pip install -r /code/requirements.frozen.txt; pip install gunicorn

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

RUN npm install --omit=dev

RUN set -e; \
    COLLECT_STATIC_OVERRIDE=True python manage.py collectstatic --noinput;

RUN groupadd -r -g 3993 cms && useradd --uid 3993 --gid 3993 cms
RUN chown -R cms /code
USER cms
RUN mkdir /code/media

EXPOSE 8000
CMD exec gunicorn streetnoise.wsgi:application --bind 0.0.0.0:8000 --workers 3


LABEL org.opencontainers.image.version=${VERSION}
LABEL org.opencontainers.image.created=${BUILD_DATE}
LABEL org.opencontainers.image.documentation="https://github.com/streetnoiseorchestra/streetnoise.at"
LABEL org.opencontainers.image.source="https://github.com/streetnoiseorchestra/streetnoise.at"
LABEL org.opencontainers.image.vendor="StreetNoise Orchestra"
