import requests
from datetime import datetime

# ------------step-1: create a user id----------------

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "roXXXXXnghxxxx"
TOKEN = "roXXXXXXXXXnghxxx"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# --------------step-2&3: crate a graph and get the graph--------------

# graph_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "cycling",
    "unit": "km",
    "type": "float",
    "color": "shibafu",  # japanese name of green
}

header = {
    "X-USER-TOKEN": TOKEN,  # more secure way to provide key
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)


# --------------step-3: post values to the graph--------------

# today = datetime(year=2023, month=10, day=12)  # formated_date = today.strftime("%Y%m%d, %H:%S, %I:%S %p") # print(formated_date)

today = datetime.now()
print(today.strftime("%Y%m%d"))

graph_value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many km did you cycle today: "),
}

# response = requests.post(url=graph_value_endpoint, json=value_params, headers=header)
# print(response.text)


# --------------step-4: updating a piece of data----------------

update_endpoint = f"{graph_value_endpoint}/{20231009}"   # update this date's data

update_pixel = {
    "quantity": "30.5"
}

# response = requests.put(url=update_endpoint, json=update_pixel, headers=header)
# print(response.text)

graph_update_endpoint = f"{graph_value_endpoint}"
update_parameter = {
    "timezone": "Asia/Kolkata",     # adding timezone in graph
}

response = requests.put(url=graph_update_endpoint, json=update_parameter, headers=header)
print(response.text)


# -------------step-5: delete a piece of data-------------

delete_endpoint = f"{graph_value_endpoint}/{20231010}"      # delete this date's data

# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)










