import requests
import time
import subprocess
import json

def get_node_ips():
    result = subprocess.run(["kubectl", "get", "nodes", "-o", "json"], capture_output=True, text=True)
    nodes = json.loads(result.stdout)
    node_ips = [addr['address'] for node in nodes['items'] for addr in node['status']['addresses'] if addr['type'] == 'InternalIP']
    return node_ips

def get_node_port():
    result = subprocess.run(["kubectl", "get", "svc", "color-grid", "-o", "jsonpath={.spec.ports[0].nodePort}"], capture_output=True, text=True)
    return result.stdout.strip()

def send_requests(node_ips, node_port):
    while True:
        for node_ip in node_ips:
            url = f"http://{node_ip}:{node_port}/"
            try:
                print(f"Sending request to {url}")
                response = requests.get(url)
                print("Response:", response.status_code)
            except requests.RequestException as e:
                print("Request failed:", e)
            time.sleep(1)  # adjust the sleep time as necessary

if __name__ == "__main__":
    node_ips = get_node_ips()
    node_port = get_node_port()
    send_requests(node_ips, node_port)
