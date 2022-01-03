from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def contact_form(request):
    return render(request, "contact_form.html")

def contact(request):
    template = "contact_form.html"
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email:" + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["franalibello@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        template = "contact_susess.html"

    return render(request, template)
