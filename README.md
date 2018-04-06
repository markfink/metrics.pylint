[![License](http://img.shields.io/badge/license-MIT-yellowgreen.svg)](MIT_LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/markfink/metrics.pylint.svg?maxAge=2592000)](https://github.com/markfink/metrics.pylint/issues)


# installation

to install:

``` bash
$ pip install metrics.pylint
```

to uninstall:

``` bash
$ pip uninstall metrics.pylint
```

for details please see the documentation of metrics.


# metrics.pylint

The **matrics.gitinfo** package is a plugin for the metrics package. 

metrics.pylint adds a pylint_score to file metrics for all python files:

``` json
    "tests/test_sloc_python.py": {
        "comments": 8,
        "language": "Python",
        "mccabe": 0,
        "positions": [],
        "pylint_score": 6.67,
        "ratio_comment_to_code": 0.24,
        "sloc": 33
    }
```


# Acknowledgements

alecxe for a recipe on how to use pylint programmatically and how to extract the
pylint score: https://stackoverflow.com/questions/39453828/extracting-pylint-score


# License

Copyright (c) 2018 Mark Fink and others.
metrics is released under the MIT License (see MIT_LICENSE).
