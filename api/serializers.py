from django.db.models import fields

from .models import  Song
from rest_framework import serializers
class SongSerializer(serializers.ModelSerializer):
   # cloths = SongSerializer_1(many= True, read_only =True)
    class Meta:
        model = Song
        fields = ['id', 'title','cloths']

    def to_representation(self, instance):
        self.fields['cloths'] = SongSerializer(read_only=True)
        return super(SongSerializer, self).to_representation(instance)


# class SingerSerializer(serializers.ModelSerializer):
#     sungby = SongSerializer(many= True, read_only =True)
#     class Meta:
#         model = Singer
#         fields = ['id', 'title', 'singer', 'sungby' ]

