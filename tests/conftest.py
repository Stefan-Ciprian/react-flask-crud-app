import pytest
from sqlalchemy import event
import os
import tempfile
from flaskapp import create_app
from flaskapp.config import TestingConfig
from flaskapp.database import engine, db_session, Base


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(TestingConfig)

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture(scope="session")
def connection():
    connection = engine.connect()

    yield connection

    connection.close()


@pytest.fixture(scope="session")
def setup_db(connection, request):
    Base.metadata.bind = connection
    Base.metadata.create_all()

    def teardown():
        Base.metadata.drop_all()

    request.addfinalizer(teardown)

    return None


@pytest.fixture(autouse=True)
def session(connection, setup_db, request):
    transaction = connection.begin()
    session = db_session(bind=connection)
    session.begin_nested()

    @event.listens_for(session, "after_transaction_end")
    def restart_savepoint(db_session, transaction):
        if transaction.nested and not transaction._parent.nested:
            session.expire_all()
            session.begin_nested()

    def teardown():
        db_session.remove()
        transaction.rollback()

    request.addfinalizer(teardown)

    return session


