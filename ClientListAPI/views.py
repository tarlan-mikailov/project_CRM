from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
# from rest_framework import authentication, permissions
from .serializers import ClientSerializer
from clientapp.models import Client as ClientModel
from django.core.paginator import Paginator, EmptyPage

# Create your views here.

class ClientList(APIView):

    def get(self, request):
        clients = ClientModel.objects.all()
        birthday_date = request.query_params.get('birthday')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=5)
        page = request.query_params.get('page', default = 1)
        if birthday_date:
            clients = clients.filter(birthday=birthday_date)
        if search:
            clients = clients.filter(first_name__istartswith=search)
        if ordering:
            ordering_fields = ordering.split(',')
            clients = clients.order_by(*ordering_fields)
        paginator = Paginator(clients, per_page=perpage)
        try:
            clients = paginator.page(number=page)
        except EmptyPage:
            clients = []
        serialized_data = ClientSerializer(clients, many=True)
        return Response(serialized_data.data, status.HTTP_200_OK)
    
    def post(self, request):
        deserialized_data = ClientSerializer(data=request.data)
        if deserialized_data.is_valid():
            client = deserialized_data.save()
            client.save()
        return Response(deserialized_data.data, status.HTTP_201_CREATED)


class Client(APIView):

    def get(self, request, pk):
        client = get_object_or_404(ClientModel, pk=pk)
        serialized_data = ClientSerializer(client)
        return Response(serialized_data.data, status.HTTP_200_OK)

    def put(self, request, pk):
        client = get_object_or_404(ClientModel, pk=pk)
        deserialized_data = ClientSerializer(client, data=request.data)
        if deserialized_data.is_valid():
            client_model = deserialized_data.save()
            client_model.save()
        return Response(deserialized_data.data, status.HTTP_200_OK)
    
    def patch(self, request, pk):
        client = ClientModel.objects.get(id=pk)
        deserialized_data = ClientSerializer(client, data=request.data, partial=True)
        if deserialized_data.is_valid():
            client_model = deserialized_data.save()
            client_model.save()
            return Response(deserialized_data.data, status.HTTP_200_OK)
        return Response(deserialized_data.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        client = ClientModel.objects.get(id=pk)
        name = f"{client.first_name} {client.last_name}"
        client.delete()
        return Response({"message": f"client {name} deleted"}, status.HTTP_200_OK)


# class ClientListView(generics.ListCreateAPIView):
#     queryset = ClientModel.objects.all()
#     serializer_class = ClientSerializer

# class DeleteClientView(generics.DestroyAPIView):
#     queryset = ClientModel.objects.all()
#     serializer_class = ClientSerializer