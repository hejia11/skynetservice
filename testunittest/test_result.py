import requests



def test_returnPara():
    url = "http://47.96.53.33/swagger-apiui/skynet-service/department/list"
    response = requests.get(url)
    print(response.text)
    result = response.json()
    print(type(result))
    data = result["data"]
    a = []
    for x in data:
        a.append(x['departmentId'])
    print(a)
    return a


def test_inputPara(para):
    url = 'http://47.96.53.33/swagger-apiui/skynet-service/department/cityList'
    response = requests.get(url, 'department=' + str(para))
    print(response.text)


b = test_returnPara()
print(b)
for y in b:
    print(y)
    test_inputPara(y)


