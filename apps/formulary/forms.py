from django import forms
from .models import Formulary


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
