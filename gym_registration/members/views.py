# members/views.py
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import MemberRegistrationForm, MemberEditForm
from .models import Member

@login_required
def register_member(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberRegistrationForm()
    return render(request, 'members/register_member.html', {'form': form})

@login_required
def member_list(request):
    members = Member.objects.all()

    # Calculate remaining days dynamically
    for member in members:
        member.remaining_days_value = member.remaining_days()

    # Sorting logic
    sort_by = request.GET.get('sort_by', 'name')  # Default sorting is by name
    sort_order = request.GET.get('sort_order', 'asc')  # Default order is ascending

    if sort_by == 'remaining_days':
        members = sorted(members, key=lambda x: x.remaining_days(), reverse=(sort_order == 'desc'))
    else:
        if sort_order == 'desc':
            sort_by = f"-{sort_by}"
        members = members.order_by(sort_by)

    context = {
        'members': members,
        'sort_by': request.GET.get('sort_by', 'name'),
        'sort_order': request.GET.get('sort_order', 'asc'),
    }
    return render(request, 'members/member_list.html', context)

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('member_list')
    else:
        return redirect('login')


@login_required
def edit_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)  # Fetch the member object
    if request.method == 'POST':
        form = MemberEditForm(request.POST, instance=member)  # Bind form to the member instance
        if form.is_valid():
            form.save()  # Save the updated member details
            return redirect('member_list')  # Redirect back to the member list
    else:
        form = MemberEditForm(instance=member)  # Populate the form with the existing data
    return render(request, 'members/edit_member.html', {'form': form})


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


@login_required
def extend_membership(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.extend_membership(30)  # Extend membership by 30 days
    return redirect('member_list')  # Redirect back to the member list


@login_required
def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.delete()  # Delete the member
    return redirect('member_list')  # Redirect back to the member list