from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from stock.models import Supplier,Category,Article
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
#showing all category  with a paginator to show to show more
def all_category(request):
    categories=Category.objects.all()
    return render(request,'template/enfants/welcome.html',{
        'categories':categories,    
    })


#defining all article under a category
def see_more(request,cat_ref):
    category=Category.objects.get(slug=cat_ref)
    articles=category.category_article.filter(category=category)
    return render(request,'template/enfants/more_article.html',{'articles':articles,
                                                                'category':category})

#detail on given article
def detail(request,article_id):
    article=Article.objects.get(id=article_id)
    cat=article.category
    category=cat.category_article.all()
    return render(request,'template/enfants/detail_article.html',{
        'article':article,
        'category':category,
    })

def search_item(request):
    if request.method == "GET":
        querry=request.GET.get('query')
        if querry:
          articles = Article.objects.filter(
          Q(name__icontains=querry) |
          Q(marque__icontains=querry) |
          Q(category__reference__icontains=querry) |
          Q(supplier__name__icontains=querry) |
          Q(color__icontains=querry)
            )
          return render(request,'template/enfants/search.html',{
          'articles':articles,
          })
        else :
            print ('no information to display')
            return render(request,'template/enfants/search.html',{})
        
def cart(request):
    articles=Article.objects.all()
    return render(request,'template/enfants/cart.html',{'articles':articles})

def updatecart(request):
    return JsonResponse("find it's working", safe=False)