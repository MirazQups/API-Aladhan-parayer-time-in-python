import requests


def data_from_server(method="", endpoint="", headers="", params=""):
    res = requests.request(method, endpoint, headers=headers, data=params)
    return res


def post_data():
    r = requests.post("https://reqres.in/api/users", data={
        "email": "tracey.ramos@reqres.in",
        "first_name": "Momtaz",
        "last_name": "Ramos"})
    return r


def data_for_post(url="", data={}):
    res = requests.post(url, data)
    return res
