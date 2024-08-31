from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly
from .paginations import CustomPagination
from rest_framework.response import Response

# افزودن ماژول فیلترینگ داده ها
from django_filters.rest_framework import DjangoFilterBackend

# ماژول سرچ و جستجو در فیلترها
from rest_framework.filters import SearchFilter, OrderingFilter

# from rest_framework.views import APIView

# from rest_framework.generics import (
#     GenericAPIView, ListAPIView, ListCreateAPIView,
#     RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, )
# from rest_framework.mixins import (
#     ListModelMixin,CreateModelMixin,DestroyModelMixin,
#     UpdateModelMixin,RetrieveModelMixin, )

from rest_framework import viewsets

from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404

"""
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serialized = PostSerializer(posts,many=True)
        return Response(serialized.data)
    elif request.method == 'POST':
        serialized = PostSerializer(data=request.data)
        # if serialized.is_valid():
        #     serialized.save()
        #     return Response(serialized.data)
        # else:
        #     return Response(serialized.errors)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)
"""
"""
class PostList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request):
        posts = Post.objects.all()
        serialized = PostSerializer(posts,many=True)
        return Response(serialized.data)

    def post(self,request):
        serialized = PostSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)                
"""

"""
class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
"""
# def get(self, request):
#     query_set = self.get_queryset()
#     serialized = self.serializer_class(query_set,many=True)
#     return Response(serialized.data)

# def post(self,request):
#     serialized = self.serializer_class(data=request.data)
#     serialized.is_valid(raise_exception=True)
#     serialized.save()
#     return Response(serialized.data)


"""
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetails(request,id):
    # return error message using try catch
    # try:
    #     post = Post.objects.get(pk=id)
    #     serialized = PostSerializer(post)
    #     return Response(serialized.data)
    # except Post.DoesNotExist:
    #     return Response({'detail':"Record dosn't exist"},status=status.HTTP_404_NOT_FOUND)

    # return error message using get_object_or_404() function
    post = get_object_or_404(Post,pk=id)
    if request.method  == 'GET':
        serialized = PostSerializer(post)
        return Response(serialized.data)
    elif request.method == 'PUT':
        serialized = PostSerializer(post,data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'Deleting performed successfully'},status=status.HTTP_204_NO_CONTENT)
"""

"""
class PostDetails(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request,id):
        post = get_object_or_404(Post,pk=id)        
        serialized = self.serializer_class(post)
        return Response(serialized.data)
    
    def put(self,request,id):
        post = get_object_or_404(Post,pk=id)   
        serialized = self.serializer_class(post,data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)     

    def delete(self,request,id):
        post = get_object_or_404(Post,pk=id)   
        post.delete()
        return Response({'detail':'Deleting performed successfully'},status=status.HTTP_204_NO_CONTENT)
"""

""" class PostDetails(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin): """


"""
class PostDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
"""

"""
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs) 
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
"""

# def get(self, request,id):
#     post = get_object_or_404(Post,pk=id)
#     serialized = self.serializer_class(post)
#     return Response(serialized.data)


class PostModelViewSet(viewsets.ModelViewSet):

    # (Owner)صدور مجوز تغییر فقط برای کاربر ایجاد کننده پست
    # (IsOwnerOrReadOnly)و بقیه کاربران تنها مشاهده محتوای پست
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # (ordering)ایجاد امکان فیلترینگ رکوردها و جستجو و مرتب سازی
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # انتخاب فیلدهای مورد نظر برای فیلترینگ
    filterset_fields = ["category", "author", "status"]
    # انتخاب فیلدهای مورد نظر برای جستجو
    search_fields = ["title", "content"]
    # انتخاب فیلدهای مورد نظر برای مرتب سازی
    ordering_fields = ["title", "category", "published_date"]
    # paginations.py ایجاد امکان صفحه بندی برگرفته از فایل
    pagination_class = CustomPagination

    # def list(self, request):
    #     serialized = self.serialized_class(self.queryset, many=True)
    #     return Response(serialized.data)

    # def retrieve(self, request, pk=None):
    #     post = get_object_or_404(self.queryset, pk=pk)
    #     serialized = self.serialized_class(post)
    #     return Response(serialized.data)

    # def create(self, request):
    #     serialized = self.serialized_class(data=request.data)
    #     serialized.is_valid(raise_exception=True)
    #     serialized.save()
    #     return Response(serialized.data)

    # def update(self, request, pk=None, *args, **kwargs):
    #     return self.update(request, pk=pk, *args, **kwargs)

    # def partial_update(self, request, pk=None):
    #     # kwargs['partial'] = True
    #     # return self.update(request, *args, **kwargs)
    #     pass

    # def destroy(self, request, pk=None):
    #     post = get_object_or_404(Post,pk=pk)
    #     post.delete()
    #     return Response({'detail':'Deleting performed successfully'},status=status.HTTP_204_NO_CONTENT)


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
