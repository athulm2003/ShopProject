from django.shortcuts import render


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Myapp.models import Category, ProductDb
from Myapp.serializers import CategorySerializer, ProductSerializer

class CategoryListCreateView(APIView):

    def get(self, request):
        qs = Category.objects.all()
        serializer_instance = CategorySerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = CategorySerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                {"msg": "Category Created Successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CategoryRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(Category, id=pk)
        serializer_instance = CategorySerializer(qs)
        return Response(serializer_instance.data)

    def put(self, request, pk):
        qs = get_object_or_404(Category, id=pk)

        serializer_instance = CategorySerializer(
            qs, data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        qs = get_object_or_404(Category, id=pk)
        qs.delete()

        return Response({"msg": "Category Deleted Successfully"})


class ProductListCreateView(APIView):

    def get(self, request):
        qs = ProductDb.objects.all()
        serializer_instance = ProductSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = ProductSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                {"msg": "Product Created Successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProductRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(ProductDb, id=pk)
        serializer_instance = ProductSerializer(qs)
        return Response(serializer_instance.data)

    def put(self, request, pk):
        qs = get_object_or_404(ProductDb, id=pk)

        serializer_instance = ProductSerializer(
            qs, data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        qs = get_object_or_404(ProductDb, id=pk)
        qs.delete()

        return Response({"msg": "Product Deleted Successfully"})

class ProductByCategoryView(APIView):

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)

        qs = ProductDb.objects.filter(category=category)

        serializer_instance = ProductSerializer(qs, many=True)

        return Response(serializer_instance.data)