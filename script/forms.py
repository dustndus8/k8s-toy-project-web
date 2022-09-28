from django import forms

from script.models import Script


class ScriptForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = ('project_name', 'key_pair_name', 'flavor','worker','image')
        exclude = ('writer', ) # 폼에서 writer 입력 받지 않도록