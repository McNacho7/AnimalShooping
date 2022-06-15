from rest_framework import serializers
from .models import comidagatos, comidaperro, accesorio
 

class comidagatosSerializer(serializers.ModelSerializer):   
    class Meta:
        model = comidagatos
        fields = '__all__'

class comidaperroSerializer(serializers.ModelSerializer):   
    class Meta:
        model = comidaperro
        fields = '__all__'

class accesorioSerializer(serializers.ModelSerializer):   
    class Meta:
        model = accesorio
        fields = '__all__'

