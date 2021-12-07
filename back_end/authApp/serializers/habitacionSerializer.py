from authApp.models.habitacion    import Habitacion
from rest_framework                 import serializers

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['codigo', 'descripcion' , 'disponibilidad' , 'precio']
    def to_representation(self, obj):
        habitacion = Habitacion.objects.get(id=obj.id)
        return {
            'id'                : habitacion.id,
            'codigo'            : habitacion.codigo,
            'descripcion'       : habitacion.descripcion,
            'disponibilidad'    : habitacion.disponibilidad,
            'precio'            : habitacion.precio,
        }
