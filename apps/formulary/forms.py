from django import forms
from .models import Formulary, Project
from django.contrib.auth.models import User


class CreateFormularyForm(forms.ModelForm):
    class Meta:
        model = Formulary
        fields = [
            "project",
            "change",
            "change_description",
            "change_justification",
            "priority",
            "reviewer",
        ]
        labels = {
            "project": "Proyecto",
            "change": "Cambio",
            "change_description": "Descripción",
            "change_justification": "Justificación",
            "priority": "Prioridad",
            "reviewer": "Revisor",
        }


class UpdateFormularyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"].choices = [
            ("Approved", "Aprobado"),
            ("Rejected", "Rechazado"),
        ]

    class Meta:
        model = Formulary
        fields = [
            "status",
            "comment",
        ]
        labels = {
            "status": "Estado",
            "comment": "Comentario",
        }


class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
        ]
        labels = {
            "name": "Nombre",
            "description": "Descripción",
        }
