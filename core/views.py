from django.shortcuts import render, redirect

from .forms import ProjetForm
from .models import Projet


def index(request):
    # GET : formulaire vide ; POST : formulaire rempli avec les données envoyées.
    form = ProjetForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # save() valide déjà les champs grâce au ModelForm avant l'enregistrement.
        form.save()
        # Post/Redirect/Get évite de recréer le projet au rafraîchissement.
        return redirect('home')

    # Ces données seront disponibles dans le template sous les noms form et projets.
    projets = Projet.objects.all()
    return render(request, 'index.html', {'form': form, 'projets': projets})
