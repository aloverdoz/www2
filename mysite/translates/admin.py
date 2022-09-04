from django.contrib import admin

from .models import Translates, Category


class   TranstalesAdmin(admin.ModelAdmin):
    #Какие поля отображаются в админке
    list_display = ('id', 'title', 'created_at', 'title_in_the_original_language', 'is_published', 'photo')
    #Ссылки для перехода в контент перевода
    list_display_links = ('id', 'title')
    #По каким полям осуществляется поиск
    search_fields = ('title', 'description')
    #Какие поля можно редактировать прямо из админки
    list_editable = ('is_published',)
    #По каким полям мы можем фильтровать
    list_filter = ('is_published', 'category')


class   CategoryAdmin(admin.ModelAdmin):
    #Какие поля отображаются в админке
    list_display = ('id', 'title')
    #Ссылки для перехода в контент перевода
    list_display_links = ('id', 'title')
    #По каким полям осуществляется поиск
    search_fields = ('title',)

admin.site.register(Translates, TranstalesAdmin)
admin.site.register(Category, CategoryAdmin)
