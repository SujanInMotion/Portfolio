from django.shortcuts import render
from django.shortcuts import render,loader
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import BadHeaderError
from django.http import HttpResponseForbidden

# Create your models here.
def home(request):
    template =loader.get_template("index.html")
    return HttpResponse(template.render())




def send_email(request):
    if request.method == 'POST':
        username = request.POST['username']
        user_email = request.POST['email']
        message = request.POST['message']

        # Construct the email message
        subject = f"Message from {username}"
        body = f"Name: {username}\nEmail: {user_email}\n\nMessage:\n{message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['sujanprogrammer@gmail.com']  # Your email address

        try:
            send_mail(subject, body, from_email, recipient_list)
            return HttpResponse('Message sent successfully.')
        except BadHeaderError:
            return HttpResponseForbidden('Invalid header found.')
    return render(request, 'contact_form.html')
