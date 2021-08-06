import wiotp.sdk
import sys
import json
import time

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "due986", "typeId": "vDev", "deviceId": "vSwitch"},
    "auth": {"token": "passw0rd"},
}

if len(sys.argv) != 2:
    print("\n    Usage iotremote.py on|off \n")
    sys.exit(1)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.connect()

print("")
data = {"d" : {"switch" : sys.argv[1]}}
deviceCli.publishEvent("status", "json", data, qos=0)
print("Sending the Command => " + json.dumps(data))
time.sleep(2)
