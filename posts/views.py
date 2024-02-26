from django.shortcuts import render
from django.utils.translation import gettext as _
from . models import Post 
def index(request):
    filter_string = {}
    if request.GET.get('search'):
        filter_string['title__icontains'] = request.GET.get('search')
    posts_frist_three = Post.objects.filter(**filter_string).filter(post_type='PRODUCTS')[:3]
    posts = Post.objects.filter(**filter_string).filter(post_type='PRODUCTS')[3:]
    context = {
        'posts_frist_three':  posts_frist_three ,
         'posts': posts,
    }
    return render(request, 'index.html',context)


def news(request):
     filter_string = {}
     if request.GET.get('search'):
         filter_string['title__icontains'] = request.GET.get('search')
     newss = Post.objects.filter(**filter_string).filter(post_type="NEWS")
     context = {
      'newss': newss
     }
     
     return render(request, 'news.html', context)

def more_info(request,news_id):
    news = Post.objects.get(slug=news_id)
    context = {
    'news': news,
    }
    return render(request,'more_info.html',context)


def research(request):
    filter_string = {}
    if request.GET.get('search'):
        filter_string['title__icontains'] = request.GET.get('search') 
    researches = Post.objects.filter(**filter_string).filter(post_type='RESEARCH')
    context = {
        'researches': researches,
    }
    return render(request, 'research.html', context)

def research_content_details(request, research_id):
    research = Post.objects.get(slug=research_id)
    context = {
        'research': research,
    }
    
    return render(request, 'research_content_details.html', context)



def contact(request):
   
    return render(request, 'contact.html')


def company(request):
    return render(request, 'company.html')

def customers(request):
    filter_string = {}
    if request.GET.get('search'):
        filter_string['title__icontains'] = request.GET.get('search') 
    frist_part = Post.objects.filter(**filter_string).filter(post_type='CUSTOMERS')[:24]
    second_part = Post.objects.filter(**filter_string).filter(post_type='CUSTOMERS')[24:]
    context={
        'frist_part': frist_part,
        'second_part': second_part,
    }
    return render(request, 'customers.html',context)

def partner(request):
    return render(request, 'partner.html')

def eda(request):
    filter_string = {}
    if request.GET.get('search'):
        filter_string['title__icontains'] = request.GET.get('search') 
    eda_data = Post.objects.filter(**filter_string).filter(post_type='EDA')
    context = {
        'eda_data': eda_data,
    }
    return render(request, 'eda.html',context)

def jm(request):
    return render(request, 'jm.html')

def databases(request):
    filter_string = {}
    if request.GET.get('search'):
        filter_string['title__icontains'] = request.GET.get('search') 
        
    databases = Post.objects.filter(**filter_string).filter(post_type='PRODUCTS')[3:]
    context = {
        'databases': databases,
    }
    return render(request, 'databases.html',context)


def database_details(request, database_id):
    database_detail = Post.objects.get(slug=database_id,post_type='PRODUCTS')
    context = {
        'database_detail': database_detail,
    }
    
    return render(request, 'database_details.html', context)

def meterial(request):
    return render(request,'material.html')

def implement(request):
    return render(request, 'implement.html')

def home_details(request, home_id):
    home_detail = Post.objects.get(slug=home_id)
    context = {
        'home_detail': home_detail,
    }
    
    return render(request, 'home_details.html', context)


def stahldat(request):
    
    return render(request,'stahldat.html')

def aluselect(request):

    return render(request,'aluselect.html')


def for_jm_pro(request):
    
    return render(request,'for_jm_pro.html')


def eda_details(request,eda_id):
    detail = Post.objects.get(slug=eda_id)
    context = {
        'detail': detail,
    }

    return render(request,'eda_details.html',context)

def jm_details(request):

    return render(request,'jm_details.html')


def imprint(request):
    return render(request, 'imprint.html')

def privacy(request):
    return render(request, 'privacy.html')

def  cookies(request):
    return render(request, 'cookies.html')

def notice(request):
    return render(request, 'notice.html')

def terms(request):
    return render(request, 'terms.html')

def search(request):
    term = request.GET.get('term', '')

    context = {
        'term': term
    }

    posts = Post.objects.filter(
        title__icontains=term,
    )
    context['posts'] = posts
    return render(request,'search.html', context)