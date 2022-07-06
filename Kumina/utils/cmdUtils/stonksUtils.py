import json
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
import http.client


class StonksUtils:
    def __init__(self):
        pass

    def saveToJsonString(self, keyword, inpit, item):
        data = json.loads(item)
        data[keyword] = inpit
        item_2 = json.dumps(data)
        return item_2

    def loadFromJsonString(self, keyword, item):
        data = json.loads(item)
        output = data[keyword]
        return output

    def getData(self, region, company):
        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
            'X-RapidAPI-Host': "yh-finance.p.rapidapi.com"
        }
        conn.request("GET", f"/auto-complete?q={company}&region={region}", headers=headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
