FROM node:22-bullseye-slim AS client-builder

WORKDIR /app
COPY . /app

RUN npm install && npm cache clean --force

ENV PATH=/app/node_modules/.bin/:$PATH
ENV NODE_PATH=/app/node_modules

RUN npm run build

# define an alias for the specific python version used in this file.
FROM python:3.11.9-slim-bullseye AS python

# Python build stage
FROM python AS python-build-stage

ARG BUILD_ENVIRONMENT=production

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

# Requirements are installed here to ensure they will be cached.
COPY ./requirements .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt


# Python 'run' stage
FROM python AS python-run-stage

ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV BUILD_ENV=${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN addgroup --system django \
  && adduser --system --ingroup django django


# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/


COPY --chown=django:django ./docker/production/django/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY --chown=django:django ./docker/setup /setup
RUN chmod +x /setup

COPY --chown=django:django ./docker/production/django/ui/start /start-ui
RUN chmod +x /start-ui

COPY --chown=django:django ./docker/production/django/api/start /start-api
RUN chmod +x /start-api

COPY --chown=django:django ./docker/production/django/celery/worker/start /start-worker
RUN chmod +x /start-worker

COPY --chown=django:django ./docker/production/django/celery/beat/start /start-scheduler
RUN chmod +x /start-scheduler

COPY ./docker/production/django/celery/flower/start /start-flower
RUN chmod +x /start-flower

# copy application code to WORKDIR
COPY --from=client-builder --chown=django:django ${APP_HOME} ${APP_HOME}
RUN mkdir -p ${APP_HOME}/staticfiles
RUN chown -R django:django ${APP_HOME}

USER django

RUN DATABASE_URL="" \
  REDIS_BASE_URL="" \
  DJANGO_SECRET_KEY="i18n" \
  DJANGO_SETTINGS_MODULE="config.settings.production.base" \
  python manage.py compilemessages

RUN DATABASE_URL="" \
  REDIS_BASE_URL="" \
  DJANGO_SECRET_KEY="i18n" \
  DJANGO_SETTINGS_MODULE="config.settings.production.base" \
  python manage.py collectstatic --no-input

ENTRYPOINT ["/entrypoint"]
