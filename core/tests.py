from django.test import TestCase, override_settings

from .models import Projet


@override_settings(SECURE_SSL_REDIRECT=False)
class ProjetViewTests(TestCase):
    def test_index_displays_form_and_projects(self):
        Projet.objects.create(titre='Projet solaire', description='Énergie propre')

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Projet solaire')
        self.assertTemplateUsed(response, 'index.html')

    def test_valid_submission_creates_project_and_redirects_home(self):
        response = self.client.post(
            '/',
            {'titre': 'Projet solaire', 'description': 'Énergie propre'},
        )

        self.assertRedirects(response, '/')
        self.assertEqual(Projet.objects.count(), 1)
        self.assertEqual(Projet.objects.get().titre, 'Projet solaire')

    def test_invalid_submission_does_not_create_project(self):
        response = self.client.post('/', {'titre': '', 'description': ''})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Projet.objects.count(), 0)
        self.assertContains(response, 'Ce champ est obligatoire.')

    def test_title_longer_than_100_characters_is_rejected(self):
        response = self.client.post(
            '/',
            {'titre': 'x' * 101, 'description': 'Description'},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Projet.objects.count(), 0)
