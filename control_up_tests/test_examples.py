import pytest
import json
import logging
from datetime import datetime
from datetime import timedelta

from support.weather_api import WeatherApi


@pytest.mark.parametrize("place_name_or_location, date", [("Paris",
                                                           (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d"))])
def test_history(place_name_or_location, date):
    w_a = WeatherApi()
    history_data = w_a.history_weather(place_name_or_location, date)
    # TODO - handle also a xml response
    content = json.loads(history_data.content)
    logging.info("Verify history date")
    with pytest.assume:
        assert str(date) == content['forecast']['forecastday'][0]['date']
    logging.info("Verify env celsius temp")
    max_temp_c = content['forecast']['forecastday'][0]['day']['maxtemp_c']
    min_temp_c = content['forecast']['forecastday'][0]['day']['mintemp_c']
    avg_temp_c = content['forecast']['forecastday'][0]['day']['avgtemp_c']
    with pytest.assume:
        # there is a problem with avg. temps in the api:
        # e.g - for 9.1.2024 in Paris: max_c was 1.4, min_c was -1.5 and the avg_c was -0.7
        assert avg_temp_c == format((max_temp_c + min_temp_c) // 2, '.1f')
    logging.info("Compare sunrise data using the lat and lon parameters")
    sunrise = content['forecast']['forecastday'][0]['astro']['sunrise']
    latitude = content['location']['lat']
    longitude = content['location']['lon']
    with pytest.assume:
        history_data_by_lat_lon = w_a.history_weather(f"{latitude},{longitude}", date)
        content_by_lat_lon = json.loads(history_data_by_lat_lon.content)
        assert sunrise == content_by_lat_lon['forecast']['forecastday'][0]['astro']['sunrise']


@pytest.mark.parametrize("search_param, response_length", [("sama", 5)])
def test_search_or_autocomplete(search_param, response_length):
    w_a = WeatherApi()
    response = w_a.search_by_param(search_param)
    # TODO - handle also a xml response
    content = json.loads(response.content)
    logging.info("Verify the length of a response")
    assert len(content) == response_length

