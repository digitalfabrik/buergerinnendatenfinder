from django.shortcuts import render
from .forms import CitizenDateForm
from .models import CitizenDate

DATE_TYPES = {
    'telephone': 'Telefonnummer',
    'e-mail': 'E-Mail-Adresse',
    'zipcode': 'Postleitzahl',
}

def index(request):
    context = {}
    if request.method == "POST":
        cdf = CitizenDateForm( request.POST )
        if cdf.is_valid():
            cdf.save()
        else:
            print(cdf.type_hash)
            cd = CitizenDate.objects.filter(type_hash=cdf.type_hash)
            context["date_type"] = DATE_TYPES[request.POST["date_type"]]
            context["cd"] = cd
    context["all_data"] = CitizenDate.objects.filter()
    context["citizen_date_form"] = CitizenDateForm()
    return render(request, "search.html", context)

