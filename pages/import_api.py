import requests

#Estructura basada en POM
class ImportAPI:
    BASE_URL = "https://api.test.worldsys.ar/import"

    #seteo del token
    def __init__(self, token):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def import_person(self, person_id):
        payload = [{"personId": person_id}]
        try:
            response = requests.post(self.BASE_URL, json=payload, headers=self.headers)
            print(f"Request payload: {payload}")
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.text}")
            return response
        except requests.RequestException as error:
            print(f"Error en la petición: {error}")
            return None

    def import_person_raw(self, payload):
        try:
            response = requests.post(self.BASE_URL, json=payload, headers=self.headers)
            print(f"Request payload: {payload}")
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.text}")
            return response
        except requests.RequestException as error:
            print(f"Error en la petición: {error}")
            return None