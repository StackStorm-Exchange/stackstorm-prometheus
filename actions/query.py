#!/usr/bin/env python

from lib.prometheus import PrometheusAPI


class PrometheusQuery(PrometheusAPI):
    def __init__(self, config):
        super(PrometheusQuery, self).__init__(config=config)

    def run(self, query, url):
        url_temp = self.url if url == "" else url
        endpoint = "{}/api/v1/query".format(url_temp)
        return True, self._get(endpoint, params={"query": query})
