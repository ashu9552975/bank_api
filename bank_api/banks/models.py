from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    bank_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    ifsc = models.CharField(max_length=11, primary_key=True)
    branch = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.branch} ({self.ifsc})'
