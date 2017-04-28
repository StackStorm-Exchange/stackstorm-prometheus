#!/usr/bin/env python

from st2actions.runners.pythonrunner import Action
from collections import defaultdict


class AlertAggregation(Action):
    def run(self, alerts, parent, child):
        a = defaultdict(list)
        for alert in alerts:
            a[alert['labels'][parent]].append(alert['labels'][child])

        return a
