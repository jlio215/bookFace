from rest_framework.views import APIView

from bookFaceApp.models.products import products
from bookFaceApp.serializers.productSerializer import productSerializer
from django.http.response import JsonResponse

class productsHomeView(APIView):
   
    queryset = products.objects.all()
    serializer_class = productSerializer
       
    def get(self, request):
        allProducts =  list(products.objects.values())
        
        if len(allProducts)>0:
            datos={'queryset':allProducts}
        else:
            datos={'message':'no found'}
        return JsonResponse( datos, safe=False )