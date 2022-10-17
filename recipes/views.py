from django.shortcuts import render
from django.http import HttpResponse
def omlet(request):
    servings = int(request.GET.get("servings", 1))
    template_name = 'calculator/index.html'

    context = {
      'recipe': {
        'яйца, шт': round(2 * servings ,1),
        'молоко, л': round(0.1 * servings,1),
        'соль, ч.л.': round(0.5 * servings,1),
      }
    }
    return render(request, template_name, context)

def pasta(request):
    servings = int(request.GET.get("servings", 1))
    template_name = 'calculator/index.html'

    context = {
        'recipe': {
        'макароны, г': round(0.3 * servings, 1),
        'сыр, г': round(0.05 * servings,1),
        }
    }
    return render(request, template_name, context)


def buter(request):
    servings = int(request.GET.get("servings", 1))
    template_name = 'calculator/index.html'
    context = {
        'recipe': {
        'хлеб, ломтик': round(1 * servings,1),
        'колбаса, ломтик': round(1 * servings,1),
        'сыр, ломтик': round(1 * servings,1),
        'помидор, ломтик': round(1 * servings,1),
    }
    }
    return render(request, template_name, context)