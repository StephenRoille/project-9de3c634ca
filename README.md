# CI/CD using Python 🐍, `pytest`, `coverage`, and `hypothesis` on Azure Pipelines 🚀

> :bulb: You can skip the `Project Development` section by cloning the repository


## Project Development

### Initialize Your Project Structure

1. Create a `src` directory and a `tests` directory.

2. Create the following requirements files,

* `requirements-docs.txt` (empty)
* `requirements-tests.txt` (`coverage`, `hypothesis`, `pytest`)
* `requirements-true.txt` (empty)
* `requirements-dev.txt` (`python-dotenv`)

3. Copy/paste the following dependencies into the `requirements-tests.txt`
```text
coverage
hypothesis
pytest
```

4. Copy/paste the following content into the `requirements-dev.txt`
```text
-r requirements-docs.txt
-r requirements-tests.txt
-r requirements-true.txt

python-dotenv
```

The `requirements-docs.txt` and `requirements-true.txt` files are empty, but it is a
good practice to split the various dependencies accordingly.

5. Create a `.env` file to store your environment variables,
```
TESTING_PROFILE = "ci"  # select between "ci" and "debug"
```

6. Create a `.gitignore` file, and copy/paste this
[content](https://www.gitignore.io/api/python);

7. Create a `pyproject.toml` file, copy/paste the following content to configure the
`pytest` and `coverage` libraries,
```bash
# ======
# PYTEST
# ======
[tool.pytest.ini_options]
minversion = "6.0"
testpaths = ["tests"]

# ========
# COVERAGE
# ========
[tool.coverage.run]
command_line = "-m pytest"
omit = ["*/venv/*", "*/gui/*"]

[tool.coverage.html]
directory = "build/coverage/"

[tool.coverage.report]
omit = ["*/tests/*"]
```


### Initialize the `src` Directory as a Package

Copy/paste the following content into the `src/__init__.py` module, this will allow to
import the `src` package from the `tests` package,
```python
from . import codebase

__all__ = ["codebase"]
```


### Create a Set of Functions to Test

Copy/paste the following functions into the `src/codebase.py` module, this would typically
be the code base of your project,
```python
"""A set of dummy functions to test a continous integration pipeline."""


VALID_TYPES = (complex, float, int)


def add(a: complex, b: complex) -> complex:
    """Add two numbers.

    Parameters
    ----------
    a : Union[:class:`complex`, :class:`float`, :class:`int`]
        number
    b : Union[:class:`complex`, :class:`float`, :class:`int`]
        number

    Returns
    -------
    Union[:class:`complex`, :class:`float`, :class:`int`]
        result adding `a` and `b`

    Raises
    ------
    TypeError
        if `a` is not :class:`complex` / :class:`float` / :class:`int`
    TypeError
        if `b` is not :class:`complex` / :class:`float` / :class:`int`
    """
    if not isinstance(a, VALID_TYPES):
        raise TypeError(f"'a' must be {VALID_TYPES}, got {type(a)}.")
    if not isinstance(b, VALID_TYPES):
        raise TypeError(f"'b' must be {VALID_TYPES}, got {type(b)}.")
    return a + b


def subtract(a: complex, b: complex) -> complex:
    """Subtract two numbers.

    Parameters
    ----------
    a : Union[:class:`complex`, :class:`float`, :class:`int`]
        number
    b : Union[:class:`complex`, :class:`float`, :class:`int`]
        number

    Returns
    -------
    Union[:class:`complex`, :class:`float`, :class:`int`]
        result subtracting `b` from `a`

    Raises
    ------
    TypeError
        if `a` is not :class:`complex` / :class:`float` / :class:`int`
    TypeError
        if `b` is not :class:`complex` / :class:`float` / :class:`int`
    """
    if not isinstance(a, VALID_TYPES):
        raise TypeError(f"a must be {VALID_TYPES}, got {type(a)}.")
    if not isinstance(b, VALID_TYPES):
        raise TypeError(f"'b' must be {VALID_TYPES}, got {type(b)}.")
    return a - b


def multiply(a: complex, b: complex) -> complex:
    """Multiply two numbers.

    Parameters
    ----------
    a : Union[:class:`complex`, :class:`float`, :class:`int`]
        number
    b : Union[:class:`complex`, :class:`float`, :class:`int`]
        number

    Returns
    -------
    Union[:class:`complex`, :class:`float`, :class:`int`]
        result multiplying `a` and `b`

    Raises
    ------
    TypeError
        if `a` is not :class:`complex` / :class:`float` / :class:`int`
    TypeError
        if `b` is not :class:`complex` / :class:`float` / :class:`int`
    """
    if not isinstance(a, VALID_TYPES):
        raise TypeError(f"a must be {VALID_TYPES}, got {type(a)}.")
    if not isinstance(b, VALID_TYPES):
        raise TypeError(f"'b' must be {VALID_TYPES}, got {type(b)}.")
    return a * b


def divide(a: complex, b: complex) -> complex:
    """Divide two numbers.

    Parameters
    ----------
    a : Union[:class:`complex`, :class:`float`, :class:`int`]
        number
    b : Union[:class:`complex`, :class:`float`, :class:`int`]
        number

    Returns
    -------
    Union[:class:`complex`, :class:`float`, :class:`int`]
        result diving `a` by `b`

    Raises
    ------
    TypeError
        if `a` is not :class:`complex` / :class:`float` / :class:`int`
    TypeError
        if `b` is not :class:`complex` / :class:`float` / :class:`int`
    ZeroDivisionError
        if `b` is `0`
    """
    if not isinstance(a, VALID_TYPES):
        raise TypeError(f"a must be {VALID_TYPES}, got {type(a)}.")
    if not isinstance(b, VALID_TYPES):
        raise TypeError(f"'b' must be {VALID_TYPES}, got {type(b)}.")
    return a / b
```

### Write Some Tests

Copy/paste the following test functions into the `tests/test_codebase.py` module,
```python
import hypothesis.strategies as st
import pytest
import src
from hypothesis import given

# load hypothesis configuration
import config  # noqa:F401


def all_types():
    """All built-in types hypothesis knows."""
    return st.from_type(type).flatmap(st.from_type)


@given(
    a=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
    b=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
)
def test_add(a: int, b: int):
    types = (float, int, complex)
    # invalid inputs should raise a TypeError
    if not isinstance(a, types) or not isinstance(b, types):
        with pytest.raises(TypeError):
            src.codebase.add(a, b)
    else:
        c = src.codebase.add(a, b)
        # the return type must be a supertype of the input argument types
        if type(a).__name__ == "complex" or type(b).__name__ == "complex":
            assert type(c).__name__ == "complex"
        elif type(a).__name__ == "float" or type(b).__name__ == "float":
            assert type(c).__name__ == "float"
        else:
            assert type(c).__name__ == "int"


@given(
    a=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
    b=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
)
def test_subtract(a: int, b: int):
    types = (float, int, complex)
    # invalid inputs should raise a TypeError
    if not isinstance(a, types) or not isinstance(b, types):
        with pytest.raises(TypeError):
            src.codebase.subtract(a, b)
    else:
        c = src.codebase.subtract(a, b)
        # the return type must be a supertype of the input argument types
        if type(a).__name__ == "complex" or type(b).__name__ == "complex":
            assert type(c).__name__ == "complex"
        elif type(a).__name__ == "float" or type(b).__name__ == "float":
            assert type(c).__name__ == "float"
        else:
            assert type(c).__name__ == "int"


@given(
    a=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
    b=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
)
def test_multiply(a: int, b: int):
    types = (float, int, complex)
    # invalid inputs should raise a TypeError
    if not isinstance(a, types) or not isinstance(b, types):
        with pytest.raises(TypeError):
            src.codebase.multiply(a, b)
    else:
        c = src.codebase.multiply(a, b)
        # the return type must be a supertype of the input argument types
        if type(a).__name__ == "complex" or type(b).__name__ == "complex":
            assert type(c).__name__ == "complex"
        elif type(a).__name__ == "float" or type(b).__name__ == "float":
            assert type(c).__name__ == "float"
        else:
            assert type(c).__name__ == "int"


@given(
    a=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
    b=st.one_of(st.integers(), st.floats(), st.complex_numbers(), all_types()),
)
def test_divide(a: int, b: int):
    types = (float, int, complex)
    # invalid inputs should raise a TypeError
    if not isinstance(a, types) or not isinstance(b, types):
        with pytest.raises(TypeError):
            src.codebase.divide(a, b)
    # b=0 should raise a ZeroDivisionError
    elif b == 0:
        with pytest.raises(ZeroDivisionError):
            src.codebase.divide(a, b)
    else:
        c = src.codebase.divide(a, b)
        # the return type must be a supertype of the input argument types
        if type(a).__name__ == "complex" or type(b).__name__ == "complex":
            assert type(c).__name__ == "complex"
        else:
            assert type(c).__name__ == "float"
```

### Configure Your `hypothesis` Test Profile

Copy/paste the following content into the `tests/config.py` module to configure the
`hypothesis` package,
```python
import os

import hypothesis
from dotenv import load_dotenv

# load environment variables from file
load_dotenv()

suppress_health_check = (
    hypothesis.HealthCheck.data_too_large,
    hypothesis.HealthCheck.filter_too_much,
    hypothesis.HealthCheck.too_slow,
    hypothesis.HealthCheck.return_value,
    hypothesis.HealthCheck.large_base_example,
    hypothesis.HealthCheck.not_a_test_method,
)

# CREATE CI PROFILE
# =================
hypothesis.settings.register_profile(
    "ci",
    deadline=1000,
    max_examples=1000,
    suppress_health_check=suppress_health_check,
)

# CREATE DEBUGGING PROFILE
# ========================
hypothesis.settings.register_profile(
    "debug",
    deadline=1000,
    max_examples=20,
    suppress_health_check=suppress_health_check,
    verbosity=hypothesis.Verbosity.verbose,
)

# SET PROFILE
# ===========
# read value from TESTING_PROFILE environment variable
MODE = os.environ.get("TESTING_PROFILE", "debug")
hypothesis.settings.load_profile(MODE)
```

## Install the Dependencies

1. Create a virtual environment to isolate your dependencies,
```bash
python -m venv --prompt=project-9de3c634ca venv
```

2. Activate your virtual environment (Window 10, this command depends on the OS),
```bash
venv\scripts\activate.bat
```
Note that the command prompt should now be prefixed by `(project-9de3c634ca)`

3. Install all the development dependencies,
```bash
pip install -r requirements-dev.txt
```

This call recursively installs the dependencies from all the required files (`-docs`,
`-tests`, `-true`).


## Create a Repository and Enable the Azure Pipelines

> :bulb: Follow the steps shown in the video from this page for details:
>
> [Announcing Azure Pipelines with unlimited CI/CD minutes for open source](
https://azure.microsoft.com/en-us/blog/announcing-azure-pipelines-with-unlimited-ci-cd-minutes-for-open-source/)

1. Create an Azure DevOps account (the account creation and usage will be free, you can
connect through your GitHub account);

2. Install the Azure Pipelines Application from the GitHub Marketplace;

3. Create a new `Public` GitHub repository. Enable the Azure Pipelines App to access the
current repository. If the Azure Pipelines does not appear, be sure you have done steps
1 and 2 correctly. Selecting `Public` grants you access to 10 concurrent jobs and an
unlimited number of build minutes 😁

![create_repo](https://github.com/StephenRoille/project-9de3c634ca/blob/master/screenshots/create_repo.png)

4. Push the code from your local machine (see `Project Development` section, or the
cloned repository) to your GitHub account, if you have cloned the repo be sure to manually
delete the `.git` directory before executing the following commands. This will ensure
your remote server is linked to your account and not mine.
```bash

git init .
git add .
git commit -m "First commit"
git remote add origin git@github.com:<your-name>/<your-repo>.git
git push -u origin master
```

## Configure the CI/CD Pipeline

> :bulb: Follow the steps from this page for details:
>
> [GitHub integration with Azure Pipelines](
https://azuredevopslabs.com/labs/vstsextend/github-azurepipelines/)

1. Connect through GitHub (YAML);

![create_project_azure_step_1_connect](https://github.com/StephenRoille/project-9de3c634ca/blob/master/screenshots/create_project_azure_step_1_connect.png)

2. Select the GitHub repository you want to configure;

![create_project_azure_step_2_select](https://github.com/StephenRoille/project-9de3c634ca/blob/master/screenshots/create_project_azure_step_2_select.png)

3. Configure your pipeline using any template;

![create_project_azure_step_3_configure](https://github.com/StephenRoille/project-9de3c634ca/blob/master/screenshots/create_project_azure_step_3_configure.png)

4. Replace the content of the `azure-pipelines.yml` file;

> :warning: Be sure to replace `vmImage: ubuntu-default` with `vmImage: ubuntu-latest`
> since the former will make the build fail (at least on the day of writing).

```yaml

# Python package
# Create and test a Python package on multiple Python versions.
# Add steps that analyze code, save the dist with the build record, publish to a PyPI-compatible index, and more:
# https://docs.microsoft.com/azure/devops/pipelines/languages/python

trigger:
- master

pool:
  vmImage: ubuntu-latest
strategy:
  matrix:
    Python36:
      python.version: '3.6'
    Python37:
      python.version: '3.7'
    Python38:
      python.version: '3.8'
    Python39:
      python.version: '3.9'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '$(python.version)'
  displayName: 'Use Python $(python.version)'

- script: |
    python -m pip install --upgrade pip
    pip install -r requirements-dev.txt
  displayName: 'Install dependencies'

- script: |
    python -m pytest
  displayName: 'Run tests with pytest and hypothesis'
```

5. Save/run the pipeline by opening a pull request on a new `azure-pipelines` branch;

![create_project_azure_step_4_review](https://github.com/StephenRoille/project-9de3c634ca/blob/master/screenshots/create_project_azure_step_4_review.png)

6. Go to your GitHub account select the `azure-pipelines` branch, you should see the
build succeed;

![create_project_azure_step_5_successful_build_pull_request](https://github.com/StephenRoille/project-9de3c634ca/blob/master/screenshots/create_project_azure_step_5_successful_build_pull_request.png)

7. Merge the pull request and delete the `azure-pipelines` branch;

![create_project_azure_step_6_delete_branch](https://github.com/StephenRoille/project-9de3c634ca/blob/master/screenshots/create_project_azure_step_6_delete_branch.png)

