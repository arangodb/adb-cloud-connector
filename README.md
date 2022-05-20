# ArangoDB Cloud

[![build](https://github.com/arangodb/adb_cloud/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/arangodb/adb_cloud/actions/workflows/build.yml)
[![CodeQL](https://github.com/arangodb/adb_cloud/actions/workflows/analyze.yml/badge.svg?branch=master)](https://github.com/arangodb/adb_cloud/actions/workflows/analyze.yml)
[![Coverage Status](https://coveralls.io/repos/github/arangodb/adb_cloud/badge.svg?branch=master)](https://coveralls.io/github/arangodb/adb_cloud)
[![Last commit](https://img.shields.io/github/last-commit/arangodb/adb_cloud)](https://github.com/arangodb/adb_cloud/commits/master)

[![PyPI version badge](https://img.shields.io/pypi/v/adb_cloud?color=3775A9&style=for-the-badge&logo=pypi&logoColor=FFD43B)](https://pypi.org/project/adb_cloud/)
[![Python versions badge](https://img.shields.io/pypi/pyversions/adb_cloud?color=3776AB&style=for-the-badge&logo=python&logoColor=FFD43B)](https://pypi.org/project/adb_cloud/)

[![License](https://img.shields.io/github/license/arangodb/adb_cloud?color=9E2165&style=for-the-badge)](https://github.com/arangodb/adb_cloud/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/static/v1?style=for-the-badge&label=code%20style&message=black&color=black)](https://github.com/psf/black)
[![Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=282661&label=Downloads&query=total_downloads&url=https://api.pepy.tech/api/projects/adb_cloud)](https://pepy.tech/project/adb_cloud)

## Installation

```
pip install git+https://github.com/arangodb/adb_cloud.git
```

(not yet available)
```
pip install adb_cloud
```

## Current state

```py
from adb_cloud import get_oasis_credentials

con = get_oasis_credentials()

print(con)
```

##  Development & Testing

1. `git clone https://github.com/arangodb/adb_cloud.git`
2. `cd adb_cloud`
3. (create virtual environment of choice)
4. `pip install -e .[dev]`
6. `pytest`
