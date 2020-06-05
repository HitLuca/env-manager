# env-manager

[![Build Status](https://travis-ci.com/HitLuca/env-manager.svg?branch=master)](https://travis-ci.com/HitLuca/env-manager)
[![code style](https://img.shields.io/badge/code%20style-black-black)](https://black.readthedocs.io/en/stable/)

Environment variables manager to ensure consistency and remove human errors. Access to env variables should be done through the EnvManager class, which ensures that the environment is consistent with the user expectations.

## Features

- Using the `EnvManager` class, you are assured that all env variables fetching is done correctly, and you won't incour in errors when trying to get a variable that doesn't exist.

- `EnvManager` allows the user to fetch both string and boolean variables, and ensures that they have a set value (no `VAR=""` allowed by default, but it can be allowed manually).

- Variables loading is done using a simple api structure.

- Full `mypy` type hints.

## Installation

From `.whl` file: install the latest env-manager version by downloading the wheel file from [here](https://github.com/HitLuca/env-manager/releases).

From git: install the package from git sources (for pipenv, `pipenv install git+https://github.com/HitLuca/env-manager#egg=env-manager`)

## Usage

Your environment variables should be stored in an Enum class like so:

```python
class MyVars(Enum):
    TEST_FOO = auto()
    TEST_BAR = auto()
```

The class name is not important. Make sure that the env var names match the actual environment names. Also, the values for the enum items aren't used.

Start your project by first loading all your env variables if needed, and then make EnvManager check that everything is good using the `check_env_mappings_exist` function. After that, simply load your env variables where needed.

```python
class MyVars(Enum):
    TEST_FOO = auto()
    TEST_BAR = auto()


# load your environment from a file or externally before this step
EnvManager.check_env_mappings_exist(MyVars)
```

Assuming `TEST_FOO=true` and `TEST_BAR=tomato`:

```python
if EnvManager.get_bool(MyVars.TEST_FOO):
    print(EnvManager.get_string(MyVars.TEST_BAR))

# prints "tomato"
```

If you want to allow a string env variable to be empty, just pass the `can_be_empty` flag to `True`. This is useful for not setting some services, as in the case of `sentry.io`. Assume `SENTRY_URL` can have a url or not, and if not the sentry service won't be connected to the relative tracking project

```python
class EnvMappings(Enum):
    SENTRY_URL = auto()

sentry_sdk.init(
        dsn=EnvManager.get_string(EnvMappings.SENTRY_URL, can_be_empty=True),
        integrations=[FlaskIntegration()],
    )

# if SENTRY_URL is set it connects the script to the tracking project
# if SENTRY_URL is empty, it doesn't setup the integration
```

Easy!

## Contribute

Issue Tracker: <https://github.com/HitLuca/env-manager/issues>

Source Code: <https://github.com/HitLuca/env-manager>

## Support

If you are having issues, please let me know. This is a personal project, but if general interest is shown, I'll make sure to put more work into it

## License

The project is licensed under the MIT license.
