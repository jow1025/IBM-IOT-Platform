import wiotp.sdk
from utils import buttonSwitch as button

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "due986", "typeId": "vDev", "deviceId": "vSwitch"},
    "auth": {"token": "passw0rd"},
}

# Define our switch function
sw = 'off'
def switch():
    global sw
    if sw == 'on':
        button.buttonOff()
        sw = 'off'
        data = {"d" : {"switch" : "off"}}
    else:
        button.buttonOn()
        sw = 'on'
        data = {"d" : {"switch" : "on"}}
    deviceCli.publishEvent("status", "json", data, qos=0)
button.on_button.config(command = switch)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.connect()

while button.x == True:
    button.update()
