from django.db import models
from django.contrib.auth.models import User

# تصنيفات الكتب
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# المؤلفين
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name

# الكتب
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    pdf_file = models.FileField(upload_to='books/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Language = models.Choices = (
    #     ('EN', 'English'),
    #     ('FR', 'French'),
    #     ('ES', 'Spanish'),
    #     ('DE', 'German'),
    #     ('IT', 'Italian'),
    #     ('PT', 'Portuguese'),
    #     ('RU', 'Russian'),
    #     ('ZH', 'Chinese'),
    #     ('JA', 'Japanese'),
    #     ('AR', 'Arabic'),
    # )
    paper_number = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title

# التقييمات/المراجعات
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.rating})"
