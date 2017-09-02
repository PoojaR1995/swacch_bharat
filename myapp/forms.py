from django import forms
from models import UserModel, PostModel, LikeModel, CommentModel

#from the sign up menu of the app
class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields=['email','name','username','password']

#form for the login menu if you are existing user
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

#form the post or feed page
class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=['image', 'caption']

# for posting like on some post
class LikeForm(forms.ModelForm):

    class Meta:
        model = LikeModel
        fields=['post']

#for posting comment on feed page
class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']