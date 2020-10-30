from django.shortcuts import render,redirect
from . import models
from datetime import datetime, timedelta

def homeView(request):
    data = models.Employee.objects.all()

    if request.method =='POST':
        Name = request.POST.get('Name')
        Mobile = request.POST.get('Mobile')
        Email = request.POST.get('Email')
        EnquiryCategory = request.POST.get('EnquiryCategory')
        Message = request.POST.get('Message')
        if Name =='' or Mobile =='':
            return render('home')
        else:
            obj = models.Enquiry()
            obj.Name = Name
            obj.Mobile = Mobile
            obj.Email = Email
            obj.EnquiryCategory = EnquiryCategory
            obj.Message = Message
            obj.Enquiry_Date = datetime.today().date()
            obj.save()
            return render('home')

    html = 'home.html'
    context = {
        'data':data,
        'about_video':'https://youtu.be/B9DTCp0dItE',
        'latest_video':'https://youtu.be/B9DTCp0dItE'
    }
    return render(request,html,context)

def adminView(request):

    html = 'admin.html'
    context = {
        'admin_title': 'MyAdmin Home'
    }
    return render(request, html, context)

def employeeuploadView(request):
    data = models.Employee.objects.all()
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Designation = request.POST.get('Designation')
        Mobile = request.POST.get('Mobile')
        Email = request.POST.get('Email')
        Photo = request.FILES['myfile']
        if Name == '' or Designation =='' or Mobile =='' or Email =='' or Photo =='':
            return redirect('employee_upload')
        else:
            obj = models.Employee()
            obj.Name = Name
            obj.Designation = Designation
            obj.Mobile = Mobile
            obj.Email = Email
            obj.Photo = Photo
            obj.save()
            return redirect('home')

    html = 'employee_upload.html'
    context = {
        'admin_title': 'Employee',
        'data' : data
    }
    return render(request, html, context)

def employee_deleteView(request,id):
    obj = models.Employee.objects.get(id=id)
    obj.delete()
    return redirect('employee_upload')

    html = 'employee_upload.html'
    context = {
    }
    return render(request,html,context)

def employeeView(request,id):
    obj = models.Employee.objects.get(id=id)
    html = 'profile.html'
    context = {
        'data':obj
    }
    return render(request,html,context)

# Blog Home

def blog_home_technologyView(request):
    data = models.Blog_Technology.objects.all()
    html = 'blog_home_technology.html'
    context = {
        'data':data,
        'Blog_name':'Technology'
    }
    return render(request,html,context)

def blog_home_tutorialsView(request):
    data = models.Blog_Tutorials.objects.all()
    html = 'blog_home_tutorials.html'
    context = {
        'data':data,
        'Blog_name':'Tutorials'
    }
    return render(request,html,context)

def blog_home_circuitsView(request):
    data = models.Blog_Circuits.objects.all()
    html = 'blog_home_circuits.html'
    context = {
        'data':data,
        'Blog_name':'Circuits'
    }
    return render(request,html,context)


