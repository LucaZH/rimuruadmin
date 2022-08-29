from rest_framework import serializers
from .models import CentreMedical, Pharmacie , Utilisateur,Conseil,roleuser

class UtilisateurapiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fb_id = serializers.CharField(required=True, allow_blank=False, max_length=200)
    state = serializers.CharField(required=False,default='START')
    query = serializers.CharField(required=False, allow_blank=True, max_length=200)
    role = serializers.ChoiceField(choices=roleuser, default='normaluser')

    def create(self, validated_data):
        return Utilisateur.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fb_id = validated_data.get('fb_id', instance.fb_id)
        instance.state = validated_data.get('state', instance.state)
        instance.query = validated_data.get('query', instance.query)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
class CentreMedicalapiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(required=True, allow_blank=False, max_length=200)
    localisation = serializers.CharField(required=True, allow_blank=False, max_length=200)
    contact = serializers.CharField(required=False, allow_blank=True, max_length=200)
    verifier = serializers.BooleanField()
    publier_par =serializers.CharField(required=True,max_length=100,allow_blank=False)
    zone = serializers.IntegerField()
    def create(self, validated_data):
        return CentreMedical.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nom = validated_data.get('nom', instance.nom)
        instance.verifier = validated_data.get('verifier', instance.verifier)
        instance.localisation = validated_data.get('localisation', instance.localisation)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.publier_par = validated_data.get('publier_par', instance.publier_par)
        instance.save()
        return instance
class PharmacieapiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(required=True, allow_blank=False, max_length=200)
    localisation = serializers.CharField(required=True, allow_blank=False, max_length=200)
    contact = serializers.CharField(required=False, allow_blank=True, max_length=200)
    verifier = serializers.BooleanField()
    publier_par =serializers.CharField(required=True,max_length=100,allow_blank=False)
    zone = serializers.IntegerField()
    def create(self, validated_data):
        return Pharmacie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nom = validated_data.get('nom', instance.nom)
        instance.verifier = validated_data.get('verifier', instance.verifier)
        instance.localisation = validated_data.get('localisation', instance.localisation)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.publier_par = validated_data.get('publier_par', instance.publier_par)
        instance.save()
        return instance
class ConseilapiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length = 30000)
    
    def create(self, validated_data):
        return Conseil.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance