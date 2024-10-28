# main.py

import threading
import time

import uvicorn

from fast_api import app as fastapi_app


def run_fastapi_server():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # Create threads for FastAPI servers
    fastapi_thread = threading.Thread(target=run_fastapi_server, daemon=True)

    # Start the servers
    fastapi_thread.start()

    print("Concord servers are running.")

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("Shutting down servers...")
