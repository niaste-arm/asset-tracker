from django.test import TestCase
from webapp.models import Employee, Asset
from webapp.forms import AssetForm, EmployeeForm

class EmployeeTestCase(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(full_name="Adam Smith", 
                                date_of_birth="1969, 7, 20", 
                                address="123 Street Avenue")

    def test_employee_returns_name(self):
        self.assertEqual = (self.employee.__str__(), "Adam Smith")
    
    def test_employee_address_valid(self):
        return self.employee.is_address_valid()

class FormTestCase(TestCase):

    def test_add_asset_form(self):
        ## Create sample employee for test case asset owner
        employee = Employee.objects.create(full_name="Adam Smith", 
                                date_of_birth="1969, 7, 20", 
                                address="123 Street Avenue")
        ## Create sample asset for testing
        asset = Asset.objects.create(asset_owner=employee, 
                                     asset_name="Phone", 
                                     asset_desc="This is a test.")
        ## Create asset form and test if valid
        data = {'asset_owner' : asset.asset_owner, 'asset_name' : asset.asset_name, 'asset_desc' : asset.asset_desc}
        form = AssetForm(data=data)
        self.assertTrue(form.is_valid())

    def test_add_employee_form(self):
        employee = Employee.objects.create(full_name="Adam Smith", 
                                date_of_birth="1969, 7, 20", 
                                address="123 Street Avenue")
        
        data = {'full_name' : employee.full_name, 'date_of_birth' : employee.date_of_birth, 'address' : employee.address}
        form = EmployeeForm(data=data)
        self.assertTrue(form.is_valid())

