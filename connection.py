import urllib3
from urllib3.util.retry import Retry
from urllib3.exceptions import MaxRetryError

http = urllib3.PoolManager()

try:
    response = http.request('GET', 'http://localhost:8825/env/experiment_name')
    # Process the response
except MaxRetryError as e:
    print(f"Unable to connect to the server: {e}")
    # Handle the error, possibly by logging and retrying after a delay
