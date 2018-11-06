import pytest
import allure


@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
    Parse env config info
    """
    allure.environment(测试数据库='120.79.232.23')
