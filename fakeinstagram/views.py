from email import message
import json
from django.http import HttpResponse


def hello_word(request):
    return HttpResponse("Hello word")


def sort_integer(request):
    """Remember that number variable has to be sent in the url as a paramater"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sort_ints = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sort_ints,
        'message': 'Integers sorted successfuly'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}. you are not allowed here.'.format(name)
    else:
        message = 'Welcome again {}'.format(name)

    return HttpResponse(message)
