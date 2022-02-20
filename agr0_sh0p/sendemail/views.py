
from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    f'{subject} от {from_email}',
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    (from_email,)
                )
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('sendemail:success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "sendemail/email.html", {'form': form})

def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')