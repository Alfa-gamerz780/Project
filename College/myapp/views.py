from django.shortcuts import render, HttpResponse

from myapp.models import Contact, signtbl


# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def eBook(request):
    return render(request, 'e-book.html')

def loginn(request):
    return render(request, 'login.html')

def signupp(request):
    return render(request, 'signup.html')

def contactcode(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    msg = request.POST.get('msg')
    Contact.objects.create(name=name, email=email, subject=subject, message=msg)
    return HttpResponse("<script>alert('data has been sent');window.location.href='../'</script>")

def signcode(request):
    name = request.POST.get('name')
    dob = request.POST.get('dob')
    roll = request.POST.get('roll')
    password = request.POST.get('pass')
    cpassword = request.POST.get('cpass')
    if password == cpassword:
        signtbl.objects.create(name=name, dob=dob, roll=roll, password=password)
        return HttpResponse("<script>alert('Sign Up successfully');window.location.href='../loginn'</script>")
    else:
        return HttpResponse("<script>alert('password and Confirm password did not match');window.location.href='../signupp'</script>")

def logincode(request):
    roll = request.POST.get('roll')
    password = request.POST.get('password')
    data = signtbl.objects.filter(roll=roll).first()
    if not data:
        return HttpResponse("<script>alert('Roll number is wrong');window.location.href='../loginn'</script>")
    if data.password != password:
        return HttpResponse("<script>alert('password is wrong');window.location.href='../loginn'</script>")
    else:
        return HttpResponse("<script>alert('Login Successfully');window.location.href='../dashboard'</script>")

def dashboard(request):
    return render(request, 'dashboard.html')
