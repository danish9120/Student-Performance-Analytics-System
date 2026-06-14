from django.shortcuts import render
from .models import Result


def home(request):

    results = Result.objects.all()

    roll_no = request.GET.get('roll_no')

    if roll_no:
        results = results.filter(student__roll_no=roll_no)

    total_students = results.count()

    context = {
        'results': results,
        'total_students': total_students
    }

    return render(request, 'home.html', context)