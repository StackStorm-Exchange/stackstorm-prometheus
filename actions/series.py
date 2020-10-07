#!/usr/bin/env python

from lib.prometheus import PrometheusAPI


class PrometheusSeries(PrometheusAPI):
    def __init__(self, config):
        super(PrometheusSeries, self).__init__(config=config)

    def run(self, queries, url=None):
        params = ['match[]=' + query for __, query in queries.iteritems()]
        url_temp = self.url if url is None else url
        endpoint = "{}/api/v1/series?{}".format(url_temp, '&'.join(params))
        return True, self._get(endpoint, None)
