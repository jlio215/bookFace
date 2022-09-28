from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bookFaceApp.models.sales import Sales
from bookFaceApp.serializers.salesSerializer import salesSerializer
 
class salesView(APIView):
    permission_classes = (IsAuthenticated,)
   
    queryset = Sales.objects.all()
    serializer_class = salesSerializer

    def get_object(self, sale):
        '''
        Helper method to get the object with given sale id
        '''
        try:
            return Sales.objects.get(sale=sale)
        except Sales.DoesNotExist:
            return None

       
    def get(self, request, *args, **kwargs):
        '''
        Retrieves the sales with given sales id
        '''
        sales_instance = self.get_object(kwargs['pk'])
        if not sales_instance:
            return Response(
                {"res": "Object with sales id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = salesSerializer(sales_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = salesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   
   
    def put(self, request, *args, **kwargs):
        '''
        Updates the sales item with given brach id if exists
        '''
        sales_instance = self.get_object(kwargs['pk'])
        if not sales_instance:
            return Response(
                {"res": "Object with sales id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = salesSerializer(instance =sales_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the sales item with given sales id if exists
        '''
        sales_instance = self.get_object(kwargs['pk'])
        if not sales_instance:
            return Response(
                {"res": "Object with sales id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        sales_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
