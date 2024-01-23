from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "POST":
        try:
            pass
            # update = Update.de_json(request.body.decode('utf-8'))
            # bot.process_new_updates([update])
            # bot.add_message_handler({"/start": handlers.start,
            #                          "/help": handlers.help,
            #                          "/register": handlers.register,
            #                          "/menu": handlers.register})
        except Exception as e:
            print(str(e))
        return HttpResponse('', status=200)

    elif request.method == "GET":
        return HttpResponse('OK', status=200)

    else:
        return Http404
