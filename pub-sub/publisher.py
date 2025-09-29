import paho.mqtt.client as mqtt
import time
import random
import json

broker_address = "localhost"
port = 1883
topic = "iot/sensores/temperatura"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Falha na conexão: {reason_code}")
    else:
        print("Conectado ao Broker MQTT!")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="sensor_temperatura_01")
client.on_connect = on_connect

client.connect(broker_address, port)

client.loop_start()

try:
    while True:
        temperatura = round(random.uniform(20.0, 30.0), 2)
        umidade = round(random.uniform(50.0, 70.0), 2)
        
        payload = {
            "temperatura": f"{temperatura}°C",
            "umidade": f"{umidade}%"
        }
        payload_str = json.dumps(payload)

        result = client.publish(topic, payload_str, qos=0)
        
        status = result[0]
        if status == 0:
            print(f"Enviado para o tópico '{topic}': {payload_str}")
        else:
            print(f"Falha ao enviar mensagem para o tópico {topic}")

        time.sleep(2)

except KeyboardInterrupt:
    print("Publicação encerrada.")
    client.loop_stop()
    client.disconnect()