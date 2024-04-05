from django.contrib import admin
from .models import Elements, Alloys

@admin.register(Elements)
class ElementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'percent']  # Определяет, какие поля отображать в списке элементов
    search_fields = ['name', 'percent']  # Определяет, по каким полям можно выполнять поиск
    # Добавьте другие атрибуты Meta, если это необходимо

@admin.register(Alloys)
class AlloysAdmin(admin.ModelAdmin):
    list_display = ['name']  # Определяет, какие поля отображать в списке сплавов
    search_fields = ['id', 'name', 'percent']  # Определяет, по каким полям можно выполнять поиск
    filter_horizontal = ['elements']  # Определяет, какие поля ManyToMany отображать в виде множественного выбора
    # Добавьте другие атрибуты Meta, если это необходимо
