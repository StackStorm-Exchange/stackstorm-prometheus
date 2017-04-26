#!/usr/bin/env python

from lib.prometheus import PrometheusAPI


class PrometheusQuery(PrometheusAPI):
    def __init__(self, config):
        super(PrometheusQuery, self).__init__(config=config)

    def run(self, query):
        endpoint = "{}/api/v1/query".format(self.url)
        return True, self._get(endpoint, params={"query": query})

