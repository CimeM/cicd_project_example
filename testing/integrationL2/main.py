import requests
import sys
import os


api1_url = os.environ.get('API1_URL')
api2_url = os.environ.get('API2_URL')


# Test for return code 200
def test_web_request_200(url):
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

# launch tests here
if __name__ == "__main__":

    test_web_request_200(f"{api2_url}/count_landmark")
    
    print("All tests passed")
