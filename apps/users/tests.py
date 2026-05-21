from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from .models import User


class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('users:register')

    def test_register_page_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_success_creates_user_and_redirects(self):
        response = self.client.post(self.url, {
            'username': 'nuevouser',
            'email': 'nuevo@example.com',
            'phone_number': '1122334455',
            'password1': 'ClaveSegura123!',
            'password2': 'ClaveSegura123!',
        })
        self.assertRedirects(response, reverse('games:catalog'))
        self.assertTrue(User.objects.filter(username='nuevouser').exists())

    def test_register_success_logs_in_automatically(self):
        self.client.post(self.url, {
            'username': 'nuevouser',
            'email': 'nuevo@example.com',
            'password1': 'ClaveSegura123!',
            'password2': 'ClaveSegura123!',
        })
        # Si está logueado, /users/login/ redirige al catálogo
        response = self.client.get(reverse('users:login'))
        self.assertRedirects(response, reverse('games:catalog'))

    def test_register_password_mismatch_shows_error(self):
        response = self.client.post(self.url, {
            'username': 'nuevouser',
            'email': 'nuevo@example.com',
            'password1': 'ClaveSegura123!',
            'password2': 'ClaveDiferente123!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='nuevouser').exists())

    def test_register_duplicate_username_shows_error(self):
        User.objects.create_user(username='existente', password='pass')
        response = self.client.post(self.url, {
            'username': 'existente',
            'email': 'otro@example.com',
            'password1': 'ClaveSegura123!',
            'password2': 'ClaveSegura123!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(username='existente').count(), 1)

    def test_register_new_user_has_zero_balance(self):
        self.client.post(self.url, {
            'username': 'nuevouser',
            'email': 'nuevo@example.com',
            'password1': 'ClaveSegura123!',
            'password2': 'ClaveSegura123!',
        })
        user = User.objects.get(username='nuevouser')
        self.assertEqual(user.balance, Decimal('0.00'))


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('users:login')
        self.user = User.objects.create_user(
            username='testuser',
            password='ClaveSegura123!',
            email='test@example.com',
        )

    def test_login_page_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_success_redirects_to_catalog(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'ClaveSegura123!',
        })
        self.assertRedirects(response, reverse('games:catalog'))

    def test_login_wrong_password_stays_on_page(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'clave_incorrecta',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_wrong_username_stays_on_page(self):
        response = self.client.post(self.url, {
            'username': 'usuario_inexistente',
            'password': 'ClaveSegura123!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_already_authenticated_redirects_to_catalog(self):
        self.client.login(username='testuser', password='ClaveSegura123!')
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('games:catalog'))


class TestLogoutView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='ClaveSegura123!',
        )

    def test_logout_redirects_to_login(self):
        self.client.login(username='testuser', password='ClaveSegura123!')
        response = self.client.get(reverse('users:logout'))
        self.assertRedirects(response, reverse('users:login'))

    def test_logout_ends_session(self):
        self.client.login(username='testuser', password='ClaveSegura123!')
        self.client.get(reverse('users:logout'))
        # Acceder a perfil después del logout debe redirigir al login
        profile_url = reverse('users:profile')
        response = self.client.get(profile_url)
        self.assertRedirects(response, f"{reverse('users:login')}?next={profile_url}")


class TestProfileView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='ClaveSegura123!',
            email='test@example.com',
            balance=Decimal('75.50'),
            country='Argentina',
        )
        self.url = reverse('users:profile')

    def test_profile_requires_authentication(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, f"{reverse('users:login')}?next={self.url}")

    def test_profile_loads_for_authenticated_user(self):
        self.client.login(username='testuser', password='ClaveSegura123!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_profile_shows_username(self):
        self.client.login(username='testuser', password='ClaveSegura123!')
        response = self.client.get(self.url)
        self.assertContains(response, 'testuser')

    def test_profile_shows_balance(self):
        self.client.login(username='testuser', password='ClaveSegura123!')
        response = self.client.get(self.url)
        # es-ar formatea decimales con coma: 75.50 → 75,50
        self.assertContains(response, '75,50')
