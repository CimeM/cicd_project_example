import requests
import sys
import os


app_url = os.environ.get('APP_URL')
api_url = os.environ.get('API_URL')


# Test for return code 200
def test_web_request_200(url):
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

# test if ENV variable is defined
def test_env_variable(var_name, variable):
    if variable: 
         print(f"The {var_name} is: {variable}")
    else:
        print(f"The environment variable {var_name} is not set")


# launch tests here
if __name__ == "__main__":

    test_env_variable("APP_URL", app_url)
    test_env_variable("API_URL", api_url)
    
    test_web_request_200(app_url)  
    test_web_request_200(f"{api_url}/docs")
    
    print("All tests passed")
