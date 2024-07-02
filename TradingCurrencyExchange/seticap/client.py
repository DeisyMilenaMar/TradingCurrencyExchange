from decouple import config
import requests
from datetime import datetime

class SeticapClient:
    def __init__(self, base_url, timeout):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.auth_token = config('SETICAP_AUTH_TOKEN')  # Get authorization token from environment variable
    
    def make_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': self.auth_token,
            'Content-Type': 'application/json'
        }
        
        try:
            response = self.session.post(url, json=data, headers=headers, timeout=self.timeout)
            response.raise_for_status()  # Throws an exception for 4xx/5xx response codes
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            return(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            return(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            return(f"An error occurred: {req_err}")

    def get_trm(self, fecha=None):
        if fecha is None:
            fecha = datetime.now().strftime('%Y-%m-%d')
        
        endpoint = "seticap/api/estadisticas/estadisticasPrecioMercado/"
        data = {
            "fecha": fecha,
            "mercado": 71,
            "delay": 15
        }
        return self.make_request(endpoint, data)
