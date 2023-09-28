from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
import json
import os
import signal
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from twilio.rest import Client
import openai
import langchain
#export OPENAI_API_KEY="Medicine"
import os
from langchain.llms import OpenAI
from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm,NameForm1
import os
from twilio.rest import Client



from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            Search = form.cleaned_data["Search"]
            print(type(Search))

            openai.api_key = os.getenv("openai_api_key")

            from langchain.llms import OpenAI

            llm = OpenAI(openai_api_key="openai_api_key")

            from langchain.llms import OpenAI

            llm = OpenAI()

            resp = llm.predict(Search)
            
            return render(request, "index.html", {"form": resp})

    else:
        form = NameForm()

    return render(request, "index.html", {"form": form})

def make_call(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm1(request.POST)
        # check whether it's valid:
        if form.is_valid():

            Message_On_Call = form.cleaned_data["Message"]
            NumbertoCall = form.cleaned_data["NumbertoCall"]
            print(type(NumbertoCall))
            Num_list = NumbertoCall.split(",")
            # Find your Account SID and Auth Token at twilio.com/console
            # and set the environment variables. See http://twil.io/secure
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            for Num in Num_list:

                call = client.calls.create(
                                        twiml='<Response><Say>'+Message_On_Call+'</Say></Response>',
                                        to='+91'+Num,
                                        from_='+918708115075'
                                    )

                print(call.sid
                ) 
                print(call.events)
                status=str(call.sid)
            if status:
                result = "Call been successfully made"
                return render(request, "call.html", {"form": result})

    else:
        form = NameForm1() 

    return render(request, "call.html", {"form": form})


def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        username = request.POST.get("exampleInputName1")
        print(username)
        return HttpResponse("student form is created successfully")
    return render(request , 'index.html')


@api_view(["POST"])
def Search_view(request):
    if request.method == 'POST':
        
        # llm = OpenAI(temperature=0.3)
        # print(llm.predict("what is the capital of delhi"))
        
        print(request.data)



        
        openai.api_key = os.getenv("openai_api_key")

        from langchain.llms import OpenAI

        llm = OpenAI(openai_api_key="openai_api_key")

        from langchain.llms import OpenAI

        llm = OpenAI()

        resp = llm.predict("Medical store phone numbers  in Hisar ")

        #print(type(llm.predict("Medical store phone numbers  in Hisar ")))
        return Response(resp) 

@api_view(["POST"]) 
def call_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        print(form)


      # Download the helper library from https://www.twilio.com/docs/python/install
        import os
        from twilio.rest import Client


        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        call = client.calls.create(
                                twiml='<Response><Say>Hi PK</Say></Response>',
                                to='+919467389160',
                                from_='+918708115075'
                            )

        print(call.sid
        ) 
        print(call.events)
        status=str(call.sid)
        return Response(status)    
       

        

# Create your views here.


