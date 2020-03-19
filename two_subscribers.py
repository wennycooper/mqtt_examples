import paho.mqtt.client as mqtt
import time

def on_connect1(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("kkuei1")

def on_connect2(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("kkuei2")

def on_message_callback1(mosq, obj, msg):
    print("cb1 MESSAGES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload.decode("utf-8", "ignore")))

def on_message_callback2(mosq, obj, msg):
    print("cb2 MESSAGES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload.decode("utf-8", "ignore")))

mqttc1 = mqtt.Client()
mqttc1.on_connect = on_connect1
mqttc1.on_message = on_message_callback1
mqttc1.connect("localhost", 1883, 60)
mqttc1.loop_start()

mqttc2 = mqtt.Client()
mqttc2.on_connect = on_connect2
mqttc2.on_message = on_message_callback2
mqttc2.connect("localhost", 1883, 60)
mqttc2.loop_start()

while 1:
    time.sleep(1)
    




