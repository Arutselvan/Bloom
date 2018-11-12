import requests
import urllib.parse
import json
import time


vi_url = "https://api.videoindexer.ai"
vi_account_id = "806129c8-59b7-43e0-9a5f-831be6dc3e1d"
vi_location = "trial"
vi_apiKey = "3d91d6c6f9a145cd9292d04d25cbd541"

headers = {
    'Ocp-Apim-Subscription-Key': '3d91d6c6f9a145cd9292d04d25cbd541',
}

r = requests.get("https://api.videoindexer.ai/auth/trial/Accounts/806129c8-59b7-43e0-9a5f-831be6dc3e1d/AccessToken?allowEdit=true",
        headers=headers,
    )

token = r.text.strip("\"")


# video_url = "lol"

upload_url = vi_url+ "/"+ vi_location+"/Accounts/"+vi_account_id+"/Videos?accessToken="+token+"&name=sample&description=sample_description&privacy=private&partition=some_partition"
form_data = {'file': open('/home/arut/tree.mp4', 'rb')}



# print (upload_url)


# url = "https://api.videoindexer.ai"
r = requests.post(upload_url, files=form_data)
# print(r.url)
print("Uploading done")
# print(json.dumps(r.json(), indent=2))

video_id = r.json()['id']

# data = {"accessToken": token, "language": "English"}

status = r.json()['state']

while status=="Processing":

    time.sleep(120)
    status_url= vi_url+"/"+vi_location+"/Accounts/"+vi_account_id+"/Videos/"+video_id+"/Index?accessToken="+token+"&language=English"
    r = requests.get(status_url)
    status = r.json()['state']


# status_url= vi_url+"/"+vi_location+"/Accounts/"+vi_account_id+"/Videos/"+video_id+"/Index?accessToken="+token+"&language=English"
# r = requests.get(status_url)
# print(json.dumps(r.json(), indent=2))
