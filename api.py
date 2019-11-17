import http.client
from base64 import b64encode

class API(object):

    def __init__(self, deviceID, token):
        self.baseURL = "87p5n9.messaging.internetofthings.ibmcloud.com"
        self.postURL = "/api/v0002/device/types/afterburner-node/devices/{0}/events/simulation".format(deviceID)
        userAndPass = b64encode(bytes('use-token-auth:' + token)).encode("utf-8")
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'Basic %s' %  userAndPass}

    def sendPayload(self, payload):
        con = http.client.HTTPSConnection(self.baseURL, 443)
        con.request('POST', self.postURL, payload, self.headers)
        response = con.getresponse()
        return response.status
