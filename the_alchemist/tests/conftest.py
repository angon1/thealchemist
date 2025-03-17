import pytest
from workbench.workbench import Workbench

@pytest.fixture
def workbench():
    return Workbench(tools=[], ingredients=[])