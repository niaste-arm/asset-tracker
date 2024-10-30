from django.urls import path

from . import views

app_name = 'webapp'
urlpatterns = [
    # ex: /webapp/
    path("", views.index, name="index"),
    # ex: /webapp/home
    path("home/", views.index, name="home"),
    # ex: webapp/login
    path("login/", views.log_in, name="login"),
    # ex: webapp/logout
    path("logout/", views.log_out, name="logout"),
    # ex: webapp/register
    path("register/", views.register, name="register"),
    # ex: /webapp/assets/<int:asset_id>
    path("assets/<int:asset_id>", views.asset_detail, name="assetdetail"),
    # ex: /webapp/assets/add_asset
    path("assets/add_asset", views.add_asset, name="addasset"),
    # ex: /webapp/assets/delete_asset
    path("assets/delete_asset/<int:asset_id>", views.delete_asset, name="deleteasset"),
    # ex: /webapp/assets/search
    path("assets/search", views.search_asset, name="assetsearch"),
    # ex: /webapp/assets/update/<int:asset_id>
    path("assets/update/<int:asset_id>", views.update_asset, name="assetupdate"),
    # ex: /webapp/employees
    path("employees/", views.view_employees, name="viewemployees"),
    # ex: /webapp/employees/<int:employee_id>
    path("employees/<int:employee_id>", views.employee_detail, name="employeedetail"),
    # ex: webapp/employees/add_employee
    path("employees/add_employee", views.add_employee, name="addemployee"),
    # ex: webapp/employees/delete_employee
    path("employees/delete_employee/<int:employee_id>", views.delete_employee, name="employeedelete"),
    # ex: webapp/employees/update
    path("employees/update/<int:employee_id>", views.update_employee, name="employeeupdate"),
]