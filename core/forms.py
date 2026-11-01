from django import forms

from .models import Projet


class ProjetForm(forms.ModelForm):
    """Formulaire de saisie construit à partir du modèle Projet."""

    class Meta:
        # ModelForm réutilise les règles du modèle pour valider les données.
        model = Projet
        fields = ('titre', 'description')
        labels = {
            'titre': 'Titre du projet',
            'description': 'Description',
        }
        widgets = {
            # Les widgets contrôlent l'apparence des champs HTML générés.
            'titre': forms.TextInput(attrs={
                'placeholder': 'Titre du projet',
                'class': 'w-full border p-2 rounded',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description',
                'class': 'w-full border p-2 rounded',
            }),
        }
