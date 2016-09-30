from	django	import	forms
from	.models	import	Post, Comment

# IMPORTAR los modelos antes de crear el formulario

class PostForm(forms.ModelForm):
				class	Meta:
							model = Post
							fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

	
	class Meta:
		model = Comment 
		fields = ('author' , 'text')							