import requests
# Define API URLs and headers

MONSTER_API_URL = "https://api.mlsakiit.com/monsters"
SURVIVORS_API_URL = "https://api.mlsakiit.com/survivors"
RESOURCES_API_URL = "https://api.mlsakiit.com/resources"



# 1. DataFetcher Class
class DataFetcher:
    @staticmethod
    def fetch_monster_data():
        try:
            response = requests.get(MONSTER_API_URL, headers={"accept": "application/json"})
            response.raise_for_status()
            return response.json().get("monsters", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching monster data: {e}")
            return [{"monster_id": "unknown", "lat": 0, "lon": 0}]  # Default fallback

    @staticmethod
    def fetch_resource_data():
        try:
            response = requests.get(RESOURCES_API_URL, headers={"accept": "application/json"})
            response.raise_for_status()
            return response.json().get("features", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching resource data: {e}")
            return []

    @staticmethod
    def fetch_survivor_data():
        try:
            response = requests.get(SURVIVORS_API_URL, headers={"accept": "application/json"})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching survivor data: {e}")
            return []