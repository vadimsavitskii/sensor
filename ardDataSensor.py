import re
import serial
from influxdb import InfluxDBClient
from datetime import datetime


client = InfluxDBClient(your credentials)

arduinoData = serial.Serial('com4', 115200)


while True:
    arduinoString = arduinoData.readline()
    arduinoStringValues = str(arduinoString)
    arduinoStringValuesFound = re.findall("[0-9]{1,3}\.[0-9]{2}", arduinoStringValues)

    humidity = float(arduinoStringValuesFound[0])
    light = float(arduinoStringValuesFound[1])
    temp = float(arduinoStringValuesFound[2])

    time = datetime.utcnow()

    json_body = [
        {
            "measurement": "Humidity",
            "time": time,
            "fields": {
                "humidity": humidity,
            }
        },
        {
            "measurement": "Light",
            "time": time,
            "fields": {
                "light": light,
            }
        },
        {
            "measurement": "Temperature in Celsius",
            "time": time,
            "fields": {
                "temp": temp,
            }}
    ]
    client.write_points(json_body)
    print(json_body)
