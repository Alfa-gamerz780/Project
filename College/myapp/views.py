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
    email_login = request.POST.get('email_login')
    dob = request.POST.get('dob')
    roll = request.POST.get('roll')
    password = request.POST.get('pass')
    cpassword = request.POST.get('cpass')
    if password == cpassword:
        signtbl.objects.create(name=name, email_login=email_login, dob=dob, roll=roll, password=password)
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

def admin_login(request):
    return render(request, 'admin_login.html')

def admin_logincode(request):
    admin_username = request.POST.get('admin_username')
    admin_password = request.POST.get('admin_password')
    data = admintbl.objects.filter(admin_username=admin_username).first()
    if not data:
        return HttpResponse("<script>alert('Username is wrong');window.location.href='../admin_login'</script>")
    if data.admin_password != admin_password:
        return HttpResponse("<script>alert('password is wrong');window.location.href='../admin_login'</script>")
    else:
        return HttpResponse("<script>alert('Admin Login Successfully');window.location.href='../dashboard'</script>")


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def student_info(request):
    return render(request, 'student_info.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def admin_notices(request):
    return render(request, 'admin_notices.html')

def student_info(request):
    students = signtbl.objects.all()
    return render(request, 'student_info.html', {'students': students})

def admin_notices(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    Notice.objects.create(title=title, content=content)
    return HttpResponse("<script>alert('Notice has been posted');window.location.href='../admin_notices'</script>")

def admin_notices(request):
    notice = Notice.objects.all()
    return render(request, 'admin_notices.html', {'notice': notice})

from myapp.models import admintbl

