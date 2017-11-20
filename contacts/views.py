from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from contacts.models import Contacts


def default(request):
    return render(request, 'contacts/input.html')


def search(request):
    all_contacts = Contacts.objects.all().order_by("name")[:50]
    template = loader.get_template('contacts/search_result.html')
    context = {
        'all_contacts': all_contacts,
    }

    return HttpResponse(template.render(context, request))