# Upload Blog
def blog_upload_technologyView(request):
    data = models.Blog_Technology.objects.all()

    if request.method == 'POST':
        obj = models.Blog_Technology()
        obj.blog_heading = request.POST.get('blog_heading')
        obj.blog_discription = request.POST.get('blog_discription')
        obj.blog_date = datetime.today().date()

    # Block 1
        obj.sub_title_1 = request.POST.get('sub_title_1')
        obj.image_1 = request.FILES['img1']
        obj.content_1 = request.POST.get('content_1')
        obj.p1 = request.POST.get('p1')
        obj.p2 = request.POST.get('p2')
        obj.p3 = request.POST.get('p3')
        obj.p4 = request.POST.get('p4')
        obj.p5 = request.POST.get('p5')
        obj.p6 = request.POST.get('p6')
        obj.p7 = request.POST.get('p7')
        obj.p8 = request.POST.get('p8')
        obj.p9 = request.POST.get('p9')
        obj.p10 = request.POST.get('p10')
    # Block 2
        obj.sub_title_2 = request.POST.get('sub_title_2')
        obj.image_2 = request.FILES['img2']
        obj.content_2 = request.POST.get('content_2')
        obj.p11 = request.POST.get('p11')
        obj.p12 = request.POST.get('p12')
        obj.p13 = request.POST.get('p13')
        obj.p14 = request.POST.get('p14')
        obj.p15 = request.POST.get('p15')
        obj.p16 = request.POST.get('p16')
        obj.p17 = request.POST.get('p17')
        obj.p18 = request.POST.get('p18')
        obj.p19 = request.POST.get('p19')
        obj.p20 = request.POST.get('p20')
    # Block 3
        obj.sub_title_3 = request.POST.get('sub_title_3')
        obj.image_3 = request.FILES['img3']
        obj.content_3 = request.POST.get('content_3')
        obj.p21 = request.POST.get('p21')
        obj.p22 = request.POST.get('p22')
        obj.p23 = request.POST.get('p23')
        obj.p24 = request.POST.get('p24')
        obj.p25 = request.POST.get('p25')
        obj.p26 = request.POST.get('p26')
        obj.p27 = request.POST.get('p27')
        obj.p28 = request.POST.get('p28')
        obj.p29 = request.POST.get('p29')
        obj.p30 = request.POST.get('p30')
    # Block 4
        obj.sub_title_4 = request.POST.get('sub_title_4')
        obj.image_4 = request.FILES['img4']
        obj.content_4 = request.POST.get('content_4')
        obj.p31 = request.POST.get('p31')
        obj.p32 = request.POST.get('p32')
        obj.p33 = request.POST.get('p33')
        obj.p34 = request.POST.get('p34')
        obj.p35 = request.POST.get('p35')
        obj.p36 = request.POST.get('p36')
        obj.p37 = request.POST.get('p37')
        obj.p38 = request.POST.get('p38')
        obj.p39 = request.POST.get('p39')
        obj.p40 = request.POST.get('p40')
    # Block 5
        obj.sub_title_5 = request.POST.get('sub_title_5')
        obj.image_5 = request.FILES['img5']
        obj.content_5 = request.POST.get('content_5')
        obj.p41 = request.POST.get('p41')
        obj.p42 = request.POST.get('p42')
        obj.p43 = request.POST.get('p43')
        obj.p44 = request.POST.get('p44')
        obj.p45 = request.POST.get('p45')
        obj.p46 = request.POST.get('p46')
        obj.p47 = request.POST.get('p47')
        obj.p48 = request.POST.get('p48')
        obj.p49 = request.POST.get('p49')
        obj.p50 = request.POST.get('p50')

        obj.save()
        return redirect('blog_home_technology')

    html = 'blog_upload_technology.html'
    context = {
        'data':data,
        'admin_title' : 'Blog Technology'
    }
    return render(request,html,context)

