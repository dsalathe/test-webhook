import os
import sys

sys.path.append('src')
from models import Builds
import db


def test_db_exists():
    db.init_db()
    db_exists = os.path.exists('../database.db')
    assert db_exists is True


def test_db_does_not_exist():
    db.init_db()
    db_exists = os.path.exists('../db.db')
    assert db_exists is False


def test_insert_new_build():
    db.init_db()
    number_of_builds = len(Builds.query.all())
    db.create_build("This is a new test", True)
    new_len = len(Builds.query.all())
    assert number_of_builds == new_len - 1
