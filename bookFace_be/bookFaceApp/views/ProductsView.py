from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bookFaceApp.models.products import products
from bookFaceApp.serializers.productSerializer import productSerializer
 
class productsView(APIView):
    permission_classes = (IsAuthenticated,)
   
    queryset = products.objects.all()
    serializer_class = productSerializer

    def get_object(self, product):
        '''
        Helper method to get the object with given product id
        '''
        try:
            return products.objects.get(product=product)
        except products.DoesNotExist:
            return None

       
    def get(self, request, *args, **kwargs):
        '''
        Retrieves the product with given product id
        '''
        product_instance = self.get_object(kwargs['pk'])
        if not product_instance:
            return Response(
                {"res": "Object with inventory id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = productSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = productSerializer(data=request.data)
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
     
        serializer = productSerializer(instance =product_instance, data=request.data, partial = True)
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
