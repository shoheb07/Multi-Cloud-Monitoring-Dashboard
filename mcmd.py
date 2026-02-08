from fastapi import FastAPI
import psutil
import platform
import time

app = FastAPI(title="Multi-Cloud Monitor")

START_TIME = time.time()

def uptime():
    return round(time.time() - START_TIME, 2)

@app.get("/")
def root():
    return {
        "message": "Multi-Cloud Monitoring Dashboard",
        "status": "running"
    }

@app.get("/system")
def system_info():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
        "uptime_seconds": uptime()
    }

@app.get("/metrics")
def metrics():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent
    }

@app.get("/cloud")
def cloud_example():
    return {
        "aws": "connected (mock)",
        "azure": "connected (mock)",
        "gcp": "connected (mock)"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
