from django.shortcuts import render
from django.views import View
from .models import Elements, Alloys
from django.http import JsonResponse
from django.db.models import Count, Q
import json
from django.db import connection


class DisplayElementsView(View):
    def get(self, request):
        elements = Elements.objects.all()
        return render(request, 'Game.html', {'elements': elements})

    def post(self, request):
        # Десериализация тела запроса
        req_body = json.loads(request.body.decode('utf-8'))
        selected_element_ids = req_body.get('element_ids', [])
        selected_element_ids = [int(id) for id in selected_element_ids]  # Преобразование в целые числа

        # Находим сплавы, содержащие хотя бы один из выбранных элементов
        alloys_with_selected_elements = Alloys.objects.filter(elements__id__in=selected_element_ids).distinct()

        # Фильтруем сплавы, чтобы оставить только те, которые содержат ровно все выбранные элементы
        correct_alloys = []
        for alloy in alloys_with_selected_elements:
            # Получаем ID всех элементов сплава
            alloy_element_ids = set(alloy.elements.values_list('id', flat=True))
            # Проверяем, что сплав содержит только и все выбранные элементы
            if alloy_element_ids == set(selected_element_ids):
                correct_alloys.append(alloy)

        # Подготавливаем данные для ответа
        alloys_data = [{'id': alloy.id,
                        'name': alloy.name,
                        'description': alloy.description,
                        'images': str(alloy.images),
                        } for alloy in correct_alloys]

        return JsonResponse({'alloys': alloys_data})


class RecipesView(View):
    def get(self, request):
        # Логика представления, если необходимо
        return render(request, 'recipes.html')
