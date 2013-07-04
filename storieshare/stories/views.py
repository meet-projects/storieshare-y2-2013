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
def search (request):
	string = request.POST["searchString"]
	List_of_stories = story.objects.filter(storyHeadline=string)	
	context = {"stories": List_of_stories}
	return render(request,'stories/read_stories.html',context)




def newstory (request):
	Headline = request.POST["Headline"]
	Description  = request.POST["Description"]
	Story = request.POST["Story"]
	public= request.POST["storyPublic"]
	genre_name=request.POST["storyPublic"]
	story_genre=genre.objects.filter(genreName=genre_name)
	publicbool=False
	if public=="1":
		publicbool=True
	else:
		publicbool=False
	print publicbool
	a = story (storyHeadline = Headline , storyDescription = Description, storyPublic=publicbool, storyGenre=story_genre[0])
	a.save ()	
	b = Paragraph (pargraphContent = Story, story = a)
	b.save ()
	return HttpResponseRedirect ('writtenstory')


def newcomment (request,story_id) :
	s = request.POST["Story"]
	d=story.objects.filter(storyID=story_id)
	p=d[0]
	com = request.POST["Com"]
	w = request.POST["Writer"]	
	c=comment (writer = w , commentContent = com , story= p)
	c.save()
	s = story.objects.filter(storyID=story_id)
	List_of_para = Paragraph.objects.filter(story = s[0])
	c=story.objects.filter(storyID=story_id)
	context = {"paragraphs" : List_of_para,"coms":c,"t":story_id}
	return HttpResponseRedirect ('/readstory/'+str(story_id))



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
def newpara (request,story_id) :
	s = story.objects.filter(storyID=story_id)
	List_of_para = Paragraph.objects.filter(story = s[0])
	context = {"paragraphs" : List_of_para,"t":story_id}
	return render(request,'stories/add_paragraph.html',context)



def addpara (request,story_id) :
	com = request.POST["Para"]
	s = story.objects.filter(storyID=story_id)
	para_s=s[0]
	b = Paragraph (pargraphContent = com, story = para_s)
	b.save()	
	List_of_para = Paragraph.objects.filter(story = s[0])
	c=story.objects.filter(storyID=story_id)
	context = {"paragraphs" : List_of_para,"coms":c,"t":story_id}
	return HttpResponseRedirect ('/readstory/'+str(story_id))

def readstory (request) :
	List_of_stories = story.objects.all()
	
	context = {"stories": List_of_stories}
	return render(request,'stories/read_stories.html',context)



def showstory(request,story_id) :
	s = story.objects.filter(storyID=story_id)
	List_of_para = Paragraph.objects.filter(story = s[0])
	c=comment.objects.filter(story=s[0])
	
	context = {"paragraphs" : List_of_para,"coms":c,"t":story_id}
	return render(request,'stories/show_story.html',context)
	
