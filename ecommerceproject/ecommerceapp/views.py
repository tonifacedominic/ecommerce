from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category, Products
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.
# def index(request):
#     return HttpResponse('Hey you ')

def AllProdCat(request, c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page= get_object_or_404(Category,slug=c_slug)
        products=Products.objects.all().filter(category=c_page,available=True)
    else:
        products=Products.objects.all().filter(available=True)

    try:
        paginator=Paginator(products, '6')
        page_number=int(request.GET.get('page',"1"))
        page_obj=paginator.page(page_number)

    except (InvalidPage,EmptyPage):
        page_obj=paginator.page(page_number)




    return render(request,'category.html', {'category':c_page,'products':page_obj})

def ProDetail(request,c_slug, p_slug):
    try:
        product=Products.objects.get(category__slug=c_slug, slug=p_slug)

    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})
