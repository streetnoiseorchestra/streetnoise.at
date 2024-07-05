FROM docker.io/library/python:3.11
LABEL maintainer="Casey Link"

ARG BUILD_DATE=unknown
ARG VERSION=unknown


RUN set -e; \
  DEB_CODENAME=$(grep -oP '^VERSION_CODENAME=\K.*' /etc/os-release); \
  echo "deb https://deb.nodesource.com/node_20.x $DEB_CODENAME main" > /etc/apt/sources.list.d/nodesource.list; \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -; \
  apt-get update; \
  apt-get install -yqq nodejs; \
  pip install -U pip; \
  npm i -g npm@^10; \
  rm -rf /var/lib/apt/lists/*


RUN set -e; \
  apt-get update; \
  apt-get install -yqq libmagickwand-dev imagemagick; \
  rm -rf /var/lib/apt/lists/*

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production

RUN pip install --upgrade pip
COPY requirements.frozen.txt /code/requirements.frozen.txt
RUN set -ex; pip install -r /code/requirements.frozen.txt; pip install gunicorn wand

COPY . /code/
WORKDIR /code/

RUN set -e; \
    npm install; \
    pwd; \
    ls -al; \
    npm run build; \
    COLLECT_STATIC_OVERRIDE=True python manage.py collectstatic --noinput; \
    rm -rf node_modules ./_*; \
    npm install --omit=dev;

RUN groupadd -r -g 3993 cms && useradd --uid 3993 --gid 3993 cms
RUN chown -R cms /code
USER cms
RUN mkdir /code/media

EXPOSE 8000
CMD exec gunicorn streetnoise.wsgi:application --bind 0.0.0.0:8000 --workers 4


LABEL org.opencontainers.image.version=${VERSION}
LABEL org.opencontainers.image.created=${BUILD_DATE}
LABEL org.opencontainers.image.documentation="https://github.com/streetnoiseorchestra/streetnoise.at"
LABEL org.opencontainers.image.source="https://github.com/streetnoiseorchestra/streetnoise.at"
LABEL org.opencontainers.image.vendor="StreetNoise Orchestra"
