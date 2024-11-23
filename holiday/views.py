from django.shortcuts import render

def holiday_view(request):
    return render(request, 'holiday/holiday_page.html')
