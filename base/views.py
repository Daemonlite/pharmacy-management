from django.shortcuts import get_object_or_404, redirect, render
from base.models import Drug

from django.contrib import messages
from base.forms import DrugForm  
import logging

logger = logging.getLogger(__name__)
# Create your views here.


def home(request):
    drugs = Drug.objects.all()

    search_query = request.GET.get("search", "")
    if search_query:
        drugs = Drug.objects.filter(name__icontains=search_query)

    context = {"drugs": drugs, "search_query": search_query}
    return render(request, "base/home.html", context)
    



def add_drug(request):
    if request.method == "POST":
        form = DrugForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Drug created successfully.")
            return redirect('home')  
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = DrugForm()

    return render(request, "base/add_drug.html", {"form": form})


def remove_drug(request, drug_id):
    drug = get_object_or_404(Drug, id=drug_id)

    return redirect("confirm_delete_drug", drug_id=drug.id)



def confirm_delete_drug(request, drug_id):
    # Retrieve the drug object based on the drug_id
    drug = Drug.objects.get(id=drug_id)

    if request.method == 'POST':
        # Delete the drug object
        drug.delete()
        return redirect('home')  # Redirect to the home page after deletion

    context = {'drug': drug}
    return render(request, 'base/confirm.html', context)

def edit_drug(request, drug_id):
    drug = get_object_or_404(Drug, id=drug_id)
    if request.method == 'POST':
        form = DrugForm(request.POST, instance=drug)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DrugForm(instance=drug)
    return render(request, 'base/edit_drug.html', {'form': form, 'drug': drug})