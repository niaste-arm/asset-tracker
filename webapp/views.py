from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Asset, Employee
from .forms import AssetForm
from .forms import EmployeeForm
from .forms import LoginForm
from .forms import RegisterForm

def index(request):
    """
    Info: Index View for application
    Args: request (HttpRequest)
    Returns: rendered index page
    """
    asset_list = Asset.objects.all()
    context = {"asset_list" : asset_list}
    return render (request, "webapp/index.html", context)

def log_in(request):
    """
    Info: Login view for application
    Args: request (HttpRequest)
    Returns: rendered login page
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('webapp:index')
        
        form = LoginForm()
        return render(request, 'webapp/login.html', {'form': form})
        
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"{username.title()} successfully logged in.")
                return redirect('webapp:index')
    
    messages.error(request, "Error: invalid username/password, please try again.")
    return render(request, "webapp/login.html", {"form": form})

def log_out(request):
    """
    Info: Logout View for application
    Args: request (HttpRequest)
    Returns: Redirects to login page
    """
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect('webapp:login')

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'webapp/register.html', {"form": form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Registration successful.')
            login(request, user)
            return redirect('webapp:login')
        else:
            return render(request, 'webapp/register.html', {'form': form})

@login_required
def asset_detail(request, asset_id):
    """
    Info: Asset detail view for application
    Args: request (HttpRequest), asset_id object Primary Key
    Returns: Renders detailed asset view based on requested asset id
    """
    asset = get_object_or_404(Asset, pk=asset_id)
    return render(request, "webapp/asset_detail.html", {"asset": asset})

@login_required
def add_asset(request):
    """
    Info: Add Asset view for application
    Args: request (HttpRequest)
    Returns: Redirects back to form after handling POST data
    """
    submitted = False
    if request.method == "POST": # If Form Submitted
        form = AssetForm(request.POST)
        if form.is_valid(): # Check form is valid
            form.save()
            return HttpResponseRedirect('/webapp/assets/add_asset?submitted=True') # Return submitted as True
    else:
        form = AssetForm
        if 'submitted' in request.GET:
            submitted = True
    form = AssetForm
    return render(request, "webapp/add_asset.html", {'form':form, 'submitted':submitted})

@login_required
def delete_asset(request, asset_id):
    """
    Info: Delete Asset View for application
    Args: request (HttpRequest), asset_id object Primary Key
    Returns: Redirects back to home page after 
             handling asset deletion POST data
    """
    asset = get_object_or_404(Asset, pk=asset_id)
    asset.delete()
    messages.success(request, 'Asset deleted successfully.')
    return redirect('webapp:index')


@login_required
def search_asset(request):
    """
    Info: Search Asset View for application
    Args: request (HttpRequest)
    Returns: Rendered search asset page with the asset ID of input
    """
    if request.method == "POST": # If search submitted
        search_query = request.POST['searchquery'] # Get query
        search_results = Asset.objects.filter(asset_name__contains=search_query) # Use query
        return render(request, "webapp/search_asset.html", {'search_query':search_query, 'search_results':search_results})
    else:
        return render(request, "webapp/search_asset.html", {})

@login_required
def update_asset(request, asset_id):
    """
    Info: Update Asset View for application
    Args: request (HttpRequest), asset_id object Primary Key
    Returns: Rendered update asset page with asset id passed
    """
    asset = Asset.objects.get(pk=asset_id)
    form = AssetForm(request.POST or None, instance=asset)
    if form.is_valid():
        form.save()
        return redirect('webapp:index')
    return render(request, "webapp/update_asset.html", {'asset':asset, 'form':form})

@login_required
def view_employees(request):
    """
    Info: View Employees View for application
    Args: request (HttpRequest)
    Returns: Rendered view employees page
    """
    employee_list = Employee.objects.all()
    context = {"employee_list": employee_list}
    return render (request, "webapp/view_employees.html", context)

@login_required
def employee_detail(request, employee_id):
    """
    Info: Employee Detail View for application
    Args: request (HttpRequest), employee_id object Primary Key
    Returns: Rendered employee detail page with the employee ID passed
    """
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, "webapp/employee_detail.html", {"employee": employee})

@login_required
def add_employee(request):
    """
    Info: Add Employee View for application
    Args: request (HttpRequest)
    Returns: Rendered add employee page with form
    """
    submitted = False
    if request.method == "POST": # If form is submitted
        form = EmployeeForm(request.POST)
        if form.is_valid(): # Check data is valid
            form.save()
            return HttpResponseRedirect('/webapp/employees/add_employee?submitted=True')
    else:
        form = EmployeeForm
        if 'submitted' in request.GET:
            submitted = True
    form = EmployeeForm
    return render(request, "webapp/add_employee.html", {'form':form, 'submitted':submitted})

@login_required
def delete_employee(request, employee_id):
    """
    Info: Delete Employee View for application
    Args: request (HttpRequest), employee_id object Primary Key
    Returns: Redirects to employee view on successful deletion
             or redirects to employee detail view if fails
    """
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('webapp:viewemployees')
    return render(request, "webapp/employee_detail.html", {"employee": employee})

@login_required
def update_employee(request, employee_id):
    """
    Info: Update Employee View for application
    Args: request (HttpRequest), employee_id object Primary Key
    Returns: Redirects to home page after successfully updating employee
             or return form if fails.
    """
    employee = Employee.objects.get(pk=employee_id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('webapp:index')
    return render(request, "webapp/update_employee.html", {'employee':employee, 'form': form})