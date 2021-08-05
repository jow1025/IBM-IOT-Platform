import wiotp.sdk
from time import sleep

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "hu5963", "typeId": "vDev", "deviceId": "vLamp"},
    "auth": {"token": "passw0rd"},
}

lamp = 'off'


def deviceAction(reqId, cmd):
    print(reqId, cmd)

def commandProcessor(cmd):
    global lamp
    if cmd.data["d"]["lamp"]:
        data = {}
        if cmd.data["d"]["lamp"] == "on":
            lamp = 'on'
            print("Lamp is On")
            data = {"d" : {"lamp" : "on"}}
        else:
            lamp = 'off'
            print("Lamp is Off")
            data = {"d" : {"lamp" : "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)

#deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli = wiotp.sdk.device.ManagedDeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.deviceActionCallback = deviceAction
deviceCli.connect()

def periodicPublish():
    data = {"d":{"lamp": lamp}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Lamp is " + lamp)

while True:
    periodicPublish()
    sleep(10)
