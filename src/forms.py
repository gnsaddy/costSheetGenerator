from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, CostSheetName, Embroidery, Fabric, Thread, MainLabel, PolyBag, CMT


class ExtendedUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter username"
    }))

    email = forms.EmailField(required=True, label="Email", max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'Email Id'
    }))

    first_name = forms.CharField(label="First Name", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'First Name'
    }))

    last_name = forms.CharField(label="Last Name", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'Last Name'
    }))

    password1 = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter password"
    }))
    password2 = forms.CharField(max_length=50, label='Confirm password', widget=forms.PasswordInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Confirm password"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    mobile = forms.CharField(label="Mobile", max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'Mobile Number'
    }))

    class Meta:
        model = UserProfile
        fields = ['mobile', 'userType']


class CostSheetNameForm(forms.ModelForm):
    costSheetName = forms.CharField(label="Cost Sheet Name", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter cost Sheet Name"
    }))

    buyer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter buyer name"
    }))

    styleNum = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter Style number"
    }))

    category = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter category"
    }))

    description = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter description"
    }))

    season = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter season"
    }))

    order_quant = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter order quantity"
    }))

    class Meta:
        model = CostSheetName
        fields = ['costSheetName', 'buyer', 'styleNum', 'category', 'description', 'season', 'order_quant', 'image']


class EmbroideryForm(forms.ModelForm):
    embroideryDes = forms.CharField(label="Embroidery Description", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter Embroidery Description"
    }))

    color = forms.CharField(label="Color", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter color"
    }))

    consumption = forms.CharField(label="Consumption", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter consumption"
    }))

    extraAllowance = forms.CharField(label="Extra Allowance", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter Extra Allowance"
    }))

    rate = forms.CharField(label="Rate", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter rate"
    }))

    remark = forms.CharField(label="Remark", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter remark"
    }))

    totalCost = forms.CharField(label="TotalCost", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter totalCost"
    }))

    supplier = forms.CharField(label="supplier", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter supplier"
    }))

    class Meta:
        model = Embroidery
        fields = ['related', 'embroideryDes', 'color', 'consumption', 'extraAllowance', 'rate', 'remark', 'totalCost',
                  'supplier']


class FabricForm(forms.ModelForm):
    fabricName = forms.CharField(label="Fabric Name", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter Fabric Name"
    }))
    content = forms.CharField(label="Content", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter content"
    }))
    gsm = forms.CharField(label="GSM", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter gsm"
    }))
    yarnCount = forms.CharField(label="Yarn count", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter yarn count"
    }))
    construction = forms.CharField(label="Construction", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter construction"
    }))
    type = forms.CharField(label="Type", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter type"
    }))
    consumption = forms.CharField(label="Consumption", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter consumption"
    }))
    totalWidth = forms.CharField(label="Total Width", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter totalWidth"
    }))
    extraAllowance = forms.CharField(label="Extra Allowance", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter type"
    }))
    rate = forms.CharField(label="Rate", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter rate"
    }))
    totalCost = forms.CharField(label="Total Cost", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter totalCost"
    }))
    importDuty = forms.CharField(label="Import Duty", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter importDuty"
    }))
    remark = forms.CharField(label="Remark", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter remark"
    }))
    supplier = forms.CharField(label="Supplier", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control rounded-pill",
        "placeholder": "Enter supplier"
    }))

    class Meta:
        model = Fabric
        fields = ['related', 'fabricName', 'content', 'gsm', 'yarnCount', 'construction', 'type', 'consumption',
                  'totalWidth',
                  'extraAllowance', 'rate', 'totalCost', 'importDuty', 'remark', 'supplier']


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['related', 'threadType', 'content', 'threadColor', 'tktSize', 'cost_unit', 'consumption', 'extraAllowance', 'importDuty', 'totalCost',  'remark',
                  'supplier']


class MainLabelForm(forms.ModelForm):
    class Meta:
        model = MainLabel
        fields = ['related', 'labelType', 'textType', 'dimension', 'rate', 'extraAllowance', 'totalCost', 'importDuty', 'remark', 'supplier']


class PolyBagForm(forms.ModelForm):
    class Meta:
        model = PolyBag
        fields = ['related', 'polyBagType', 'polyBagMaterial', 'dimension', 'cost_unit', 'extraAllowance', 'totalCost',
                  'importDuty', 'remark', 'supplier']


class CMTForm(forms.ModelForm):
    class Meta:
        model = CMT
        fields = ['related', 'cmtCost', 'packagingCharge', 'factoryOverheadCost', 'testingCost', 'otherCost',
                  'logisticCost', 'factoryMarkup', 'totalInr', 'agentMarkup', 'factoryFOB', 'clientFOB',
                  'constractualCost'
                  ]
