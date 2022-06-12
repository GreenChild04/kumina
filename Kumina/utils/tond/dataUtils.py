import json


class DATA_UTILS:
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