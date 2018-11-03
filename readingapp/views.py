from django.shortcuts import render, redirect
from django.db.models import Sum, Count
from .models import Subject, Topic

def index(request):
    subjects = Subject.objects.all().order_by('tag', 'name')
    print('Count of Subjects Found: '+str(subjects.count()))
    #con_sub = {}
    for subject in subjects:
        subject.count = Topic.objects.filter(subject_id=subject.id).aggregate(Count('estimation'))
        subject.total = Topic.objects.filter(subject_id=subject.id).aggregate(Sum('estimation'))
        # con_sub.update({
        #     'name': subject.name,
        #     'tag': subject.tag,
        #     'updated_at': subject.updated_at,
        #     'count': Topic.objects.filter(subject_id=subject.id).aggregate(Count('estimation')),
        #     'total': Topic.objects.filter(subject_id=subject.id).aggregate(Sum('estimation')),
        # })
    #print('>> '+str(con_sub.values()))
    print('>>> ' + str(subjects))
    context = {
        'title': 'Welcome to Reading App',
        'subjects': subjects,
    }
    return render(request, template_name='readingapp/createviewsubject.html', context=context)

def create(request):
    print(request.POST)
    subject = Subject(name = request.POST['name'], tag = request.POST['tag'])
    subject.save()
    return redirect('/reading/')

def edit(request, id):
    subject = Subject.objects.get(id=id)
    context = {
        'title': 'Edit Subject',
        'subject': subject
    }
    return render(request, template_name='readingapp/editsubject.html', context=context)

def update(request, id):
    subject = Subject.objects.get(id=id)
    subject.name = request.POST['name']
    subject.tag = request.POST['tag']
    subject.save()
    return redirect('/reading/')

def delete(request, id):
    Subject.objects.get(id=id).delete()
    return redirect('/reading/')

def viewtopic(request, id):
    subject1 = Subject.objects.get(id=id)
    topics = Topic.objects.filter(subject_id=id).order_by('name')
    context = {
        'title': 'Topics',
        'topics': topics,
        'subject': subject1
    }
    return render(request, template_name='readingapp/createviewtopic.html', context=context)

def viewtopicdetails(request, id, sid):
    topic = Topic.objects.get(id=id)
    subject = Subject.objects.get(id=sid)
    context = {
        'title': topic.name+' Details',
        'topic': topic,
        'subject': subject
    }
    return render(request, template_name='readingapp/topicdetails.html', context=context)

def edittopic(request, id, sid):
    topic = Topic.objects.get(id=id)
    subject = Subject.objects.get(id=sid)
    context = {
        'title': 'Edit Topic',
        'topic': topic,
        'subject': subject
    }
    return render(request, template_name='readingapp/edittopic.html', context=context)

def updatetopic(request, id, sid):
    topic=Topic.objects.get(id=id)
    topic.name = request.POST['topicname']
    topic.estimation = request.POST['estimation']
    topic.embed_link = request.POST['url']
    topic.pct_completed = request.POST['pct']
    topic.details = request.POST['textarea']
    topic.subject_id=sid
    topic.save()
    sid_str = str(sid)
    return redirect('/reading/viewtopic/' + sid_str)

def createtopic(request, id):
    topic = Topic(name=request.POST['topicname'], estimation=request.POST['estimation'], subject_id=id, details=request.POST['textarea'], embed_link=request.POST['url'])
    topic.save()
    id_str = str(id)
    return redirect('/reading/viewtopic/'+id_str)

def deletetopic(request, id, sid):
    Topic.objects.get(id=id).delete()
    sid_str = str(sid)
    return redirect('/reading/viewtopic/' + sid_str)
