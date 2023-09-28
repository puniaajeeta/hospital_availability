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
#from .forms import NameForm,NameForm1
from .forms import NameForm1
import os
from twilio.rest import Client



from django.http import HttpResponseRedirect
from django.shortcuts import render

#from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    print("Inside post metod.......$$$......")
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        #form = NameForm(request.POST)

        

        # check whether it's valid:
        # if form.is_valid():

        #     Search = form.cleaned_data["search"]
        #     print(type(Search))

        #     openai.api_key = os.getenv("openai_api_key")

        #     from langchain.llms import OpenAI

        #     llm = OpenAI(openai_api_key="openai_api_key")

        #     from langchain.llms import OpenAI

        #     llm = OpenAI()

        #     resp = llm.predict(Search)
            
        #     return render(request, "index.html", {"form": resp})
        print("Inside post metod.............")

        Search = request.POST.get('search')
        print(Search)


        # if form.is_valid():

        #     Search = form.cleaned_data["search"]
        #     print(type(Search))
        openai.api_key = os.getenv("openai_api_key")

        from langchain.llms import OpenAI

        llm = OpenAI(openai_api_key="openai_api_key")

        from langchain.llms import OpenAI

        llm = OpenAI()

        resp = llm.predict(Search)
        print(".......................",resp)
        
        return render(request, "index.html", {"form": resp})

    else:
        #form = NameForm()

       # return render(request, "index.html", {"form": form})
        return render(request, "index.html")

def make_call(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        #form = NameForm1(request.POST)
        print('here comes the control .....................')
        Message_On_Call = request.POST.get('message')
        print('.....................',Message_On_Call)
        NumbertoCall = request.POST.get('number')
        print('.....................',NumbertoCall)
        print(type(NumbertoCall))
        # check whether it's valid:
        #if form.is_valid():

        # Message_On_Call = form.cleaned_data["Message"]
        # NumbertoCall = form.cleaned_data["NumbertoCall"]
        # print(type(NumbertoCall))
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
       # form = NameForm1() 

       # return render(request, "call.html", {"form": form})
        return render(request, "call.html")


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









    



import time
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.views.generic import View  
from django.shortcuts import render
from django.http import StreamingHttpResponse
from rest_framework import status
#from faker import Faker
import speech_recognition
import pyttsx3


FLAG = True


# Create your views here.

class StreamGeneratorView(APIView):
    def get(self,request): 

        recognizer = speech_recognition.Recognizer()
       
       # while FLAG:
        try:
            with speech_recognition.Microphone() as mic:
                #print(flag_no)
                recognizer.adjust_for_ambient_noise(mic ,duration =0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text  = text.lower()
                print(f"Recognized{text}")
                #flag_no = flag_no+1
                response =  StreamingHttpResponse(text,status=200, content_type='text/event-stream')
                response['Cache-Control']= 'no-cache',
                return response
        
        except speech_recognition.UnknownValueError:
            response =  StreamingHttpResponse(text,status=200, content_type='text/event-stream')
            response['Cache-Control']= 'no-cache',
            return response    



@api_view(["POST"]) 
def Flag_view(request):
    if request.method == 'GET':
        FLAG =False
        response =  StreamingHttpResponse("Listining process has been stopped",status=200, content_type='text/event-stream')
        response['Cache-Control']= 'no-cache',
        return response 

    


class HomeView(View): 

    def get(self,request):
        return render(request,'index.html')


