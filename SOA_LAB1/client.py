import requests

BASE_URL = "http://localhost:5000/users"

def print_response(response):
    try:
        response.raise_for_status()
        try:
            print(response.json())
        except ValueError:
            print("Non-JSON response:", response.text)
    except requests.exceptions.HTTPError as http_err:
        try:
            print("HTTP error:", response.status_code, response.json())
        except Exception:
            print("HTTP error:", response.status_code, response.text)
    except requests.exceptions.RequestException as err:
        print("Request failed:", err)

def main():
    # Create a new user
    print("Creating user...")
    response = requests.post(BASE_URL, json={"name": "Alice", "email": "alice@example.com"})
    print_response(response)

    # Get all users
    print("\nGetting all users...")
    response = requests.get(BASE_URL)
    print_response(response)

    # Update user with ID 1
    print("\nUpdating user 1...")
    response = requests.put(f"{BASE_URL}/1", json={"name": "Alice Cooper", "email": "alice@cooper.com"})
    print_response(response)

    # Get user with ID 1
    print("\nGetting user 1...")
    response = requests.get(f"{BASE_URL}/1")
    print_response(response)

    # Delete user with ID 1
    print("\nDeleting user 1...")
    response = requests.delete(f"{BASE_URL}/1")
    print_response(response)

    # Try to get deleted user
    print("\nGetting deleted user 1...")
    response = requests.get(f"{BASE_URL}/1")
    print_response(response)

if __name__ == "__main__":
    main()
