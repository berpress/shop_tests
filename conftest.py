import pytest

from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    app = Application(url)
    yield app
    app.browser_close()


@pytest.fixture
def login(request, app):
    login = request.config.getoption("--username")
    passwd = request.config.getoption("--password")
    app.open_main_page()
    if app.login.logout_button() == 0:
        app.login.auth(login, passwd)


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="http://automationpractice.com/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="admin@admin.ru",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="admin",
        help="enter password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=True,
        help="launching browser without gui",
    ),
