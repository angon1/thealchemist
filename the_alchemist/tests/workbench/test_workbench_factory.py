import pytest
from workbench.workbench_factory import WorkbenchFactory

def test_create_workbench_success(mocker):
    data = {'param1': 'value1', 'param2': 'value2'}
    mock_workbench = mocker.patch('workbench.workbench_factory.Workbench', return_value='mock_workbench')
    
    result = WorkbenchFactory.create(data)
    
    mock_workbench.assert_called_once_with(**data)
    assert result == 'mock_workbench'

def test_create_workbench_failure(mocker):
    data = {'param1': 'value1', 'param2': 'value2'}
    mocker.patch('workbench.workbench_factory.Workbench', side_effect=Exception('Creation error'))
    
    with pytest.raises(Exception) as excinfo:
        WorkbenchFactory.create(data)
    
    assert str(excinfo.value) == 'Failed to create workbench: Creation error'