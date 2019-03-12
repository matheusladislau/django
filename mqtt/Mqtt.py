import paho.mqtt.client as mqtt
import mqtt_config

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(mqtt_config.topic)



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #print(str(msg.payload))

def setClient():
    client = mqtt.Client()
    client.username_pw_set(mqtt_config.username,mqtt_config.password)
    return client

def sub():
    client=setClient()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(mqtt_config.host, mqtt_config.port, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.

    client.loop_forever()

def pub(topic,value):
    client = client=setClient()

    topic=mqtt_config.topic+'/'+topic
    client.connect(mqtt_config.host,mqtt_config.port, 60)
    client.publish(topic,value)
