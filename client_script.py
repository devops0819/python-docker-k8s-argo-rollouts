import requests
import time

for i in range(1, 10000):
    requests.get('http://a9da78c8e751a4b4b926f843bd9d1a96-1816739119.ap-south-1.elb.amazonaws.com:5000/')