import requests
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def Homepage(request):
    return render(request, 'Base.html')


def Customer(request):
    return render(request, 'Main/Cust.html')


def manager(request):
    return render(request, 'Main/Man.html')


def Message(request, PhoneNumber):
    import requests
    defaultNumber = 6352512793
    url = "https://www.fast2sms.com/dev/bulk"
    message = datetime.datetime.now
    querystring = {"authorization":"O5hePUfZv1wY5lc8HF5zq4iA3wYdnl4GbK7mm8mVRInOftNeulbzLFSVXGfW","sender_id":"FSTSMS",
                   "message":"This is test message","language":"english","route":"p","numbers": PhoneNumber}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    returnMessage = response.text

    querystring = {"authorization": "O5hePUfZv1wY5lc8HF5zq4iA3wYdnl4GbK7mm8mVRInOftNeulbzLFSVXGfW",
                   "sender_id": "FSTSMS",
                   "message": "This is test message", "language": "english", "route": "p", "numbers": defaultNumber}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return HttpResponse(returnMessage + response.text)


def Textway2smsMessage(request, phone_number):
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'

    # get request

    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {
            'apikey': apiKey,
            'secret': secretKey,
            'usetype': useType,
            'phone': phoneNo,
            'message': textMessage,
            'senderid': senderId
        }
        return requests.post(reqUrl, req_params)

    # get response

    response = sendPostRequest(URL, 'T6K7DL0TFN49AGY9I86W8ZFVMYUH4KLO', 'W1E5E2WN4TISIQ5K', 'stage', phone_number,'mananv1791@gmail.com',"This message is sent by bot,Have a nice day")

    print(response.text)

    return HttpResponse('Message Sent Successfully')