import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # Retrieve environment variables
    env_a = os.getenv('a', 'Not Set')
    env_b = os.getenv('b', 'Not Set')
    env_c = os.getenv('c', 'Not Set')
    env_d = os.getenv('d', 'Not Set')

    # Return environment variables
    return {
        "a": env_a,
        "b": env_b,
        "c": env_c,
        "d": env_d
    }
