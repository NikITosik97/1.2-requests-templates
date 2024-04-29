from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def omlet_view(requests):
    if requests.GET.get('servings', False):
        amount_ = int(requests.GET.get('servings'))
        context = {'recipe': {},
                   'title': f"Omlet for {amount_} servings"}
        for ingredient, amount in DATA['omlet'].items():
            context['recipe'].setdefault(ingredient, round(amount * amount_, 2))
        return render(requests, 'calculator/index.html', context=context)
    else:
        context = {'recipe': DATA['omlet'],
                   'title': 'Omlet', }
        return render(requests, 'calculator/index.html', context=context)


def pasta_view(requests):
    if requests.GET.get('servings', False):
        amount_ = int(requests.GET.get('servings'))
        context = {'recipe': {},
                   'title': f"Pasta for {amount_} servings"}
        for ingredient, amount in DATA['pasta'].items():
            context['recipe'].setdefault(ingredient, round(amount * amount_, 2))
        return render(requests, 'calculator/index.html', context=context)
    else:
        context = {'recipe': DATA['pasta'],
                   'title': 'Pasta', }
        return render(requests, 'calculator/index.html', context=context)


def buter_view(requests):
    if requests.GET.get('servings', False):
        amount_ = int(requests.GET.get('servings'))
        context = {'recipe': {},
                   'title': f"Buter for {amount_} servings"}
        for ingredient, amount in DATA['buter'].items():
            context['recipe'].setdefault(ingredient, round(amount * amount_, 2))
        return render(requests, 'calculator/index.html', context=context)
    else:
        context = {'recipe': DATA['buter'],
                   'title': 'Buter', }
        return render(requests, 'calculator/index.html', context=context)
