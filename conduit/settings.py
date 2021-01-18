# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from datetime import timedelta


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('CONDUIT_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_HEADER_PREFIX = 'Token'
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:4100',
        'http://localhost:4100',
        'http://0.0.0.0:8000',
        'http://localhost:8000',
        'http://0.0.0.0:4200',
        'http://localhost:4200',
        'http://0.0.0.0:4000',
        'http://localhost:4000',
        'http://0.0.0.0:8080',
        'https://0.0.0.0:8080',
        'https://projetdevopsfront.netlify.app/',
    ]
    JWT_HEADER_TYPE = 'Token'


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgres://auppxzvqwsyije:8fb06fca4d0ef56a7ef181fb38718c0320108b7f1890347ea712ed908fef359a@ec2-54-234-28-165.compute-1.amazonaws.com:5432/dd0ltlic7j2vjf')


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgres://auppxzvqwsyije:8fb06fca4d0ef56a7ef181fb38718c0320108b7f1890347ea712ed908fef359a@ec2-54-234-28-165.compute-1.amazonaws.com:5432/dd0ltlic7j2vjf')
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(10 ** 6)


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgres://auppxzvqwsyije:8fb06fca4d0ef56a7ef181fb38718c0320108b7f1890347ea712ed908fef359a@ec2-54-234-28-165.compute-1.amazonaws.com:5432/dd0ltlic7j2vjf')
    # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    BCRYPT_LOG_ROUNDS = 4
