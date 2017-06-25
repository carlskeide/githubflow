# coding=utf-8
from os import environ as env


class FlaskConfig(object):
    DEBUG = False


class CeleryConfig(object):
    DEBUG = False

    BROKER_URL = env.get("CELERY_BROKER") or "redis://redis"

    CELERY_CREATE_MISSING_QUEUES = True

    CELERY_TASK_SERIALIZER = "json"
    CELERY_ACCEPT_CONTENT = ["json"]
    CELERY_RESULT_SERIALIZER = "json"


# Application
TARGET_BRANCH = "master"
RELEASE_PATTERN = r"^\d{8}\.\d+$"

# Secrets
WEBHOOK_SECRET = env.get("GITHUB_WEBHOOK_SECRET")
GITHUB_TOKEN = env.get("GITHUB_TOKEN")
SLACK_WEBHOOK = env.get("SLACK_WEBHOOK")