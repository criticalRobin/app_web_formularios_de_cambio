from django.urls import path
from .views import CreateFormulary, ListFormulary, UpdateFormulary, form_pdf


app_name = "formulary"

urlpatterns = [
    path("", ListFormulary.as_view(), name="form_list"),
    path("create/", CreateFormulary.as_view(), name="form_create"),
    path("update/<int:pk>/", UpdateFormulary.as_view(), name="form_update"),
    path("pdf/<int:pk>/", form_pdf, name="form_pdf"),
]
