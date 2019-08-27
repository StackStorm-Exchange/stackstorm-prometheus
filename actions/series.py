#!/usr/bin/env python

from lib.prometheus import PrometheusAPI


class PrometheusSeries(PrometheusAPI):
    def __init__(self, config):
        super(PrometheusSeries, self).__init__(config=config)

    def run(self, queries, url):
        params = ['match[]=' + query for __, query in queries.iteritems()]
        endpoint = "{}/api/v1/series?{}".format(url, '&'.join(params))

        return True, self._get(endpoint, None)
