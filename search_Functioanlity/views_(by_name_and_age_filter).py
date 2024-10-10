from django.shortcuts import render, redirect
from home.models import Students2, Student
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == "POST":
        print("inside index")
        print(request.POST)

        name = request.POST.get("full_name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        ulpoad_file = request.FILES['ulpoad_file']

        Students2.objects.create(

            name = name,
            age = age,
            gender = gender,
            ulpoad_file = ulpoad_file,
        )
        # return redirect("/Thank you/")
        # print(ulpoad_file)
        # print(name, age , gender)
        # return redirect("/")

    else:
        print(request.method)
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')



def dynamic_path(request, num):
    print(num)
    return HttpResponse("This is dynamic path page")


def search_page(request):
    students = Student.objects.all()
    

    print(request.GET.get('search'))

    search = request.GET.get('search')

    age = request.GET.get('age')

    if search:
        # students = students.filter(name__icontains = search)
        # students = students.filter(college__college_name__icontains = search)

        students = students.filter(
            Q(name__icontains = search)|
            Q(email__icontains = search)|
            Q(gender__icontains = search)|
            Q(student_bio__icontains = search)
            )
        # print(students)

    if age:
        print(age, type(age))
    if age == "1":
        students = students.filter(age__gte = 18 , age__lte = 20).order_by('age')
    if age == "2":
        students = students.filter(age__gte = 20 , age__lte = 22).order_by('age')

    if age == "3":
        students = students.filter(age__gte = 22 , age__lte = 24).order_by('age')


    context = {'students':students, 'search': search}
    return render(request, 'search.html', context)
