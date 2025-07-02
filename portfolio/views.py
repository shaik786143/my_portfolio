from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def experience(request):
    return render(request, 'portfolio/experience.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        try:
            send_mail(
                subject=f'Portfolio Contact Form: {name}',
                message=f'From: {name} <{email}>\n\n{msg}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['subhanishaikmb11@gmail.com'],
                fail_silently=False,
            )
            message = 'Your message has been sent successfully!'
        except Exception as e:
            message = 'There was an error sending your message. Please try again later.'
    return render(request, 'portfolio/contact.html', {'message': message})
