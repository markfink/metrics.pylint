# -*- coding: utf-8 -*-
from metrics_pylint.info import PyLintMetric


def test_pylint_metric():
    plm = PyLintMetric({})

    plm.process_file('Python', 'tests/test_pylint_metric.py', [])
    metrics = plm.metrics

    assert metrics == {'pylint_score': 6.67}
