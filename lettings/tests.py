from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsTest(TestCase):
    def setUp(self) -> None:
        self.address = Address.objects.create(
            street='Boulevard du Triomphe',
            number=400,
            city='Bruxelles',
            state='Bruxelles',
            zip_code='1080',
            country_iso_code='BE'
        )
        self.letting = Letting.objects.create(title="Lettings Test", address=self.address)

    def test_index(self):
        response = self.client.get(reverse('lettings:index'))
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def test_letting_detail(self):
        response = self.client.get(reverse('lettings:letting', args=[1]))
        assert response.status_code == 200
        assert b"<title>Lettings Test</title>" in response.content

    def test_lettings_models_str(self):
        assert str(self.address) == f'{self.address.number} {self.address.street}'
        assert str(self.letting) == self.letting.title
