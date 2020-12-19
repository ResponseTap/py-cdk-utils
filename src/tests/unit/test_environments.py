import pytest
from py_cdk_utils import DeployEnv, get_config

test_default = "default"
test_overrides = {DeployEnv.DEV: "dev val", DeployEnv.LOCAL: "local val"}


def test_no_args():
    with pytest.raises(TypeError):
        get_config()


def test_default_value():
    with pytest.raises(TypeError):
        get_config(default_value="test")


def test_override_only():
    with pytest.raises(TypeError):
        get_config({DeployEnv.DEV: "dev value"})


def test_valid_multiple_overrides_none_qualify(mocker):
    mocker.patch("py_cdk_utils.environments.deploy_env", DeployEnv.PROD)
    assert get_config(test_default, test_overrides) == test_default


def test_valid_multiple_one_qualifies(mocker):
    mocker.patch("py_cdk_utils.environments.deploy_env", DeployEnv.DEV)
    assert get_config(test_default, test_overrides) == "dev val"
