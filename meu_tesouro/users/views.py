from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .models import User
from django.contrib import auth
from django.core.mail import EmailMessage
from django.contrib.auth.forms import PasswordChangeForm

#Trata do tráfego de urls da aplicação web


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Ative sua conta no Meu Tesouro!'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            activation_link = "{0}/?uid={1}&token{2}".format(current_site, uid, token)
            #message = "Olá {0},\n {1}".format(user.first_name, activation_link)
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            messages.warning(request, f'Um e-mail foi enviado para {to_email} confirmar o cadastro!')
            return HttpResponse('Por favor, confirme seu endereço de e-mail para completar o cadastro.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Seu perfil foi atualizado!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)


def activate(request, uidb64, token):
    try:
        # ERRO AQUI #
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        # FIM ERRO #
        print(str(user.first_name))
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        #user = None
        print('Erro!')
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        #form = PasswordChangeForm(request.user)
        return HttpResponse('Obrigado por confirmar seu e-mail ! Agora você pode efetuar o logon.')
    else:
        return HttpResponse('Link de confirmação inválido!')


