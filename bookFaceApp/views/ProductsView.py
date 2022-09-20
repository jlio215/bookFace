from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bookFaceApp.models.products import Products
from bookFaceApp.serializers.productSerilizer import productoSerializer
 
class productsView(APIView):
    #permission_classes = (IsAuthenticated,)
   
    queryset = Products.objects.all()
    serializer_class = productoSerializer
       
    def get(self, request, *args, **kwargs):
        '''
        Retrieves the product with given product id
        '''
        product_instance = self.get_object(kwargs['pk'])
        if not product_instance:
            return Response(
                {"res": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = productoSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = productoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   
   
    def put(self, request, *args, **kwargs):
        '''
        Updates the product item with given product id if exists
        '''
        product_instance = self.get_object(kwargs['pk'])
        if not product_instance:
            return Response(
                {"res": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = productoSerializer(instance =product_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the product item with given product id if exists
        '''
        product_instance = self.get_object(kwargs['pk'])
        if not product_instance:
            return Response(
                {"res": "Object with product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        product_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
