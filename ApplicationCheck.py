import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        # Checking if the HTTP status code is 200 (OK)
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException as e:
        # If there is any exception (e.g., connection error, timeout), consider the application 'down'
        print(f"An error occurred: {e}")
        return 'down'

if __name__ == "__main__":
    # URL of the application to be checked
    app_url = "https://jharsewa.jharkhand.gov.in"
    
    status = check_application_status(app_url)
    print(f"The application is {status}.")
