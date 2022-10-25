import requests
from celery import shared_task


@shared_task()
def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url).json()
    joke = response['value']

    print(joke)
    return joke
