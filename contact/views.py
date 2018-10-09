from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import contact
# Create your views here.


def contact(request):
        title = 'Contact'
        form = contactForm()
        context = {'title': title, 'form': form,}

        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            time_added = form.cleaned_data['time_added']
            subject = 'Message from alayo,com'
            message = '%s %s' %(comment, name, time_added)
            emailFrom = form.cleaned_data['email']
            emailTo = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
            confirm_message = "Thanks for the message."

            template = 'contact.html'
        return render(request, 'contact.html', context)
