from django.urls import path, include
from students.views import  (index, show, delete, create,createViaForm, editViaForm,
                             CreateStudentClassView, EditStudentClassView)
urlpatterns = [

    path('', index, name='students.index'),
    path('<int:id>', show, name='students.show'),
    path('<int:id>/delete', delete, name='students.delete'),
    path('create', create, name='students.create'),
    path('forms/create', createViaForm, name='students.forms.create'),
    # path('<int:id>/edit', editViaForm, name='students.edit'),
    path('views/create', CreateStudentClassView.as_view(), name='students.create.views'),
    path('views/<int:id>/edit', EditStudentClassView.as_view(), name='students.edit')

]