#!/usr/bin/python
import requests, json

def updateBanner(bannerText):
    url = "https://api.thingspeak.com/update"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"api_key\"\r\n\r\nJG2SKAQ2AYXXL6IJ\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"field1\"\r\n\r\n" + bannerText + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

    headers = {
                'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                'cache-control': "no-cache",
                'postman-token': "17c41886-fdd4-a12a-b0e9-e327108408a3"
              }

    response = requests.request("POST", url, data=payload, headers=headers)

def getBanner():
    url = "https://api.thingspeak.com/channels/222373/feeds.json"

    headers = {
                'api_key': "M66NL66T6TH1QMKJ",
                'cache-control': "no-cache",
                'postman-token': "ba703d21-cd97-17a2-54c1-838c9f5bc2aa"
              }

    response = requests.request("GET", url, headers=headers)

    index = len(response.json()["feeds"]) - 1
    bannerText = response.json()["feeds"][index]["field1"]

    return bannerText
