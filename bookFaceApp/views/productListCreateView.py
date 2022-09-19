from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bookFaceApp.models.products import Products
from bookFaceApp.serializers.productSerilizer import productoSerializer

class ProductListCreateView(APIView):
    permission_classes = (IsAuthenticated,)
   
    queryset = Products.objects.all()
    serializer_class = productoSerializer
   
    def get(self, request, *args, **kwargs):
        '''
        List all the products for given requested user
        '''
        products = Products.objects.all()
        serializer = productoSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def post(self, request, *args, **kwargs):
        serializer = productoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)


