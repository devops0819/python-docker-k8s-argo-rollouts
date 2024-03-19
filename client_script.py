import requests
import time

url = 'http://a9da78c8e751a4b4b926f843bd9d1a96-1816739119.ap-south-1.elb.amazonaws.com:5000/'

for i in range(1, 10):
    # requests.get('http://a9da78c8e751a4b4b926f843bd9d1a96-1816739119.ap-south-1.elb.amazonaws.com:5000/')
    # print (requests.Response.status_code)

    response = requests.get(url)

    if response.status_code == 200:
        # Print the content of the response
        print(response.text)
    else:
        # Print the status code if the request was not successful
        print(f"Failed to retrieve content: HTTP {response.status_code}")