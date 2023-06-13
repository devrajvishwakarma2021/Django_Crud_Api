from django.shortcuts import render
# Create your views here.
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import Productserializers

#  @api_view(['GET'])
# def apiOverview(request):
#     api_urls ={
#         'List': '/product-list/',
#         'Detail View':  '/product-detail/<int:id>',
#         'create': '/product-create/',
#         'Update':'/product-update/<int:id>',
#         'Delete':'/product-detail/<int:id>',

#     }
#     return Response(api_urls)



@api_view(['GET'])
def showall(request):
    products =Product.objects.all()
    serializer = Productserializers(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewOneProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = Productserializers(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreatProduct(request):
    serializer =Productserializers(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
    
@api_view(['POST'])
def UpdateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer=Productserializers(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

@api_view(['GET'])
def DeleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Item Successfully deleted')
    