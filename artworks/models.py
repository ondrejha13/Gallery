from django.db import models
from django.db.models import ImageField, ForeignKey, CharField, PositiveIntegerField, SET_NULL
from taggit.managers import TaggableManager


class Artwork(models.Model):
    CATEGORY_CHOICES = [
        ('painting', 'Obraz'),
        ('sketch', 'Skica'),
        ('object', 'Objekt'),
        ('sculpture', 'Plastika'),
        ('relief', 'Reliéf'),
        ('other', 'Ostatní'),
    ]

    title_cz = CharField(max_length=200, verbose_name="Název", null=True, blank=True)
    title_en = CharField(max_length=200, verbose_name="Title", null=True, blank=True)
    year = PositiveIntegerField(verbose_name="Rok vzniku", null=True, blank=True)
    category = CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Kategorie", null=True, blank=True)
    technique = CharField(max_length=100, verbose_name="Technika", blank=True)
    material = CharField(max_length=100, verbose_name="Materiál", blank=True)
    dimensions = CharField(max_length=100, verbose_name="Rozměry", blank=True)
    tags = TaggableManager(blank=True, verbose_name="Tagy")

    def __str__(self):
        components = [self.title_cz, self.title_en]

        titles = list(filter(None, components))

        if self.dimensions:
            titles.append(self.dimensions)

        if self.technique:
            titles.append(self.technique)

        if self.material:
            titles.append(self.material)

        if self.year:
            titles.append(str(self.year))

        return f"{' / '.join(titles[:2])}, {', '.join(titles[2:])}"

    class Meta:
        verbose_name = "Dílo"
        verbose_name_plural = "Díla"
        ordering = ['-year', 'title']


class ArtworkImage(models.Model):
    artwork = ForeignKey(Artwork, on_delete=SET_NULL, related_name='images', null=True, blank=True)
    image = ImageField(upload_to='artworks/', verbose_name="Fotky", null=True, blank=True)

    def __str__(self):
        return f"{self.artwork.title_cz} - foto"

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotky"


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('catalog', 'Katalog'),
        ('book', 'Kniha'),
    ]

    title_cz = CharField(max_length=200, verbose_name="Název", null=True, blank=True)
    title_en = CharField(max_length=200, verbose_name="Title", null=True, blank=True)
    author = CharField(max_length=100, verbose_name="Autor", null=True, blank=True)
    publisher = CharField(max_length=100, verbose_name="Vydavatel", blank=True)
    year = PositiveIntegerField(verbose_name="Rok", null=True, blank=True)
    category = CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Kategorie", default='book', null=True, blank=True)
    tags = TaggableManager(blank=True, verbose_name="Tagy")

    def __str__(self):
        components = [self.title_cz, self.title_en]

        titles = list(filter(None, components))

        if self.author:
            titles.append(self.author)

        if self.publisher:
            titles.append(self.publisher)

        if self.year:
            titles.append(str(self.year))

        return f"{' / '.join(titles[:2])}, {', '.join(titles[2:])}"

    class Meta:
        verbose_name = "Kniha"
        verbose_name_plural = "Knihy"
        ordering = ['-year', 'title']


class BookImage(models.Model):
    book = ForeignKey(Book, on_delete=SET_NULL, related_name='images', null=True, blank=True)
    image = ImageField(upload_to='books/', verbose_name="Fotky", null=True, blank=True)

    def __str__(self):
        return f"{self.book.title_cz} - foto"

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotky"