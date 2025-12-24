import requests

URL = "http://localhost:8003/ingest"

for i in range(1000):
    r = requests.post(
        URL,
        headers={"X-Tenant-ID": "tenant-a"},
        json={"text": f"Confidential document number {i}"}
    )
    if i % 100 == 0:
        print(f"Ingested {i} docs")