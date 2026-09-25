from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer


def drink_list(request):
    #get all the drinks 
    #serialise them
    #return json

    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    # return JsonResponse(serializer.data, safe=False)
    # The above returns a list instead of an object and hence the need for the safe = false tag requirment; [{"id": 1, "name": "Grape Soda", "description": "Very Grapey"}, {"id": 2, "name": "Orange Soda", "description": "Very Orangey"}]

    #incase you want an object returned instead of list, do below:
    return JsonResponse({"drinks": serializer.data})
    # Here's what it returns: {"drinks": [{"id": 1, "name": "Grape Soda", "description": "Very Grapey"}, {"id": 2, "name": "Orange Soda", "description": "Very Orangey"}]}
