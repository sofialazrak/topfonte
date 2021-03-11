from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category, Product
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def landing(request):
    return render(request, 'pages/landing.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Top-Fonte Website Inquiry"
            body = {
			    'name': form.cleaned_data['name'], 
			    'company': form.cleaned_data['company'], 
			    'email': form.cleaned_data['email'], 
			    'message':form.cleaned_data['message'], 
			}
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, body['email'], ['sofia.lazrak@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect('contact/')
            messages.success(request, 'Votre demande a bien été enregistrée. Nous vous contacterons dans les plus brefs délais.')
    return render(request, "pages/contact.html", {'form': form})

			