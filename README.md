# Burkina Ecolo App

Application web Django - Burkina Ecolo Tech.

## Démarrer le projet

```powershell
.\venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver
```

Puis ouvrir `http://127.0.0.1:8000/`.

Si le port 8000 est déjà utilisé par un autre projet :

```powershell
python manage.py runserver 8001
```

Puis ouvrir `http://127.0.0.1:8001/` (**HTTP**, pas HTTPS).

La sécurité HTTPS est réservée au déploiement. Pour l'activer explicitement,
définir `DJANGO_SECURE_SSL_REDIRECT=True` derrière un vrai serveur HTTPS.

Après avoir modifié un modèle, toujours exécuter :

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Méthode Django à suivre

1. **Comprendre le besoin** : écrire le parcours utilisateur avant de coder.
2. **Modéliser les données** : créer ou modifier les modèles dans `core/models.py`.
3. **Valider les entrées** : utiliser un `ModelForm` dans `core/forms.py`, jamais uniquement
   `request.POST` dans la vue.
4. **Écrire un test qui échoue** pour le comportement attendu.
5. **Implémenter** dans la vue, en gardant la vue courte :
   valider, sauvegarder, rediriger.
6. **Afficher dans un template** et ne jamais faire confiance aux données venant du navigateur.
7. **Vérifier régulièrement** :

```powershell
python manage.py check
python manage.py test
python manage.py makemigrations --check --dry-run
```

### Règles importantes

- Une fonctionnalité = un petit changement testable.
- Après un POST réussi, rediriger pour éviter les doublons au rafraîchissement
  (pattern **Post/Redirect/Get**).
- Ne jamais committer `.env`, `db.sqlite3` ou une vraie `SECRET_KEY`.
- Garder les migrations dans Git.
- Faire des commits courts et explicites : `Ajoute le formulaire Projet`.
- Lire les erreurs complètement avant de modifier le code.
