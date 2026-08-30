## test with Flask built-in test_client()
from app import app

client = app.test_client()

response = client.get("/healthz")
assert response.status_code == 200, f"/healthz returned {response.status.code}"
assert response.get_json()["status"] == "healthy"

response = client.get("/")
assert response.status_code == 200, f"/ returned {response.status.code}"

print("All checks passed")