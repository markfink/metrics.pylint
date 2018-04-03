# -*- coding: utf-8 -*-
"""A metrics plugin to do get pylint_score."""
from __future__ import unicode_literals, print_function

from pylint.lint import Run
from pylint.reporters.json import JSONReporter
from pylint.config import OptionsManagerMixIn

from metrics.metricbase import MetricBase


# silence please!
original__init = OptionsManagerMixIn.__init__
def patched__init__(self, usage, config_file=None, version=None, quiet=1):
    original__init(self, usage, config_file, version, quiet)

OptionsManagerMixIn.__init__ = patched__init__


class SilentReporter(JSONReporter):
    """suppress everything"""
    name = 'null'

    def display_messages(self, layout):
        pass


def get_file_processors():
    """plugin mechanism for file based metrics."""
    return [PyLintMetric]


def get_build_processors():
    """plugin mechanism for build metrics."""
    return []


class PyLintMetric(MetricBase):
    """Compute the pylint_score for a source file."""
    def __init__(self, context):
        self.name = 'pylint_score'
        self._context = context
        self.reset()

    def reset(self):
        self.pylint_score = None

    def process_file(self, language, key, token_list):
        """determine the pylint_score for a given key"""
        # extract the pylint_score as described here:
        # https://stackoverflow.com/questions/39453828/extracting-pylint-score
        if language.startswith('Python'):
            results = Run([key], reporter=SilentReporter(), exit=False)
            self.pylint_score = results.linter.stats.get('global_note', None)

    def get_metrics(self):
        if self.pylint_score:
            #print(self.pylint_score)
            return {self.name: round(self.pylint_score, 2)}
        else:
            return {}

    metrics = property(get_metrics)
