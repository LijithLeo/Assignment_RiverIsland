import requests
import json
import jsonpath

base_url = 'https://api.thecatapi.com/v1/votes'
headers_xapi = {
    "x-api-key": "DEMO-API-KEY"
}
headers_xapip = {
    "x-api-key": "DEMO-API-KEY",
    "Content-Type": "application/json"
}
assert base_url != "", "Base URL is empty"
assert headers_xapi != "", "Header is empty"
response = requests.get(base_url, headers = headers_xapi)
#print(response.content)
json_response = json.loads(response.text)
print((json_response))
print(response.status_code)
#print(type(response.status_code))
print(type(json_response))
assert response.status_code == 200, "Get Request is successful"




#for i in json_response:
#    print(i['id'])

#get the random ID
ID1 = json_response[1]['id']
print(ID1)
assert ID1 == 31099, "correct ID"

#for match in jsonpath.jsonpath(json_response, 'id'):
#    print(match)

#Post data
new_resource = "{\"image_id\":\"asf2\",\"sub_id\":\"my-user-1234\",\"value\":1}"

r = requests.post(base_url, headers = headers_xapip, data=new_resource)
print(r.status_code)
assert r.status_code == 200, "POST Successful"

jr=(r.json())
vote_id = str((jr['id']))


#Get specific Vote

url1= "https://api.thecatapi.com/v1/votes/"
response = requests.get(url1+vote_id, headers = headers_xapi)
json_response = json.loads(response.text)
print((json_response))
print(response.status_code)
assert response.status_code == 200, "GET Successful for newly added ID"

#Delete the newly added Vote
url1= "https://api.thecatapi.com/v1/votes/"
response = requests.delete(url1+vote_id, headers = headers_xapi)
json_response = json.loads(response.text)
print((json_response))
print(response.status_code)
assert response.status_code == 200, "Delete Successful for newly added ID"

#Get the Deleted Vote

url1= "https://api.thecatapi.com/v1/votes/"
response = requests.get(url1+vote_id, headers = headers_xapi)
json_response = json.loads(response.text)
print((json_response))
print(response.status_code)
assert response.status_code == 404, "Didnot get deleted Vote ID"


