def blog_upload_tutorialsView(request):
    data = models.Blog_Tutorials.objects.all()

    if request.method == 'POST':
        obj = models.Blog_Tutorials()
        obj.blog_heading = request.POST.get('blog_heading')
        obj.blog_discription = request.POST.get('blog_discription')
        obj.blog_date = datetime.today().date()

    # Block 1
        obj.sub_title_1 = request.POST.get('sub_title_1')
        obj.image_1 = request.FILES['img1']
        obj.content_1 = request.POST.get('content_1')
        obj.p1 = request.POST.get('p1')
        obj.p2 = request.POST.get('p2')
        obj.p3 = request.POST.get('p3')
        obj.p4 = request.POST.get('p4')
        obj.p5 = request.POST.get('p5')
        obj.p6 = request.POST.get('p6')
        obj.p7 = request.POST.get('p7')
        obj.p8 = request.POST.get('p8')
        obj.p9 = request.POST.get('p9')
        obj.p10 = request.POST.get('p10')
    # Block 2
        obj.sub_title_2 = request.POST.get('sub_title_2')
        obj.image_2 = request.FILES['img2']
        obj.content_2 = request.POST.get('content_2')
        obj.p11 = request.POST.get('p11')
        obj.p12 = request.POST.get('p12')
        obj.p13 = request.POST.get('p13')
        obj.p14 = request.POST.get('p14')
        obj.p15 = request.POST.get('p15')
        obj.p16 = request.POST.get('p16')
        obj.p17 = request.POST.get('p17')
        obj.p18 = request.POST.get('p18')
        obj.p19 = request.POST.get('p19')
        obj.p20 = request.POST.get('p20')
    # Block 3
        obj.sub_title_3 = request.POST.get('sub_title_3')
        obj.image_3 = request.FILES['img3']
        obj.content_3 = request.POST.get('content_3')
        obj.p21 = request.POST.get('p21')
        obj.p22 = request.POST.get('p22')
        obj.p23 = request.POST.get('p23')
        obj.p24 = request.POST.get('p24')
        obj.p25 = request.POST.get('p25')
        obj.p26 = request.POST.get('p26')
        obj.p27 = request.POST.get('p27')
        obj.p28 = request.POST.get('p28')
        obj.p29 = request.POST.get('p29')
        obj.p30 = request.POST.get('p30')
    # Block 4
        obj.sub_title_4 = request.POST.get('sub_title_4')
        obj.image_4 = request.FILES['img4']
        obj.content_4 = request.POST.get('content_4')
        obj.p31 = request.POST.get('p31')
        obj.p32 = request.POST.get('p32')
        obj.p33 = request.POST.get('p33')
        obj.p34 = request.POST.get('p34')
        obj.p35 = request.POST.get('p35')
        obj.p36 = request.POST.get('p36')
        obj.p37 = request.POST.get('p37')
        obj.p38 = request.POST.get('p38')
        obj.p39 = request.POST.get('p39')
        obj.p40 = request.POST.get('p40')
    # Block 5
        obj.sub_title_5 = request.POST.get('sub_title_5')
        obj.image_5 = request.FILES['img5']
        obj.content_5 = request.POST.get('content_5')
        obj.p41 = request.POST.get('p41')
        obj.p42 = request.POST.get('p42')
        obj.p43 = request.POST.get('p43')
        obj.p44 = request.POST.get('p44')
        obj.p45 = request.POST.get('p45')
        obj.p46 = request.POST.get('p46')
        obj.p47 = request.POST.get('p47')
        obj.p48 = request.POST.get('p48')
        obj.p49 = request.POST.get('p49')
        obj.p50 = request.POST.get('p50')

        obj.save()
        return redirect('blog_upload_tutorials')

    html = 'blog_upload_tutorials.html'
    context = {
        'data':data,
        'admin_title' : 'Blog Tutorials'
    }
    return render(request,html,context)

def blog_upload_circuitsView(request):
    data = models.Blog_Circuits.objects.all()

    if request.method == 'POST':
        obj = models.Blog_Circuits()
        obj.blog_heading = request.POST.get('blog_heading')
        obj.blog_discription = request.POST.get('blog_discription')
        obj.blog_date = datetime.today().date()

    # Block 1
        obj.sub_title_1 = request.POST.get('sub_title_1')
        obj.image_1 = request.FILES['img1']
        obj.content_1 = request.POST.get('content_1')
        obj.p1 = request.POST.get('p1')
        obj.p2 = request.POST.get('p2')
        obj.p3 = request.POST.get('p3')
        obj.p4 = request.POST.get('p4')
        obj.p5 = request.POST.get('p5')
        obj.p6 = request.POST.get('p6')
        obj.p7 = request.POST.get('p7')
        obj.p8 = request.POST.get('p8')
        obj.p9 = request.POST.get('p9')
        obj.p10 = request.POST.get('p10')
    # Block 2
        obj.sub_title_2 = request.POST.get('sub_title_2')
        obj.image_2 = request.FILES['img2']
        obj.content_2 = request.POST.get('content_2')
        obj.p11 = request.POST.get('p11')
        obj.p12 = request.POST.get('p12')
        obj.p13 = request.POST.get('p13')
        obj.p14 = request.POST.get('p14')
        obj.p15 = request.POST.get('p15')
        obj.p16 = request.POST.get('p16')
        obj.p17 = request.POST.get('p17')
        obj.p18 = request.POST.get('p18')
        obj.p19 = request.POST.get('p19')
        obj.p20 = request.POST.get('p20')
    # Block 3
        obj.sub_title_3 = request.POST.get('sub_title_3')
        obj.image_3 = request.FILES['img3']
        obj.content_3 = request.POST.get('content_3')
        obj.p21 = request.POST.get('p21')
        obj.p22 = request.POST.get('p22')
        obj.p23 = request.POST.get('p23')
        obj.p24 = request.POST.get('p24')
        obj.p25 = request.POST.get('p25')
        obj.p26 = request.POST.get('p26')
        obj.p27 = request.POST.get('p27')
        obj.p28 = request.POST.get('p28')
        obj.p29 = request.POST.get('p29')
        obj.p30 = request.POST.get('p30')
    # Block 4
        obj.sub_title_4 = request.POST.get('sub_title_4')
        obj.image_4 = request.FILES['img4']
        obj.content_4 = request.POST.get('content_4')
        obj.p31 = request.POST.get('p31')
        obj.p32 = request.POST.get('p32')
        obj.p33 = request.POST.get('p33')
        obj.p34 = request.POST.get('p34')
        obj.p35 = request.POST.get('p35')
        obj.p36 = request.POST.get('p36')
        obj.p37 = request.POST.get('p37')
        obj.p38 = request.POST.get('p38')
        obj.p39 = request.POST.get('p39')
        obj.p40 = request.POST.get('p40')
    # Block 5
        obj.sub_title_5 = request.POST.get('sub_title_5')
        obj.image_5 = request.FILES['img5']
        obj.content_5 = request.POST.get('content_5')
        obj.p41 = request.POST.get('p41')
        obj.p42 = request.POST.get('p42')
        obj.p43 = request.POST.get('p43')
        obj.p44 = request.POST.get('p44')
        obj.p45 = request.POST.get('p45')
        obj.p46 = request.POST.get('p46')
        obj.p47 = request.POST.get('p47')
        obj.p48 = request.POST.get('p48')
        obj.p49 = request.POST.get('p49')
        obj.p50 = request.POST.get('p50')

        obj.save()
        return redirect('blog_upload_circuits')

    html = 'blog_upload_circuits.html'
    context = {
        'data':data,
        'admin_title' : 'Blog Circuits'
    }
    return render(request,html,context)



