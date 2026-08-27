import requests
from celery import shared_task

from config.settings import TG_API_KEY
from habits.models import Habit


@shared_task
def create_periodic_tasks():
    habits = Habit.objects.all()
    for habit in habits:
        text = f"Я буду {habit.action} в {habit.time} в {habit.place}."
        send_message(text, habit.owner.chat_id)


@shared_task
def send_message(text, chat_id):
    params = {
        "chat_id": chat_id,
        "text": text
    }
    requests.get(f"https://api.telegram.org/bot{TG_API_KEY}/sendMessage", params=params).json()
