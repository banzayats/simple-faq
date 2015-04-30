# coding: utf-8

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'romscifcuercsdkxjdfaw87erq84xmwehxwqjxri4awxerewatvu76rser2q34534'

SQLALCHEMY_DATABASE_URI = 'mysql://promua_user:pa$$w0rd@localhost/promua'
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = "mwehxwqjxri4awxereaxzcdfvbgcbngrxr"

LANGUAGES = {
    'en': 'English',
    'ru': 'Русский'
}