from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
 
from bookFaceApp.models.inventory import Inventory
from bookFaceApp.serializers.inventorySerializer import inventorySerializer

class InventoryCreateView(APIView):
    permission_classes = (IsAuthenticated,)
   
    queryset = Inventory.objects.all()
    serializer_class = inventorySerializer
   
    def get(self, request, *args, **kwargs):
        '''
        List all the inventory for given requested user
        '''
        inventories = Inventory.objects.all()
        serializer = inventorySerializer(inventories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = inventorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        '''
        Updates the inventory item with given inventory if exists
        '''
        inventory_instance = self.get_object(kwargs['pk'])
        if not inventory_instance:
            return Response(
                {"res": "Object with inventory id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = inventorySerializer(instance =inventory_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


       

