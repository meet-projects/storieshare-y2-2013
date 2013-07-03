from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from models import story
from models import Paragraph
def homepage (request):
    return render(request,'stories/storieshare.html',{})

def addstory (request):
    return render(request,'stories/add_story.html',{})

def newstory (request):
	Headline = request.POST["Headline"]
	Description  = request.POST["Description"]
	Story = request.POST["Story"]
	a = story (storyHeadline = Headline , storyDescription = Description )
	a.save ()	
	b = Paragraph (pargraphContent = Story, story = a)
	b.save ()
	return HttpResponseRedirect ('writtenstory')

def writtenstory (request) :
	List_of_stories = story.objects.all ()
	story_to_show = List_of_stories[(len(List_of_stories)-1)]
	List_of_paragraphs = Paragraph.objects.filter (story = story_to_show)
	context = {"paragraphs" : List_of_paragraphs}
	
	return render(request,'stories/written_story.html',context)
def readstory (request) :
	List_of_stories = story.objects.all()
	List_of_paragraphs = Paragraph.objects.all()
	context = {"stories": List_of_stories, "paragraphs" : List_of_paragraphs}
	return render(request,'stories/read_stories.html',context)
def showstory(request,story_id) :
	s = story.objects.filter(storyID=story_id)
	List_of_para = Paragraph.objects.filter(story = s[0])
	context = {"paragraphs" : List_of_para}
	return render(request,'stories/show_story.html',context)
	
	
