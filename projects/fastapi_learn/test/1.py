from requests import *


# fastapi test
def test_fastapi():
    baseurl = "http://127.0.0.1:8080"
    re = get(baseurl + "/useers/me")
    print(re.json())


test_fastapi()
