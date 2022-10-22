import requests
from datetime import datetime
from tkinter import *

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = 'toyea'
TOKEN = 'erijfidfnnfvnd'
BOOK_READING_GRAPHID = 'bookreading'
BACKGROUND_COLOR = '#EAEAEA'
FONT = ('Arial', 20, 'italic')

today_day = datetime.now().date().day
today_month = datetime.now().date().month
today_year = datetime.now().date().year
today = f'{today_year}{today_month}{today_day}'

GRAPH_PIXELA_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
POST_PIXELA_ENDPOINT = f'{GRAPH_PIXELA_ENDPOINT}/{BOOK_READING_GRAPHID}'
UPDATE_PIXELA_ENDPOINT = f'{POST_PIXELA_ENDPOINT}/{today}'



parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_parameters = {
    'id': BOOK_READING_GRAPHID,
    'name': 'Book Reading Tracker',
    'unit': 'mins',
    'type': 'int',
    'color': 'ajisai'
}

post_parameters = {
    'date': today,
    'quantity': '3'
}

graph_parameters_header = {
    'X-USER-TOKEN': TOKEN
}

edit_parameters = {
    'quantity': '5'
}


# Making a new post

# response = requests.post(POST_PIXELA_ENDPOINT, json=post_parameters, headers=graph_parameters_header)
# print(response.text)

# Updating A previous post

# response = requests.put(url=UPDATE_PIXELA_ENDPOINT, headers=graph_parameters_header, json=edit_parameters)
# print(response.text)


# UI

# Window
windows = Tk()
windows.title('My Habit Tracker')
windows.config(width=500, height=500, pady=50, padx= 50, bg=BACKGROUND_COLOR)

#logo
canvas = Canvas(width=460, height=460, bg='white')
title = canvas.create_text(230, 35, text='Toye\'s Habit Tracker ✔', font=FONT)
canvas.grid(column=1, row=1, columnspan= 2)

#








windows.mainloop()