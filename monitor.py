import requests
import time

URL = "http://localhost:5001/health"

print("📡 Starting service monitor loop (Press Ctrl+C to stop)...")
while True:
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print(f"💚 [SAFE] Service Health Check Passed: {response.json()}")
        else:
            print(f"⚠️ [WARNING] Unexpected status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"🚨 [CRITICAL ALERT] Heart Disease Prediction Service is DOWN! Error: {e}")
    
    time.sleep(10)  # Check every 10 seconds