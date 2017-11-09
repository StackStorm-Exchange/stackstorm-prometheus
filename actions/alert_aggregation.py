#!/usr/bin/env python

from collections import defaultdict
from st2common.runners.base_action import Action


class AlertAggregation(Action):
    def run(self, alerts, parent, child):
        a = defaultdict(list)
        for alert in alerts:
            a[alert['labels'][parent]].append(alert['labels'][child])

        return a
