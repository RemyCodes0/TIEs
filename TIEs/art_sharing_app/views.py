from django.shortcuts import get_object_or_404, render, redirect
from .models import Artwork, ArtworkComment, Like, Message, Userprofile, Event, PremiumAccount, TiesLogo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from TIEs.forms import ArtworkForm, CommentForm, Modifprof

# Create your views here.
def home(request):
    logo= TiesLogo.objects.all()
    artworks= Artwork.objects.all().order_by('-created_at')
    stat = Userprofile.objects.all()
    comments= ArtworkComment.objects.all() 
    return render(request, 'art_sharing_app/home.html',{'artwork':artworks, "comments":comments , "stat":stat, "logo":logo})



def like_artwork(request, artwork_id):
    logo= TiesLogo.objects.all()

    artwork= Artwork.objects.get(pk= artwork_id)
    
    if request.method == "POST":
        user= request.user
        artwork.save()
        if user in artwork.likes.all():
            artwork.likes.remove(user)
        else:
            artwork.likes.add(user)
    return redirect("home")

def comments(request, artwork_id):
    logo= TiesLogo.objects.all()

    artwork= get_object_or_404(Artwork, pk= artwork_id)
    comment=ArtworkComment.objects.all()
    form= CommentForm()
    if request.method== "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user= request.user
            comment.artwork = artwork
            comment.save()
            return redirect("comments", artwork_id = artwork_id)
        else:
            form = CommentForm()
    return render(request, "art_sharing_app/comments.html",{"artwork": artwork, "form":form, "comments":comment, "logo":logo} )

def ranking(request):
    logo= TiesLogo.objects.all()

    artwork =Artwork.objects.all()
    sorted_artworks = sorted(artwork, key= lambda x:x.likes.count(), reverse=True)
    top4 = sorted_artworks[4:]
    artwork2 =Artwork.objects.all()
    sorted_artworks2 = sorted(artwork2, key= lambda x:x.likes.count(), reverse=True)
    top1 = sorted_artworks[:1]

    artwork3 =Artwork.objects.all()
    sorted_artworks3 = sorted(artwork3, key= lambda x:x.likes.count(), reverse=True)
    top2 = sorted_artworks[1:2]

    artwork4 =Artwork.objects.all()
    sorted_artworks4 = sorted(artwork4, key= lambda x:x.likes.count(), reverse=True)
    top3 = sorted_artworks[2:3]




    return render(request, "art_sharing_app/ranking.html", {"artwork":top4, "artwork2":top1, "artwork3":top2, "artwork4":top3, "logo":logo})

def zoom(request, artwork_id):
    logo= TiesLogo.objects.all()

    artwork= get_object_or_404(Artwork, pk= artwork_id)
    return render(request, "art_sharing_app/zoom.html", {"artwork": artwork, "logo":logo})
    
def staff(request):
    logo= TiesLogo.objects.all()

    return render(request, "art_sharing_app/created_by.html", {"logo":logo})


def discussions(request):
    messages=Message.objects.all()
    return render(request, 'art_sharing_app/discussion.html', {"messages":messages})



def profile(request, user_id):
    logo= TiesLogo.objects.all()

    user=User.objects.get(id=user_id)
    profile = Userprofile.objects.filter(id= user_id)
    artworks= Artwork.objects.filter(user=user)
    return render(request, 'art_sharing_app/profile.html', {"user":user, "logo":logo, "artwork":artworks, 'profiles':profile})

def modifier_profile(request, user_id):
    try:
        logo= TiesLogo.objects.all()

        form= Modifprof()
        user = request.user.userprofile
        if request.method == "POST":
            form = Modifprof(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect("profile", user_id= user_id)
            else:
                form = Modifprof()
                print("non valid")
        return render(request, "art_sharing_app/modifier.html", {"form":form, "message":"no" , "logo":logo})
    except:
        logo= TiesLogo.objects.all()

        form2 = Modifprof()
        users = Userprofile(user = request.user)
        none = request.user.userprofile
        if request.method == "POST":
            form2 = Modifprof(request.POST, request.FILES, instance=users)
            if form2.is_valid():
                form2.save()
                return redirect("profile", user_id = user_id)
            else:
                form2 = Modifprof()
        return render(request, "art_sharing_app/modifier.html", {"form2":form2, "logo":logo})



@login_required 
def post_artwork(request):
    if request.method=='POST':
        #la soumission du formulaire pour les oeuvres d'art
        return render(request, "art_sharing_app/post_artwork.html")
    return render(request, "art_sharing_app/post_artwork.html")

def event(request):
    logo= TiesLogo.objects.all()

    events=Event.objects.all().order_by("-start_date")
    return render(request, "art_sharing_app/event.html", {'events':events, "logo":logo})
    
@login_required
def publish_event(request):
    if request.method=='POST':
        theme=request.POST.get('theme')
        start_date=request.POST.get('start_date')
        Event.objects.create(theme=theme, start_date=start_date)
        return redirect('current_event')
    return render(request, 'publish_event.html')


def current_event(request):
    current_event=Event.objects.last()
    return render(request, "art_sharing_app/current_event.html", {"current_event":current_event})

def artwork_detail(request, artwork_id):
    artwork=get_object_or_404(Artwork, pk=artwork_id)
    comments = ArtworkComment.objects.filter(artwork=artwork)
    if request.method=="POST":
        comment_text=request.POST.get('comment')
        ArtworkComment.objects.create(user=request.user,artwork=artwork)
        ArtworkComment.objects.create(user=request.user, artwork=artwork, comment=comment_text)
        return redirect('artwork_detail', artwork_id=artwork_id)
    return render(request, 'art_sharing_app/artwork_detail.html', {"artwork":artwork, 'comment':comments})

def add_artwork(request):
    logo= TiesLogo.objects.all()

    form= ArtworkForm()
    if request.method=='POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork= form.save(commit=False) 
            artwork.user= request.user
            artwork.save()
            return redirect("home") 
        else:
            print("not valide")
    return render(request, 'art_sharing_app/add_artwork.html', {'form':form, "logo":logo})       
