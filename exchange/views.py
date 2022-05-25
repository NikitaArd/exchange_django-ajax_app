from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import requests


def index(request):
    curr_table = requests.get('https://api.exchangerate-api.com/v4/latest/usd').json()
    curr_table = curr_table['rates']
    # if request.method == 'POST':
    #     amount = float(request.POST.get('amount') or 0)
    #     curr_from = request.POST.get('curr_from')
    #     curr_to = request.POST.get('curr_to')
    #     total = round((curr_table[curr_to] / curr_table[curr_from]) * amount, 2)
    #
    #     context = {
    #         'amount': amount,
    #         'curr_from': curr_from,
    #         'curr_to': curr_to,
    #         'total': total,
    #         'curr_table': curr_table,
    #     }
    # #     return render(request, 'exchange/index.html', context)
    # else:
    return render(request, 'exchange/index.html', {'curr_table': curr_table})


def post_index(request):
    curr_table = requests.get('https://api.exchangerate-api.com/v4/latest/usd').json()
    curr_table = curr_table['rates']

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'POST':

        amount = float(request.POST.get('amount') or 0)
        curr_from = request.POST.get('curr_from')
        curr_to = request.POST.get('curr_to')
        total = round((curr_table[curr_to] / curr_table[curr_from]) * amount, 2)

        context = {
            'amount': amount,
            'curr_from': curr_from,
            'curr_to': curr_to,
            'total': total,
            'curr_table': curr_table,
        }

        #srl_context = serializers.serialize('json', [context, ])

        return JsonResponse(context, status=200)
    else:
        context = {'amount ': 0}
        return JsonResponse({'context': context}, status=400)
