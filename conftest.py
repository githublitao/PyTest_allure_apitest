import pytest
import allure

from config.configHost import ConfHost


@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
    Parse env config info
    """
    host_config = ConfHost()
    host = host_config.get_host_conf()
    allure.environment(test_platform=host["test_platform"])
    allure.environment(test_platform=host["mock"])
