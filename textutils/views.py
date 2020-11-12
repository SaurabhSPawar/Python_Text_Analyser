# this is generated file by saurabh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'analyser.html')


def stackHolder(request):
    params = {'name': 'Saurabh', 'place': 'India'}
    return render(request, 'index.html', params)
# 1.params is use to transfer data from python page(views.py )
# to destination html page with help of templates present in settings.py in template array
# 2. render is use for to pass the values and to call html pages

def textanalyser_response(request):
    str1 = request.POST.get('text1', 'default')
    #if you want to use get method then replace POST.get by GET.get
    strx=str1
    #get method use to get variable from html page  default is use to
    #default is secondary options because it give avlue when we do not
    #get any value through get method
    str2 = request.POST.get('check1', 'off')
    str3 = request.POST.get('check2', 'off')
    str4 = request.POST.get('check3', 'off')
    str5 = request.POST.get('check4', 'off')
    str6 = request.POST.get('check5', 'off')
    flag=0
    count = 0
    if str2 == '1' and strx != "":
        flag=1
        punc = '''!()-[]{};:'",\<>./?@#$%^&*_~`'''
        analyse = ""
        for char in strx:
            if char not in punc:
                analyse = analyse + char
        strx=analyse
        #params = {'purpose': 'text-analysis', 'outputstr': analyse}
        #return render(request,'response.html', params)
    if str3 == '2' and strx != "":
        flag = 1
        analyse = ""
        for char in strx:
            analyse=analyse+char.upper()
        strx=analyse
        #params = {'purpose': 'text-uppercase', 'outputstr': analyse}
        #return render(request, 'response.html', params)
    if str4 == '3' and strx != "":
        flag = 1
        analyse = ""
        for char in strx:
            if char != "\n":
                analyse = analyse + char
        strx=analyse
        #params = {'purpose': 'text-next-line-remover', 'outputstr': analyse}
        #return render(request, 'response.html', params)
    if str5 == '4' and strx != "":
        flag = 1
        analyse = ""
        for index, char in enumerate(strx):
            if not(strx[index]==" " and strx[index+1]==" "):
                analyse = analyse + char
        strx=analyse
        #params = {'purpose': 'text-extra-space-remover', 'outputstr': analyse}
        #return render(request, 'response.html', params)
    if str6 == '5' and strx != "":
        flag = 1
        for char in strx:
            if char.isalpha():
                count += 1
    if strx == "":
        strx = str1
    params = {'purpose':'All Request In One', 'outputstr': strx,'count':count}
    return render(request, 'response.html', params)
    if flag == 0:
        return HttpResponse("error")

def about(request):
    return HttpResponse("<i>about me</i>:  I am<b> Saurabh </b>")
#in above HttpResponse is use to show output directly on html page
#we can use html tags as it is

def ourproducts(request):
    with open("one.txt","r")as f:
        return HttpResponse(f.read())
#we use file reader to fetch data from file

def home(request):
    with open("home_page.html", "r")as f:
        return HttpResponse(f.read())

def service(request):
    with open("service.html", "r")as f:
        return HttpResponse(f.read())