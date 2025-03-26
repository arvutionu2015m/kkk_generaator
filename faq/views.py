from .models import FAQ
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FAQGenerateForm
from .utils import generate_faqs
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automaatne sisselogimine
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def admin_review_faqs(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_faqs')
        FAQs = FAQ.objects.filter(id__in=selected_ids)
        count = FAQs.update(approved=True)
        messages.success(request, f"{count} KKK(d) kinnitatud.")
        return redirect('admin_review_faqs')

    faqs = FAQ.objects.filter(approved=False).order_by('-created_at')
    return render(request, 'admin_review_faqs.html', {'faqs': faqs})


@user_passes_test(lambda u: u.is_superuser)
def approve_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    faq.approved = True
    faq.save()
    messages.success(request, f"KKK kinnitatud: {faq.question[:50]}")
    return redirect('admin_review_faqs')

@user_passes_test(lambda u: u.is_superuser)
def delete_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    faq.delete()
    messages.warning(request, "KKK kustutatud.")
    return redirect('admin_review_faqs')

def generate_faq_view(request):
    if request.method == 'POST':
        form = FAQGenerateForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            generated_faqs = generate_faqs(description)
            for q, a in generated_faqs:
                FAQ.objects.create(question=q, answer=a, approved=False)
            messages.success(request, f"{len(generated_faqs)} KKK elementi lisatud kinnitamata kujul.")
            return redirect('home')
    else:
        form = FAQGenerateForm()
    return render(request, 'generate_faq.html', {'form': form})


def home(request):
    faqs = FAQ.objects.filter(approved=True)
    return render(request, 'home.html', {'faqs': faqs})
