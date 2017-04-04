from django.shortcuts import render

from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http import *
from django.template import *
import json
from django.template.response import TemplateResponse
from django.core import serializers
from .models import *
from json import dumps, loads
from django.template.context import RequestContext
from django.template import RequestContext, Context, Template
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
import time
from threading import Timer
from django.views.decorators.http import condition
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.pagesizes import landscape
# from reportlab.platypus import Image
# from reportlab.lib.units import inch
import csv
# import Image



# data_file = 'data.csv'

# def import_data(request):
#     # attendee_data = csv.reader(open(data_file,'rb'))
#     # for row in attendee_data:
#     last_name = 'gogineni'
#     first_name = 'ravi'
#     course_name = 'Pdf generator'
#     pdf_file_name = first_name+'.pdf'
#     generatecertificate(first_name,last_name,course_name,pdf_file_name)
#     return render(request,'home.html')

# def generatecertificate(first_name,last_name,course_name,pdf_file_name):
#     # import pdb; pdb.set_trace()
#     attendee_name = first_name+' '+last_name
#     c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))
#     # header test
#     c.setFont('Helvetica', 48, leading=None)
#     c.drawCentredString(415, 500, "Certificate of completion")
#     c.setFont('Helvetica',24, leading=None)
#     c.drawCentredString(415, 450, "This certificate is presented to:")
#     c.setFont('Helvetica-Bold',34, leading = None) 
#     c.drawCentredString(415,395, attendee_name)
#     c.setFont('Helvetica',24, leading = None)
#     c.drawCentredString(415,350,"for completing the fallowing course:")
#     c.setFont('Helvetica',20, leading = None)
#     c.drawCentredString(415,310,course_name)
#     # seal = Image("Capture.png")
#     # c.drawImage(seal,350,50,width=None,height=None)
#      # move the origin up and to the left
#     # c.translate(inch,inch)
#     # # define a large font
#     # c.setFont("Helvetica", 14)
#     # # choose some colors
#     # c.setStrokeColorRGB(0.2,0.5,0.3)
#     # c.setFillColorRGB(1,0,1)
#     # # draw some lines
#     # c.line(0,0,0,1.7*inch)
#     # c.line(0,0,1*inch,0)
#     # # draw a rectangle
#     # c.rect(0.2*inch,0.2*inch,1*inch,1.5*inch, fill=1)
#     # # make text go straight up
#     # c.rotate(90)
#     # # change color
#     # c.setFillColorRGB(0,0,0.77)
#     # # say hello (note after rotate the y coord needs to be negative!)
#     # c.drawString(0.3*inch, -inch, "Hello World")
#     c.showPage()
#     c.save()
# Create your views here.
def index(request):
    return render(request,'login.html')

@login_required
def home(request):
    return render(request,'home.html')
 
def login(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        try:
            user = authenticate(username= request.POST.get("inputEmail"), password= request.POST.get("inputPassword"))
            if user is not None:
                auth_login(request,user)
                return HttpResponseRedirect('home')
            else:
                return render(request, 'login.html',{
            'login_message' : 'Please Enter correct username and password.',})
        except:
            return render(request, 'login.html',{
            'login_message' : 'Enter the username and password correctly',})

# @login_required
# @condition(etag_func=None)        
# def gettime(request):
#     # import pdb;pdb.set_trace()
#     response = ''
#     response = StreamingHttpResponse(stream_response_generator())
#     # StreamingHttpResponse(stream_response_generator()) mimetype='text/html'
#     return  response


# def stream_response_generator():
#    while True:
#        time.sleep(1)
#        yield time.strftime("%H:%M:%S", time.localtime(time.time()))
def pageredirect(request, name):
    """dynamic link to get urls"""
    if name != "":
        return render(request, name+'.html')
    else:
        return home


def createpsc(request):
    if request.method == "POST":
        import pdb;pdb.set_trace()
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        print data
    return render( 'createPSC.html', data)
