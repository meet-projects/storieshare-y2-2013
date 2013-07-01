from django.http import HttpResponse
from django.shortcuts import render
from models import story
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
	return HttpResponseRedirect ('writtenstory')

def writtenstory (request) :
	List_of_stories = story.objects.all ()
	story_to_show = List_of_stories [-1]
	List_of_paragraphs = Paragraph.objects.filter (story = story_to_show)
	context = {"paragraphs" : List_of_paragraphs}
	
	return render(request,'stories/written_story.html',context)
