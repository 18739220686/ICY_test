#使用pytest。fixture
import pytest
@pytest.fixture(scope='function',params=['http://47.93.9.92:1880/index.php'])
def my_fixture(request):
    print('前置')
    yield request.param  #yield返回
    print('后置')