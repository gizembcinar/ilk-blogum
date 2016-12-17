from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):     
    posts = Post.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
	
	
def post_detail(request, pk):
   post = get_object_or_404(Post, pk=pk)
   print("deneme")
   return render(request, 'blog/post_detail.html', {'post': post})