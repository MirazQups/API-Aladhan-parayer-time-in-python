import json


time = json.dumps({
    "city": "dhaka"
})
create = json.dumps({
    "name": "morpheus",
    "job": "leader"
})

user_to_register = json.dumps({
    "firstname": "Miraz",
    "lastname": "Islam"
})


only_email = json.dumps({
    "email": "tracey.ramos@reqre.in",
    "first_name": "Mimi",
    "last_name": "Ramos"
})

only_password = json.dumps({
    "password": "34534kjl53k45#"
})

user_to_login = json.dumps({
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
})

invalid_login_detail = json.dumps({
    "email": "sompod123@gmail.com",
})

ajan = {
    "city": "kolkata"
}