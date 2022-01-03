from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def contact_form(request):
    return render(request, "contact_form.html")

def contact(request):
    if request.method == "post":
        import pdb; pdb.set_trace()
        asunto = request.post["txtAsunto"]
        mensaje = request.post["txtMensaje"] + " / Email:" + request.post["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["franalibello@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contact_susess.html")
    return render(request, "contact_form.html")
