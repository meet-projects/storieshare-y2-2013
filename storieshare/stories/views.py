from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from models import story
from models import Paragraph
from models import comment
from django import forms
#from django.contrib.auth import authenticate
#from django.contrib.auth import logout
#from django.contrib.auth import User

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


def newcomment (request,story_id) :
	s = request.POST["Story"]
	com = request.POST["Com"]
	w = request.POST["Writer"]	
	c=comment (writer = w , commentContent = com , story= s)
	c.save()
	s = story.objects.filter(storyID=story_id)
	List_of_para = Paragraph.objects.filter(story = s[0])
	c=story.objects.filter(storyID=story_id)
	context = {"paragraphs" : List_of_para,"coms":c}
	render(request,'stories/show_story.html',context)



def writtenstory (request) :
	List_of_stories = story.objects.all ()
	story_to_show = List_of_stories[(len(List_of_stories)-1)]
	List_of_paragraphs = Paragraph.objects.filter (story = story_to_show)
	context = {"paragraphs" : List_of_paragraphs}
	
	return render(request,'stories/written_story.html',context)


#User.objects.create_user(username,email,password,last_name=,first_name=)

#class UserRegistrationForm (forms.Form):
#	username = forms.CharField (label = u"username")
#	password = forms.CharField (label = u"password")
#	email = forms.CharField (label = u"email")
#	first_name = forms.CharField (label = u"first_name")
#	last_name = forms.CharField (label = u"last_name")

#def register (request):
#	return render (request, "submit/register.html", {form : UserRegistrationForm})

#def login (request) :
#	return render (request,"submit/login.html", {} )


#def submitlogin (request) :
#	Username = request.POST ["username"]
#	Password = request.POST ["password"]
#	user = authenticate (username = , password = 
#	if user is not None :
#		if user.is_active :
#			login (request, user)
#			return HttpResponseRedirect ("profile")
#		else:
#	else:

#def logout (request) :
#	logout (request)


#def profile (request) :
#	context = {"username" : ""}
#	return render (request, "submit/profile.html", context)

def readstory (request) :
	List_of_stories = story.objects.all()
	List_of_paragraphs = Paragraph.objects.all()
	context = {"stories": List_of_stories, "paragraphs" : List_of_paragraphs}
	return render(request,'stories/read_stories.html',context)



def showstory(request,story_id) :
	s = story.objects.filter(storyID=story_id)
	List_of_para = Paragraph.objects.filter(story = s[0])
	c=story.objects.filter(storyID=story_id)
	context = {"paragraphs" : List_of_para,"coms":c}
	return render(request,'stories/show_story.html',context)
	
