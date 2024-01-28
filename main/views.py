# main/views.py

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import telebot
from django.conf import settings

bot = telebot.TeleBot(settings.TOKEN_BOT)

@csrf_exempt
@require_POST
def webhook(request):
    json_str = request.body.decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return HttpResponse(''), 200
