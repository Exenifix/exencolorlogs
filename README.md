![PyPI - Downloads](https://img.shields.io/pypi/dm/exencolorlogs)
![License](https://img.shields.io/github/license/Exenifix/exencolorlogs)
![PyPI - Version](https://img.shields.io/pypi/v/exencolorlogs)
![CodeFactor](https://www.codefactor.io/repository/github/exenifix/exencolorlogs/badge)

# ExenColorLogs

A module for nice looking colored logs. Does not have much customization, just a Logger class with special formatting.

## Installation

The module is available for installation from PyPI via pip.
```shell
$ pip install exencolorlogs
```

## Basic Usage

```python
from exencolorlogs import Logger

log = Logger()
log.info("Greeting...")
log.ok("Hello!")
```
