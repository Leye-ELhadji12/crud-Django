from django.shortcuts import redirect, render

from students.form import StudentForm
from students.models import Student


# Create your views here.
def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view')
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form': form})


def view(request):
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/view')


def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})




