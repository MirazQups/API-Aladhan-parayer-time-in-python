import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get today prayer times')
def test_01_prayer_times():
    body = post_method_test()
    print(body)
    # response_body, status_code = response_get_prayer_times_calender()
    # print(response_body)
    # print(header)
    # print(times)
    # print(type(response_body))
    # assert status_code == 201
    # assert head == {'Content-Type': 'application/json; charset=utf-8'}
    # print(type(head))
    # print(head['Content-Type'])
    # print(response_body['data'][1]['timings']['Sunrise'])
    # assert response_body['data']['email'] == 'janet.weaver@reqres.in'

