[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

**WIP**

# Battery Status Notifier (bsnotifier)

Command line application that shows a popup window when the battery is low. This Python script can be used to notify
battery status in [i3wm](https://i3wm.org/) environments.

# Table of contents

* [Get started](#get-started)
  * [Installation](#installation)
  * [Usage](#usage)
* [Developers](#developers)
  * [Requirements](#requirements)
  * [Set Python versions](#set-python-versions)
  * [Run](#run)
* [License](#license)
* [Changelog](#changelog)

# Get started

## Installation

This application can be simply installed by running:

```bash
pip install bsnotifier
```

if you want to install from a source distribution:

```bash
git clone https://github.com/eccanto/battery-status-notifier
cd battery-status-notifier/
python setup.py install
```

# Developers

## Requirements

System requirements:

```bash
sudo apt-get install wmctrl xvfb x11-utils gnumeric
```

Python requirements:

```bash
pip3 install -r requirements_testing.txt
```

## Set Python versions

1. Install [pyenv](https://github.com/pyenv/pyenv)
2. Install python versions:
    ```bash
    for python_version in "3.7" "3.8" "3.9" "3.10" "3.11" "3.12" ; do pyenv install ${python_version}; done
    ```
3. Enable python versions:
    ```bash
    pyenv local "3.7" "3.8" "3.9" "3.10" "3.11" "3.12"
    ```

## Run

We use [tox](https://tox.wiki/en/latest/) and [pytest](https://docs.pytest.org/en/6.2.x) to run the
test suite:

```bash
tox
```

to run the test suite for a particular Python version, you can do:


```bash
tox -e py37
```

# License

[MIT](./LICENSE)

# Changelog

- 1.0.0 - Initial version.
