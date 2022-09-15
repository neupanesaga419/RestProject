from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework import mixins
from rest_framework import generics

from myapp.models import Parents, Person, Student
from myapp.serializers import ParentsSerializer, PersonSerilizer, StudentSerializer


class OncePerDay(UserRateThrottle):
    rate = "3/day"

@api_view(['GET'])
@throttle_classes([OncePerDay])
def index(request):

    # return render(request, 'index.html')
    return Response({"msg":"Hello for today.. See you tomorrow"})


@api_view(['GET'])
def get_person(request):
    query = Person.objects.all()
    print("content_type",request.content_type)
    print("method",request.method)
    print("stream",request.stream)
    print("authentication", request.auth)
    print("Sessions", request.session)
    serializer = PersonSerilizer(query, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_new_person(request):
    data = request.data
    print(data)
    serializer = PersonSerilizer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"data successfully inserted","data":serializer.data})
    else:
        return Response(serializer.errors)


class PersonView(APIView):

    def get(self,request):
        query = Person.objects.all()
        serializer = PersonSerilizer(query,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data 
        serializer = PersonSerilizer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"data successfully inserted","data":serializer.data})


class PersonDetailAV(APIView):

    def get(self,request,pk):
            try:
                query = Person.objects.get(pk=pk)
            except Person.DoesNotExist:
                return Response({"msg":"Person with given id doesnot exists."})
            
            serializer = PersonSerilizer(query)
            return Response(serializer.data)
        
    def put(self,request,pk):
        try:
            query = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({"msg":"Person with given id doesnot exists."})
        data = request.data
        serializer = PersonSerilizer(query,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Data Updated","updated_data":serializer.data})
    
    def patch(self,request,pk):
        try:
            query = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({"msg":"Person with given id doesnot exists."})
        data = request.data
        serializer = PersonSerilizer(query,data=data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Data Updated","updated_data":serializer.data})

    def delete(self,request,pk):
        try:
            query = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({"msg":"Person with given id doesnot exists."})
        query.delete()
        return Response({"msg":"data successfully deleted."})   




class PersonListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    serializer_class = PersonSerilizer
    queryset = Person.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class PersonDetailGAV(mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin,
            generics.GenericAPIView
                    ):
        
        serializer_class = PersonSerilizer
        queryset = Person.objects.all()

        def get(self,request,*args,**kwargs):
            return self.retrieve(request,*args,**kwargs)
        
        def put(self,request,*args,**kwargs):
            return self.update(request,*args,**kwargs)
        
        def patch(self,request,*args,**kwargs):
            return self.partial_update(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
        
        

class StudentListAV(APIView):

    def get(self,request):
        query = Student.objects.all()
        serializer = StudentSerializer(query,many=True)
        return Response(serializer.data)


class ParentsListAV(APIView):

    def get(self,request):
        query = Parents.objects.all()
        serializer = ParentsSerializer(query,many=True)
        return Response(serializer.data)

class ParentDetailAV(mixins.RetrieveModelMixin,generics.GenericAPIView):

    serializer_class = ParentsSerializer
    queryset = Parents.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
