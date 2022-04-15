from django.shortcuts import render
from case.models import Case

# Create your views here.
def case(request):
    cases = Case.objects.all()
    case_count = cases.count()
    context = {
        'cases': cases,
        'case_count': case_count,
    }
    return render(request, 'case/case.html', context)


def case_detail(request, case_slug):
    try:
        single_case = Case.objects.get(slug=case_slug)
    except Exception as e:
        raise e
    context = {
        'single_case': single_case,
    }
    return render(request, 'case/overview.html', context)