import pytest
from base.webdriver import \
    WebDriver  # this inherits from the webdriverfactory and from those 2 are inheriting the test cases
from datetime import datetime
from py._xmlgen import html
from config import FrameworkConfig


global driver
@pytest.yield_fixture()
def setUp():

    print("Running method level setUp ")

    yield

    print("Running method level tearDown ")

@pytest.yield_fixture(scope="function")
def oneTimeSetUpv2(request, browser):
    print("Running one time setUp")
    wdf = WebDriver(browser)
    global driver
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")



def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--env", action="store", help="Environment to run tests")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")





# the methods below are used for the HTML report
# here the HTML report can be customized







@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request):

    request.config._metadata.update(
        {'Environment': FrameworkConfig.environment_test_setup,
         'Browser' : request.config.getoption("--browser"),  # adds in the html report on which browser the scripts were executed

         }
    )

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells, ):
    try:
        cells.insert(2, html.th('Description'))
        cells.insert(1, html.th('Time', class_='sortable time', col='time'))
        cells.pop()
    except:
        print("Driver not found or environment is not set or no data (conftest)")

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    try:
        cells.insert(2, html.td(report.description))
        cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
        cells.pop()
    except:
        print("Driver not found or environment is not set or no data (conftest)")

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    try:
        outcome = yield
        report = outcome.get_result()
        report.description = str(item.function.__doc__)
    except:
        print("Driver not found or environment is not set or no data (conftest)")




@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    try:
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])
        if report.when == 'call' or report.when == 'setup':
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                screenshot = driver.get_screenshot_as_base64()
                extra.append(pytest_html.extras.image(screenshot, ''))
                report.extra = extra
        report.description = str(item.function.__doc__)
    except:
        print("Driver not found or environment is not set or no data (conftest)")

@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    try:
        if report.passed:
            del data[:]
            data.append(html.div('No log output captured.', class_='empty log'))
    except Exception as e:
        print(e)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    try:
        if FrameworkConfig.generate_html_report is True:
            default_html_path = FrameworkConfig().htnl_make_report()

            if not config.option.htmlpath:
                config.option.htmlpath = default_html_path
        else:
            print("conftest report html is disabled")
    except:
        print("error occurred pytest_configure method")

