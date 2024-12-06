from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=40)
    def __str__(self):
        return self.full_name

    def is_address_valid(self):
        ## Check if address contains a house number
        has_house_no = any(chr.isdigit() for chr in self.address)
        return has_house_no

class Asset(models.Model):
    asset_owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=20)
    asset_desc = models.CharField(max_length=40)
    def __str__(self):
        return self.asset_name

    def owner(self):
        return self.asset_owner

