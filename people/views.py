from people.models import Person
from people.serializers import PersonSerializer
from rest_framework.views import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def people_list(request):
    if request.method == 'GET':
        if len(request.query_params) == 0:
            people = Person.objects.all()
            serializer = PersonSerializer(people, many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        name = request.query_params.get("name")
        if name is None:
            return Response({"error" : "no name in query params"}, status = status.HTTP_400_BAD_REQUEST)
        else:
            people = Person.objects.filter(name=name)
            if len(people) == 0:
                return Response(status = status.HTTP_404_NOT_FOUND)
            else:
                serializer = PersonSerializer(people, many = True)
                return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
