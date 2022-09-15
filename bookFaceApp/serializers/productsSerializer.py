from bookFaceApp.models.products import products
from rest_framework import serializers

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['idproducts','name_prod','author','editorial','category','type_prod',
                  'num_page','isbn','state','rank','format_prod','presentation','image','price',
                  'visits','description','name_cat','subcategory','amount','stock_prod','user']
        
        
        
      
        
        
        
       
        
        
        
        
   
        
        
        
        
        
        
  