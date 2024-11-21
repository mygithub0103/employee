from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import EmployeeForm

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_employee')  # يمكنك إنشاء صفحة عرض الموظفين لاحقًا
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})




from django.shortcuts import render
from .models import Employee

def search_employee(request):
    query = request.GET.get('q')  # الحصول على النص المدخل في البحث
    results = None
    if query:
        results = Employee.objects.filter(full_name__icontains=query)  # البحث الجزئي
    return render(request, 'search_employee.html', {'results': results, 'query': query})
