from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from src.forms import ExtendedUserCreationForm, UserProfileForm, CostSheetNameForm, EmbroideryForm, FabricForm, \
    ThreadForm, MainLabelForm, PolyBagForm, CMTForm
from src.models import Embroidery, Fabric, CostSheetName, Thread, MainLabel, PolyBag, CMT
from django.utils.timezone import datetime


class Index(TemplateView):
    template_name = 'index.html'


class PageNotFound(TemplateView):
    template_name = 'include/404.html'


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        pass1 = request.POST.get('password1')

        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.warning(request,
                             'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def userRegistration(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        userProfileForm = UserProfileForm(request.POST)
        if form.is_valid() and userProfileForm.is_valid():
            user = form.save()
            user_profile = userProfileForm.save(commit=False)
            user_profile.holder = user
            user_profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = ExtendedUserCreationForm()
        userProfileForm = UserProfileForm()
    return render(request, 'registration/userRegistration.html', {'form': form, 'userProfileForm': userProfileForm})

#
# @login_required
# def sheetFirst(request):
#     if request.method == 'POST':
#         formCost = CostSheetNameForm(request.POST, request.FILES)
#         if formCost.is_valid():
#             instance = formCost.save(commit=False)
#             instance.holder = request.user
#             instance.save()
#             costSheetName = formCost.cleaned_data.get('costSheetName')
#             messages.success(request, f'{costSheetName} cost sheet created.')
#             return redirect('costSheet')
#     else:
#         formCost = CostSheetNameForm()
#
#     if request.method == 'POST':
#         form_embroidery = EmbroideryForm(request.POST, request.FILES)
#         if form_embroidery.is_valid():
#             instance = form_embroidery.save(commit=False)
#             instance.holder = request.user
#             instance.save()
#             embroideryDes = form_embroidery.cleaned_data.get('embroideryDes')
#             messages.success(request, f'{embroideryDes} Embroidery is  created.')
#             return redirect('costSheet')
#     else:
#         form_embroidery = EmbroideryForm()
#
#     if request.method == 'POST':
#         form_fabric = FabricForm(request.POST, request.FILES)
#         if form_fabric.is_valid():
#             instance = form_fabric.save(commit=False)
#             instance.holder = request.user
#             instance.save()
#             fabricData = form_fabric.cleaned_data.get('fabricName')
#             messages.success(request, f'{fabricData} fabric data is created.')
#             return redirect('costSheet')
#     else:
#         form_fabric = FabricForm()
#
#     return render(request, 'costSheet.html', {'form': formCost,
#                                               'form_embroidery': form_embroidery,
#                                               'form_fabric': form_fabric})

@login_required
def sheetFirst(request):
    if request.method == 'POST':
        formCost = CostSheetNameForm(request.POST, request.FILES)
        if formCost.is_valid():
            instance = formCost.save(commit=False)
            instance.holder = request.user
            instance.save()
            costSheetName = formCost.cleaned_data.get('costSheetName')
            messages.success(request, f'{costSheetName} cost sheet created.')
            return redirect('costSheet')
    else:
        formCost = CostSheetNameForm()

    if request.method == 'POST':
        form_embroidery = EmbroideryForm(request.POST, request.FILES)
        if form_embroidery.is_valid():
            instance = form_embroidery.save(commit=False)
            instance.holder = request.user
            instance.save()
            embroideryDes = form_embroidery.cleaned_data.get('embroideryDes')
            messages.success(request, f'{embroideryDes} Embroidery is  created.')
            return redirect('costSheet')
    else:
        form_embroidery = EmbroideryForm()

    if request.method == 'POST':
        form_fabric = FabricForm(request.POST, request.FILES)
        if form_fabric.is_valid():
            instance = form_fabric.save(commit=False)
            instance.holder = request.user
            instance.save()
            data = form_fabric.cleaned_data.get('fabricName')
            messages.success(request, f'{data} fabric data is created.')
            return redirect('costSheet')
    else:
        form_fabric = FabricForm()

    if request.method == 'POST':
        form_thread = ThreadForm(request.POST, request.FILES)
        if form_thread.is_valid():
            instance = form_thread.save(commit=False)
            instance.holder = request.user
            instance.save()
            data = form_thread.cleaned_data.get('threadType')
            messages.success(request, f'{data} thread data is created.')
            return redirect('costSheet')
    else:
        form_thread = ThreadForm()

    if request.method == 'POST':
        form_label = MainLabelForm(request.POST, request.FILES)
        if form_label.is_valid():
            instance = form_label.save(commit=False)
            instance.holder = request.user
            instance.save()
            data = form_label.cleaned_data.get('labelType')
            messages.success(request, f'{data} data is created.')
            return redirect('costSheet')
    else:
        form_label = MainLabelForm()

    if request.method == 'POST':
        form_polybag = PolyBagForm(request.POST, request.FILES)
        if form_polybag.is_valid():
            instance = form_polybag.save(commit=False)
            instance.holder = request.user
            instance.save()
            data = form_polybag.cleaned_data.get('polyBagType')
            messages.success(request, f'{data} polyBagType data is created.')
            return redirect('costSheet')
    else:
        form_polybag = PolyBagForm()

    if request.method == 'POST':
        form_cmt = CMTForm(request.POST, request.FILES)
        if form_cmt.is_valid():
            instance = form_cmt.save(commit=False)
            instance.holder = request.user
            instance.save()
            data = form_cmt.cleaned_data.get('cmtCost')
            messages.success(request, f'{data} data is created.')
            return redirect('costSheet')
    else:
        form_cmt = CMTForm()

    return render(request, 'costSheet.html', {'form': formCost,
                                              'form_embroidery': form_embroidery,
                                              'form_fabric': form_fabric,
                                              'form_thread': form_thread,
                                              'form_polybag': form_polybag,
                                              'form_label': form_label,
                                              'form_cmt': form_cmt})


@login_required
def getData(request):
    costSheet = CostSheetName.objects.filter(holder=request.user)
    embroideryData = Embroidery.objects.filter(holder=request.user)
    fabricData = Fabric.objects.filter(holder=request.user)
    threadData = Thread.objects.filter(holder=request.user)
    mainData = MainLabel.objects.filter(holder=request.user)
    polyBagData = PolyBag.objects.filter(holder=request.user)
    cmtData = CMT.objects.filter(holder=request.user)
    return render(request, 'viewCostSheet.html', {'costSheet': costSheet,
                                                  'now': datetime.now(),
                                                  'costSheetq': embroideryData,
                                                  'fabricData': fabricData,
                                                  'threadData': threadData,
                                                  'mainData': mainData,
                                                  'polyBagData': polyBagData,
                                                  'cmtData': cmtData})


@login_required
def finalSheet(request, cid):
    cid = int(cid)
    costSheet = CostSheetName.objects.filter(holder=request.user)
    embroideryData = Embroidery.objects.filter(holder=request.user, related=cid)
    fabricData = Fabric.objects.filter(holder=request.user, related=cid)
    threadData = Thread.objects.filter(holder=request.user, related=cid)
    mainData = MainLabel.objects.filter(holder=request.user, related=cid)
    polyBagData = PolyBag.objects.filter(holder=request.user, related=cid)
    cmtData = CMT.objects.filter(holder=request.user, related=cid)
    return render(request, 'finalCostSheet.html', {'costSheet': costSheet,
                                                   'now': datetime.now(),
                                                   'embroideryData': embroideryData,
                                                   'fabricData': fabricData,
                                                   'threadData': threadData,
                                                   'mainData': mainData,
                                                   'polyBagData': polyBagData,
                                                   'cmtData': cmtData
                                                   })