# Blog Delete
def blog_technology_deleteView(request,id):
    obj = models.Blog_Technology.objects.get(id=id)
    obj.delete()
    return redirect('blog_upload_technology')
    html = 'blog_upload_technology.html'
    context = {
    }
    return render(request,html,context)

def blog_tutorials_deleteView(request,id):
    obj = models.Blog_Tutorials.objects.get(id=id)
    obj.delete()
    return redirect('blog_upload_tutorials')
    html = 'blog_upload_tutorials.html'
    context = {
    }
    return render(request,html,context)

def blog_circuits_deleteView(request,id):
    obj = models.Blog_Circuits.objects.get(id=id)
    obj.delete()
    return redirect('blog_upload_circuits')
    html = 'blog_upload_circuits.html'
    context = {
    }
    return render(request,html,context)



# Blog Details Page
def blog_technologyView(request,id):
    blog_technology = models.Blog_Technology.objects.all()
    blog_tutorials = models.Blog_Tutorials.objects.all()
    blog_circuits = models.Blog_Circuits.objects.all()
    data = models.Blog_Technology.objects.get(id=id)
    html = 'blog_technology.html'
    context = {
        'data':data,
        'blog_technology':blog_technology,
        'blog_tutorials':blog_tutorials,
        'blog_circuits':blog_circuits
    }
    return render(request,html,context)

def blog_tutorialsView(request,id):
    blog_technology = models.Blog_Technology.objects.all()
    blog_tutorials = models.Blog_Tutorials.objects.all()
    blog_circuits = models.Blog_Circuits.objects.all()
    data = models.Blog_Tutorials.objects.get(id=id)
    html = 'blog_tutorials.html'
    context = {
        'data':data,
        'blog_technology':blog_technology,
        'blog_tutorials':blog_tutorials,
        'blog_circuits':blog_circuits
    }
    return render(request,html,context)

def blog_circuitsView(request,id):
    blog_technology = models.Blog_Technology.objects.all()
    blog_tutorials = models.Blog_Tutorials.objects.all()
    blog_circuits = models.Blog_Circuits.objects.all()
    data = models.Blog_Circuits.objects.get(id=id)
    html = 'blog_circuits.html'
    context = {
        'data':data,
        'blog_technology':blog_technology,
        'blog_tutorials':blog_tutorials,
        'blog_circuits':blog_circuits
    }
    return render(request,html,context)



def enquiry_homeView(request):
    data = models.Enquiry.objects.all()
    html = 'enquiry_home.html'
    context = {
        'data':data,
        'admin_title': 'Enquiry Details'
    }
    return render(request,html,context)

def enquiry_deleteView(request,id):
    obj = models.Enquiry.objects.get(id=id)
    obj.delete()
    return redirect('enquiry_home')
    html = 'enquiry_home.html'
    context = {
    }
    return render(request,html,context)











