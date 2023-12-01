from django.urls import path
from base.views import *

urlpatterns = [
    path("", home, name="home"),
    path("add_drug/",add_drug,name="add_drug"),
    path("remove_drug/<str:drug_id>/",remove_drug,name="remove_drug"),
    path("confirm_delete_drug/<str:drug_id>/",confirm_delete_drug,name="confirm_delete_drug"),
    path("edit_drug/<str:drug_id>/",edit_drug,name="edit_drug"),
]
