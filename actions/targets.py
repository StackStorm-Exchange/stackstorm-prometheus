#!/usr/bin/env python

from lib.prometheus import PrometheusAPI


class PrometheusTarget(PrometheusAPI):
    def __init__(self, config):
        super(PrometheusTarget, self).__init__(config=config)

    def run(self, url=None):
        url_temp = self.url if url is None else url
        endpoint = "{}/api/v1/targets".format(url_temp)
        return True, self._get(endpoint, None)
