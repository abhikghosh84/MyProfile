from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='readinapp-index'),
    path('createsubject/', views.create, name='readinapp-create-redir'),
    path('editsubject/<int:id>', views.edit, name='readinapp-edit'),
    path('updatesubject/<int:id>', views.update, name='readinapp-update-redir'),
    path('deletesubject/<int:id>', views.delete, name='readinapp-delete-redir'),
    path('viewtopic/<int:id>', views.viewtopic, name='readinapp-view-topic'),
    path('viewtopicdetails/<int:id>/<int:sid>', views.viewtopicdetails, name='readinapp-view-topic-details'),
    path('edittopic/<int:id>/<int:sid>', views.edittopic, name='readinapp-edit-topic'),
    path('updatetopic/<int:id>/<int:sid>', views.updatetopic, name='readinapp-update-topic-redir'),
    path('createtopic/<int:id>', views.createtopic, name='readinapp-create-topic-redir'),
    path('deletetopic/<int:id>/<int:sid>', views.deletetopic, name='readinapp-delete-topic-redir'),
]