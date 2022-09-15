from django.urls import path
import myapp.views as miv

urlpatterns = [

    path('', miv.index, name='index'),
    path('get_person', miv.get_person, name="get-all-person"),
    path('add_new_person', miv.add_new_person, name="add-new-person"),

    path('person_view', miv.PersonView.as_view(), name="person-view"),
    path('person_detail/<int:pk>', miv.PersonDetailAV.as_view(), name="person-detail-view"),

    path('person_list', miv.PersonListView.as_view(), name='person-list'),
    path('person/<int:pk>', miv.PersonDetailGAV.as_view(), name='person-detail'),


    path('studentlist', miv.StudentListAV.as_view(), name='studentlist'),
    path('parentslist', miv.ParentsListAV.as_view(), name='parentslist'),

    path('parentdetail/<int:pk>', miv.ParentDetailAV.as_view(), name="parent-detail"),
]