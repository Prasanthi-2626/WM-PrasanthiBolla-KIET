import paho.mqtt.client as mqtt
import json
import time
from config import MQTT_BROKER, MQTT_PORT

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)

def publish_bin_data(zone, bin_id, fill_level, confidence):
    payload = {
        "bin_id": bin_id,
        "fill_level": fill_level,
        "confidence": confidence,
        "timestamp": time.time()
    }
    topic = f"waste/{zone}/bins"
    client.publish(topic, json.dumps(payload))

# Simulated event-driven publishing
while True:
    publish_bin_data("Zone_A", "BIN_01", 92, 0.94)
    time.sleep(10)
