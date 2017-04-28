#!/usr/bin/env python

from st2actions.runners.pythonrunner import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class RequestsMethod(object):
    @staticmethod
    def method(method, url, auth=None, verify_ssl=False, headers=None, params=None, json=None):
        methods = {'get': requests.get,
                   'post': requests.post}

        if not params:
            params = dict()

        if not json:
            json = dict()

        requests_method = methods.get(method)
        response = requests_method(url, auth=auth, headers=headers, params=params, json=json, verify=verify_ssl)
        if response.status_code:
            return response.json()
        else:
            return response.text


class PrometheusAPI(Action):
    def __init__(self, config):
        super(PrometheusAPI, self).__init__(config=config)
        self.api_ext = 'api/v1'
        self.url = self.config.get('url')

    def _get(self, url, params):
        return RequestsMethod.method('get', url, params=params)

    def get(self, url, endpoint, params):
        uri = "{}/{}/{}".format(url, self.api_ext, endpoint)
        return self._get(uri, params)
