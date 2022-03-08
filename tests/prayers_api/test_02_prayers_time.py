import allure

from test_data.common_data import *
from test_data.users_api.prayers_api_data import *


@allure.step('get tomorrow prayer times')
def test_02_prayer_times():
    response_body, status_code = response_get_prayer_times_calendar_by_address()
    print(response_body)
    assert status_code == 200
    print(response_body['data'][1]['timings']['Sunrise'])
    assert response_body['data'][1]['timings']['Sunrise'] == "06:46 (+03)"

    for child in response_body['data'][1]['timings']:
        print(child)
        # assert child == "Sunrise"
        # assert child['Sunrise'] == "06:46 (+03)"


def test_02_new_time():
    assert response1.status_code == 200
    print(body)
    assert body["status"] == "OK"
    assert body["code"] == 200

    # for child in body['data'][1]['timings']:


