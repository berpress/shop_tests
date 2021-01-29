import pytest

from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    app = Application(url)
    yield app
    app.browser_close()


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
        default="test74@test.com",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="Password11",
        help="enter password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=True,
        help="launching browser without gui",
    ),
