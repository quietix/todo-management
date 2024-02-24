from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from telebot.types import Update
from bot.bot_handlers import txt_handlers
from bot.setup_bot import BOT



@csrf_exempt
def index(request):
    if request.method == "POST":
        try:
            update = Update.de_json(request.body.decode('utf-8'))
            BOT.process_new_updates([update])
        except Exception as e:
            print(e)
        return HttpResponse('', status=200)

    elif request.method == "GET":
        return HttpResponse('OK', status=200)

    else:
        return Http404
