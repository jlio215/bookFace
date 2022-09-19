from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from bookFaceApp.models.cart import Cart
from bookFaceApp.serializers.cartSerializer import cartSerializer
 
class cartView(APIView):
    permission_classes = (IsAuthenticated,)
   
    queryset = Cart.objects.all()
    serializer_class = cartSerializer
       
    def get(self, request, *args, **kwargs):
        '''
        Retrieves the cart with given cart id
        '''
        cart_instance = self.get_object(kwargs['pk'])
        if not cart_instance:
            return Response(
                {"res": "Object with cart id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = cartSerializer(cart_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = cartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   
    def put(self, request, *args, **kwargs):
        '''
        Updates the cart item with given cart id if exists
        '''
        cart_instance = self.get_object(kwargs['pk'])
        if not cart_instance:
            return Response(
                {"res": "Object with cart id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = cartSerializer(instance =cart_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the cart item with given cart id if exists
        '''
        cart_instance = self.get_object(kwargs['pk'])
        if not cart_instance:
            return Response(
                {"res": "Object with cart id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        cart_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
