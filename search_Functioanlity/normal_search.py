def search_page(request):
    students = Student.objects.all()
    

    print(request.GET.get('search'))

    search = request.GET.get('search')

    if search:
        # students = students.filter(name__icontains = search)
        # students = students.filter(college__college_name__icontains = search)

        students = students.filter(
            Q(name__icontains = search)|
            Q(email__icontains = search)|
            Q(gender__icontains = search)|
            Q(student_bio__icontains = search)
            )
        print(students)

    context = {'students':students, 'search': search}
    return render(request, 'search.html', context)
