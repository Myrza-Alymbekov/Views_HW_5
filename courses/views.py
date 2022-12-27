from django.shortcuts import render
from rest_framework import viewsets, generics

from courses.my_generics import ListMixinAPI, CreateMixinAPI,\
                                            RetrieveMixinAPI, UpdateMixinApi,\
                                            DeleteMixinApi, MyAPIView, ListMixinStudentAPI,\
                                            CreateMixinStudentAPI
from courses.models import Course, Student, Mentor
from courses.serializers import CourseSerializer, StudentSerializer, MentorSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentListCreateAPIView(ListMixinStudentAPI, CreateMixinStudentAPI, MyAPIView):
    serializer_class = StudentSerializer
    model = Student

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrieveUpdateDestroyAPIView(RetrieveMixinAPI,
                                          DeleteMixinApi,
                                          UpdateMixinApi,
                                          MyAPIView):
    serializer_class = StudentSerializer
    model = Student

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MentorAPIViewSet(ListMixinAPI,
                       CreateMixinAPI,
                       RetrieveMixinAPI,
                       UpdateMixinApi,
                       DeleteMixinApi,
                       viewsets.ViewSetMixin,
                       MyAPIView):
    serializer_class = MentorSerializer
    model = Mentor
    queryset = Mentor.objects.all()


