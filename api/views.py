from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def send_email(request):
    # Do something with request.data
    pass

@api_view(['POST'])
def send_email_with_template(request):
    # Do something with request.data
    pass
