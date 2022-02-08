import requests 

URL = "http://127.0.0.1:5000/users"

EXAMPLE_JSON = {
    "firs_name": "John",
    "last_name": "Doe",
    "hobbies": "Playing video game"
}

def create_user(first_name, last_name, hobbies):
    user_json = EXAMPLE_JSON 
    user_json["first_name"] = first_name
    user_json["last_name"] = last_name
    user_json["hobbies"] = hobbies

    out = requests.post(URL, json=user_json)
    if out.status_code == 201:
        print("User created.")
    else:
        print(
            "Something wen wrong while "
            "trying to create a new user.")
            
if __name__ == "__main__":
    first_name = input("Type in the desired first name: ")
    last_name = input("Type in the desired last name: ")
    hobbies = input("Type in the desired hobbies: ")
    create_user(first_name, last_name, hobbies)
    