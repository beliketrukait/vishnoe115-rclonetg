#**************************************************
# Based on:
# Repository:  https://github.com/anasty17/mirror-leech-telegram-bot/
# Source: https://github.com/anasty17/mirror-leech-telegram-bot/blob/master/update.py
#**************************************************/

from os import path as ospath, environ
from subprocess import run as srun

if ospath.exists('botlog.txt'):
    with open('botlog.txt', 'r+') as f:
        f.truncate(0)

UPSTREAM_REPO = environ.get('UPSTREAM_REPO')
UPSTREAM_BRANCH = environ.get('UPSTREAM_BRANCH')
try:
    if len(UPSTREAM_REPO) == 0:
       raise TypeError
except TypeError:
    UPSTREAM_REPO = 'https://github.com/beliketrukait/vishnoe115-rclonetg/'
try:
    if len(UPSTREAM_BRANCH) == 0:
       raise TypeError
except TypeError:
    UPSTREAM_BRANCH = 'h-code'

if UPSTREAM_REPO is not None:
    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])

    srun([f"git init -q \
            && git config --global user.email sam.agd@outlook.com \
            && git config --global user.name rctb \
            && git add . \
            && git commit -sm update -q \
            && git remote add origin {UPSTREAM_REPO} \
            && git fetch origin -q \
            && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)
