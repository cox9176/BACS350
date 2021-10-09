from django.test import TestCase
from hero.models import Superhero
from django.urls import reverse

class SuperheroCRUDTest(TestCase):
    def test_django(self):
        self.assertTrue

    def test_num_superhero(self):
        self.assertEqual(len(Superhero.objects.all()), 0)

    def test_add_superhero(self):
        Superhero.objects.create(name='Green Lantern', identity='Alan Scott')
        self.assertEqual(len(Superhero.objects.all()), 1)

    def test_superhero_name(self):
        Superhero.objects.create(name='Green Lantern', identity='Alan Scott')
        s = Superhero.objects.get(pk=1)
        self.assertEqual(s.name, 'Green Lantern')
        self.assertEqual(s.identity, 'Alan Scott')
        self.assertEqual(s.image, 'None')
        self.assertEqual(s.description, 'None')
        self.assertEqual(s.strength, 'None')
        self.assertEqual(s.weakness, 'None')

    def test_superhero_edit(self):
        Superhero.objects.create(name='Green Lantern', identity='Alan Scott')
        s = Superhero.objects.get(pk=1)
        s.name = 'Name test'
        s.identity = 'Identity test'
        s.strength = 'Strength test'
        self.assertEqual(s.name, 'Name test')
        self.assertEqual(s.identity, 'Identity test')
        self.assertEqual(s.strength, 'Strength test')

    def test_superhero_delete(self):
        Superhero.objects.create(name='Green Lantern', identity='Alan Scott')
        s = Superhero.objects.get(pk=1)
        s.delete()
        self.assertEqual(len(Superhero.objects.all()), 0)

    def test_string_representation(self):
        superhero = Superhero.objects.create(name='Green Lantern', identity='Alan Scott')
        self.assertEqual(str(superhero), '1 - Green Lantern')

class SuperheroViewsTest(TestCase):
    def setUp(self):
        self.superhero = Superhero.objects.create(name='Green Lantern', identity='Alan Scott')

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_get_absolute_url(self):
        self.assertEqual(self.superhero.get_absolute_url(), '/hero/1')

    def test_superhero_detail_view(self):
        self.assertEqual(reverse('hero_detail', args='2'), '/hero/2')
        response = self.client.get('/hero/1')
        self.assertEqual(response.status_code, 200)

    def test_superhero_add_view(self):
        self.assertEqual(reverse('hero_add'), '/hero/add')
        response = self.client.get('/hero/add')
        self.assertEqual(response.status_code, 200)
        content = dict(name='Green Lantern', identity='Alan Scott')
        response = self.client.post('/hero/add', content)
        response = self.client.get('/hero/')
        self.assertContains(response, '<td>', count=8)

    def test_superhero_edit_view(self):
        self.assertEqual(reverse('hero_edit', args='2'), '/hero/2/')
        response = self.client.get('/hero/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Superman')
        contents = dict(name='Green Lantern', identity='Alan Scott')
        response = self.client.post('/hero/1/', contents)
        superhero = Superhero.objects.get(pk=1)
        self.assertEqual(superhero.name, 'Green Lantern')

    def test_superhero_delete_view(self):
        self.assertEqual(reverse('hero_delete', args='2'), '/hero/2/delete')
        response = self.client.get('/hero/1/delete')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/hero/1/delete')
        self.assertEqual(len(Book.objects.all()), 0)






        
