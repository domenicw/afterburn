import api as netAPI
import datetime as datetime
from random import randrange
import json

class AfterburnNode(object):

    resparking = False
    sparkFactor = 1.0

    resparkIndex = 0
    resparkChangeTime = 5
    resparkTempDelta = 40
    resparkCODelta = 650
    resparkO2Delta = 13
    resparkHumidityDelta = 40

    def __init__(self, nodeid, token):
        self.nodeid = nodeid
        self.index = 1
        self.api = netAPI.API(nodeid, token)
        self.location = self.makeLocation()
        self.tempMax = randrange(40, 65)
        self.coMax = randrange(400, 700)
        self.o2Max = randrange(18, 20)
        self.humMax = randrange(10, 20)

    def nextPackage(self):
        values = self.readValue()
        return self.makePackage(values)

    def readValue(self):
        temperature = randrange(self.tempMax-6, self.tempMax)
        co = randrange(self.coMax-40, self.coMax)
        o2 = randrange(self.o2Max-4, self.o2Max)
        hum = randrange(self.humMax-3, self.humMax)
        if self.resparking:
            if self.resparkIndex < self.resparkChangeTime:
                temperature += self.resparkIndex * self.resparkTempDelta * self.sparkFactor / self.resparkChangeTime
                co += self.resparkIndex * randrange((self.resparkCODelta-100), self.resparkCODelta) * self.sparkFactor / self.resparkChangeTime
                o2 -= self.resparkIndex * randrange(self.resparkO2Delta-2, self.resparkO2Delta) * self.sparkFactor / self.resparkChangeTime
                hum += self.resparkIndex * self.resparkHumidityDelta * self.sparkFactor / self.resparkChangeTime
                self.resparkIndex += 1
            else:
                temperature += self.resparkTempDelta * self.sparkFactor
                co += self.resparkCODelta * self.sparkFactor
                o2 -= self.resparkO2Delta * self.sparkFactor
                hum += self.resparkHumidityDelta * self.sparkFactor
        elif not self.resparking and self.resparkIndex > 0:
            temperature += self.resparkIndex * self.resparkTempDelta * self.sparkFactor / self.resparkChangeTime
            co += self.resparkIndex * self.resparkCODelta * self.sparkFactor / self.resparkChangeTime
            o2 -= self.resparkIndex * self.resparkO2Delta * self.sparkFactor / self.resparkChangeTime
            hum += self.resparkIndex * self.resparkHumidityDelta * self.sparkFactor / self.resparkChangeTime
            self.resparkIndex -= 1

        return {"CO": co, "temperature": temperature, "O2": o2, "humidity": hum}

    def makePackage(self, readings):
        payload = {
            "timestamp": datetime.datetime.now().strftime('%s'),
            "device-id": self.nodeid,
            "loc": self.location,
            "readings": readings
        }

        return json.dumps(payload)

    def makeLocation(self):
        lat = randrange(39890, 40000) / 1000.0
        lon = -1 * randrange(122760, 122900) / 1000.0

        return {"lat": lat, "lon": lon}

    def sendNextPackage(self):
        package = self.nextPackage()
        success = self.api.sendPayload(package)
        return success
