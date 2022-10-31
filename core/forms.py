from django import forms

class contatoForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    assunto = forms.CharField(label='assunto', max_length=150)
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())
