from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Bank, Branch

class BankAPITestCase(APITestCase):

    def setUp(self):
        self.bank = Bank.objects.create(name='Test Bank', bank_id=1)
        self.branch = Branch.objects.create(
            ifsc='TEST0001',
            branch='Test Branch',
            address='123 Test Street',
            city='Test City',
            district='Test District',
            state='Test State',
            bank=self.bank
        )

    def test_get_bank_list(self):
        url = reverse('bank-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_branch_detail(self):
        url = reverse('branch-detail', args=[self.branch.ifsc])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['branch'], 'Test Branch')
