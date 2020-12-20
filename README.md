[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

# Py CDK Utils

## Project Description

AWS CDK is brilliant. However, there are a few mundane tasks which require a bit of copy-paste code. This library gets
around this problem by providing some common utils to help write AWS CDK stacks in Python.

The following functionality is supported:

- Environment specific configuration

## Getting Started

Installation is as easy as:

```commandline
poetry install py-cdk-utils
```

or if you prefer:

```commandline
pip install py-cdk-utils
```

## Usage

### Environment Specific Configuration

Deploying an AWS CDK stack may require differing configuration from one environment to another. For instance, running a
stack in Dev may require different settings to that of Production.

To help make this easy, py-cdk-utils provides the ability to switch configuration based on an Environment Variable:
`DEPLOY_ENV`.

#### Import DeployEnv and get_config

To use this util, import the `DeployEnv` enum and the `get_config` helper function:

```python
from py_cdk_utils import DeployEnv, get_config
```

#### Environment Names

The following environment names are available by default:

- local
- development
- test
- pre-production
- production

#### Environment Specific Configuration

If configuration is the same for all environments, then simply continue to configure the setting normally. However, if
you require a certain value to be different from one environment to another, then you should use the `get_config`
function. The function accepts a default value - used if no qualifying override can be found - and a dictionary of
overrides. The overrides should consist of:

- Keys: An attribute of the DeployEnv enum, e.g. `DeployEnv.DEV`
- Values: The value to be used when the key is the current environment.

In this example, when the DEPLOY_ENV environment variable equals "production", then the log_level will be set to "INFO".
In all other environments, it will be set to "DEBUG":

```python
from py_cdk_utils import DeployEnv, get_config

log_level = get_config("DEBUG", {DeployEnv.PROD: "INFO"})
```

## Contributing

This projects welcomes contributions. Please follow the contribution instructions [here](CONTRIBUTING.md).

## Contributor Code Of Conduct

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree
to abide by its terms. You will find the terms [here](CODE_OF_CONDUCT.md).

## License

This library is published under the [MIT License](LICENSE.md).
