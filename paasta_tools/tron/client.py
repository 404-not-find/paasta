# Copyright 2015-2018 Yelp Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
from urllib.parse import urljoin

import requests

from paasta_tools.utils import get_user_agent


log = logging.getLogger(__name__)


class TronRequestError(Exception):
    pass


class TronClient:
    """
    Client for interacting with a Tron master.
    """

    def __init__(self, url):
        self.master_url = url

    def _request(self, method, url, data):
        headers = {'User-Agent': get_user_agent()}
        kwargs = {
            'url': urljoin(self.master_url, url),
            'headers': headers,
        }
        if method == 'GET':
            kwargs['params'] = data
            response = requests.get(**kwargs)
        elif method == 'POST':
            kwargs['data'] = data
            response = requests.post(**kwargs)
        else:
            raise ValueError('Unrecognized method: {}'.format(method))

        return self._get_response_or_error(response)

    def _get_response_or_error(self, response):
        try:
            result = response.json()
            if 'error' in result:
                raise TronRequestError(result['error'])
            return result
        except ValueError:  # Not JSON
            if not response.ok:
                raise TronRequestError(
                    'Status code {status_code} for {url}: {reason}'.format(
                        status_code=response.status_code,
                        url=response.url,
                        reason=response.reason,
                    ),
                )
            return response.text

    def _get(self, url, data=None):
        return self._request('GET', url, data)

    def _post(self, url, data=None):
        return self._request('POST', url, data)

    def update_namespace(self, namespace, new_config, skip_if_unchanged=True):
        """Updates the configuration for a namespace.

        :param namespace: str
        :param new_config: str, should be valid YAML.
        :param skip_if_unchanged: boolean. If False, will send the update
            even if the current config matches the new config.
        """
        current_config = self._get('/api/config', {'name': namespace})
        if skip_if_unchanged and new_config == current_config['config']:
            log.info('No change in config, skipping update.')
            return

        return self._post(
            '/api/config',
            data={
                'name': namespace,
                'config': new_config,
                'hash': current_config['hash'],
                'check': 0,
            },
        )

    def list_namespaces(self):
        """Gets the namespaces that are currently configured."""
        response = self._get('/api')
        return response.get('namespaces', [])
