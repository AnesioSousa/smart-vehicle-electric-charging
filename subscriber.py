import random

from paho.mqtt import client as mqtt

broker = 'broker.emqx.io'
port = 1883
topic = "SMRT001/teste"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0,100)}'

username = 'emqx'
password = 'public'


def connect_mqtt() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to MQTT Broker with result code {rc}")
        else:
            print("Failed to connect, return code %d\n", rc)
    
    client = mqtt.Client(client_id)
    client.username_pw_set = (username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message
    
    
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    
if __name__ == '__main__':
    run()