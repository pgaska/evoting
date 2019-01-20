from django import forms

class AddDigits(forms.Form):
    def __init__(self, x, *args, **kwargs):
        super(AddDigits, self).__init__(*args, **kwargs)
        for i in x:
            self.fields['choice%i' % i] = forms.ChoiceField(choices=[('choice0'+str(i), 'choice'+str(i)), ('choice1'+str(i), 'choice'+str(i))], widget=forms.RadioSelect)

class AddVote(forms.Form):
    def __init__(self, x, *args, **kwargs):
        super(AddVote, self).__init__(*args, **kwargs)
        CHOICES=[]
        for i in x:
            CHOICES.append((str(i), 'choice'))
        self.fields['choice'] = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
