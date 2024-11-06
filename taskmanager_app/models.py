from django.db import models
from pytils.translit import slugify
from datetime import datetime

class Category(models.Model):
    name = models.CharField("Название сортировки", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Сортировка по"
        verbose_name_plural = "Сортировать по"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tasks(models.Model):
    title = models.CharField("Название задачи", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите сортировку")
    customer = models.CharField("Имя заказчика", max_length=100)
    deadline = models.CharField("Дедлайн", max_length=100)
    difficulty = models.CharField("Сложность", max_length=80)
    description = models.TextField("Описание задачи")
    condition = models.TextField("Описание условия")
    address = models.CharField("Адрес заказа", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.CharField("Email", max_length=100)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)
    is_active = models.BooleanField("Активная задача", default=False)
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title

class Rules(models.Model):
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "Правило"
        verbose_name_plural = "Правила"

    def __str__(self):
        return self.description
    
class Employees(models.Model):
    title = models.CharField("Имя сотрудника", max_length=200)
    post = models.CharField("Должность", max_length=150)
    ranking = models.IntegerField("Ранг")
    checklist = models.IntegerField("Кол-во задании")
    experiences = models.IntegerField("Опыт")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.title





