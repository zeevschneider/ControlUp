import requests
from support.env_data import GetEnv


class WeatherApi:
    """
        This class is used for communication with the api provided by WeatherApi
    """
    def __init__(self):
        self.env = GetEnv().get_env_data()

    def history_weather(self, query_param, date, use_api_key=True, response_format='json', *args):
        # This function is used for the history api.
        # The use_api_key variable is here in case we will want to test negative scenario
        # without a key - # TODO: think of a better solution

        # TODO - handle also the unixdt param: api could either handle dt or unixdt but not both
        key = ""
        if use_api_key:
            key = self.env['api_key']
        args += f'q={query_param}', f'dt={date}'
        url = self._format_url(f'history.{response_format}', key, *args)
        return requests.get(url)

    def search_by_param(self, search_param, use_api_key=True, response_format='json', *args):
        # This function is used for the search / autocomplete api.
        # Regarding the use_api_key param see the comment in the history_weather func
        key = ""
        if use_api_key:
            key = self.env['api_key']
        args += (f'q={search_param}',)
        url = self._format_url(f'search.{response_format}', key, *args)
        return requests.get(url)

    def _format_url(self, api_call, key, *args):
        url = f"{self.env['base_url']}/{api_call}?key={key}&{'&'.join(args)}"
        return url


