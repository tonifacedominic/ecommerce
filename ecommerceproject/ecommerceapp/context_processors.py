from .models import Category, Products
def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)