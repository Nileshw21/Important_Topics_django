
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

