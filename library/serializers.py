from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Author, Book, Review

# ✅ Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# ✅ Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# ✅ Review Serializer (للداخل والخارج)
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'book', 'rating', 'comment', 'created_at', 'updated_at']

# ✅ Book Serializer (مع معلومات المؤلف والتصنيف والمراجعات)
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    # للسماح بإدخال ID في POST
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Book
        fields = [
            'author_id','category_id', 'title', 'description', 'pdf_file', 
            'author', 'category', 'cover_image', 'paper_number','reviews'
        ]
