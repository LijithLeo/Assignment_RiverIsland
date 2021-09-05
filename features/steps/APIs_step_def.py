import requests
import json
from behave import *

global response
base_url = 'https://api.thecatapi.com/v1/votes'
headers_xapi = {
    "x-api-key": "DEMO-API-KEY"
}
headers_xapip = {
    "x-api-key": "DEMO-API-KEY",
    "Content-Type": "application/json"
}

@given(u'Protocol Host Version and Authorization are accessible')
def pre_objective(context):
    assert base_url != "", "Base URL is empty"
    assert headers_xapi != "", "Header is empty"
    response = requests.get(base_url, headers = headers_xapi)
    print(response.status_code)
    print(type(response.status_code))
    assert response.status_code == 200, "Get Request is successful"


@when(u'We request GET method we should be able to get the list of votes')
def objective1(context):
    response = requests.get(base_url, headers=headers_xapi)
    # print(response.content)
    global json_response
    #Unmarshal response from byte to Json array
    json_response = json.loads(response.text)
    print(json_response)
    print(response.status_code)
    # print(type(response.status_code))
    # print(type(json_response))
    assert response.status_code == 200, "Get Request is successful"
    assert len(response.content) > 0, "response content length more then 0"


@when(u'We pick the ID from previous response we should be able to fetch the other details')
def objective2(context):
    ID1 = json_response[0]['id']
    print(ID1)
    assert ID1 == 31098, "Successfully validated first ID and response is not empty"


@when(u'We POST new resource it should accept the new vote')
def objective3(context):
    new_resource = "{\"image_id\":\"asf2\",\"sub_id\":\"my-user-1234\",\"value\":1}"
    global new_resource_res
    new_resource_res = requests.post(base_url, headers=headers_xapip, data=new_resource)
    print(new_resource_res.status_code)
    assert new_resource_res.status_code == 200, "POST Successful for new Vote ID"
    print(new_resource_res.json())


@when(u'We GET we should be able to get the newly created resource')
def objective4(context):
    jr = (new_resource_res.json())
    global vote_id
    vote_id = str((jr['id']))
    url1 = "https://api.thecatapi.com/v1/votes/"
    response = requests.get(url1 + vote_id, headers=headers_xapi)
    json_response = json.loads(response.text)
    print((json_response))
    print(response.status_code)
    assert response.status_code == 200, "GET Successful for newly added Vote ID"


@when(u'We DELETED the nedpoint should delete the newly created resource')
def objective5(context):
    url1 = "https://api.thecatapi.com/v1/votes/"
    response = requests.delete(url1 + vote_id, headers=headers_xapi)
    json_response = json.loads(response.text)
    print((json_response))
    print(response.status_code)
    assert response.status_code == 200, "Delete Successful for newly added ID"


@then(u'We should get 404 error trying to GET the deleted resource')
def objective6(context):
    url1 = "https://api.thecatapi.com/v1/votes/"
    response = requests.get(url1 + vote_id, headers=headers_xapi)
    json_response = json.loads(response.text)
    print((json_response))
    print(response.status_code)
    assert response.status_code == 404, "Did not get deleted Vote ID"
