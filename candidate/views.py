# from django.shortcuts import render
import json
from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Candidate
from .serializers import CandidateSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_candidate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = CandidateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Candidate created successfully'}, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Method not Allowed. Use POST Request'}, status=404)

def get_candidate_data(request, candidate_id):
    if not Candidate.objects.filter(id = candidate_id).exists():
        return JsonResponse({'error': 'No Candidate with this Id exists'}, status = 404)
    candidate = Candidate.objects.get(id = candidate_id)
    serializer = CandidateSerializer(candidate)
    return JsonResponse(serializer.data)

@csrf_exempt
def update_candidate_status(request, candidate_id):
    if not Candidate.objects.filter(id = candidate_id).exists():
        return JsonResponse({'error': 'No Candidate with this Id exists'}, status = 404)
    candidate = Candidate.objects.get(id = candidate_id)
    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            new_status = data.get('status', None)
            if new_status and new_status.capitalize() in dict(Candidate.STATUS_CHOICES).keys():
                candidate.status = new_status.capitalize()
                candidate.save()
                return JsonResponse({'message': 'Candidate status updated successfully'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid status value'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Method not Allowed. Use PATCH Request'}, status=405)
    
def candidate_list(request):
    queryset = Candidate.objects.all()
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')
    min_age = request.GET.get('min_age')
    max_age = request.GET.get('max_age')
    min_exp = request.GET.get('min_exp')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    print(min_salary, max_salary, min_age, max_age, min_exp)
    if min_salary:
        queryset = queryset.filter(expected_salary__gte=min_salary)
    if max_salary:
        queryset = queryset.filter(expected_salary__lte=max_salary)
    if min_age:
        queryset = queryset.filter(age__gte=min_age)
    if max_age:
        queryset = queryset.filter(age__lte=max_age)
    if min_exp:
        queryset = queryset.filter(years_of_exp__gte=min_exp)
    if email:
        queryset = queryset.filter(email__iexact = email)
    if phone:
        queryset = queryset.filter(phone_number__iexact = phone)
    serializer = CandidateSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False, status = 200)


def name_search(request):
    queryset = Candidate.objects.all()
    name = request.GET.get('name')
    if name:
        name_words = name.lower().split()
        # print(name_words)

        exact_matches = Candidate.objects.filter(name__iexact=name) # Exact match for name should be most relevant

        name_query = Q()
        for word in name_words:
            name_query |= Q(name__icontains=word) # query to check for different users with similar names to the given query
        partial_matches = Candidate.objects.filter(name_query).exclude(name__iexact=name)  # 

        sorted_partial_matches = sorted(partial_matches, key=lambda x: len(set(x.name.lower().split()) & set(name_words)), reverse=True) # sort partial matches according to relevance

        sorted_results = list(exact_matches) + sorted_partial_matches
        serializer = CandidateSerializer(sorted_results, many=True)
        return JsonResponse(serializer.data, safe=False, status = 200)
    else:
        serializer = CandidateSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False, status = 200)
