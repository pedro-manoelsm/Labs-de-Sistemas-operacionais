import paho.mqtt.client as mqtt

broker_address = "localhost"
port = 1883
topic = "iot/sensores/temperatura"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Falha na conexão: {reason_code}")
    else:
        print("Conectado ao Broker MQTT!")
        client.subscribe(topic, qos=0)
        print(f"Inscrito no tópico: {topic}")

def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico '{msg.topic}': {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="dashboard_cliente_01")

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port, 60)

client.loop_forever()