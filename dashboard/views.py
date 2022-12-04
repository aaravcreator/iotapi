from django.shortcuts import render,HttpResponse,redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .serializers import UserSerializer,SensorSerializer,LedSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
import random
from .forms import UserCreationForm
from .models import Sensor,Led
# Create your views here.
@login_required(login_url='dashboard:user-login')
def index(request):
    led,created = Led.objects.get_or_create(user=request.user)
    
    # return HttpResponse("THIS IS DEFAULT INDEX")
    sensor_readings = Sensor.objects.filter(user=request.user).order_by('-id')[:10]
    last_sensor_reading = sensor_readings.first()
    return render(request,'dashboard/homepage.html',{'sensor_readings':sensor_readings,'last_sensor_reading':last_sensor_reading,'led':led})





def changeLedStatus(request):
    led  = Led.objects.filter(user= request.user).first()
    led.status =  not led.status
    led.save()
    return redirect('dashboard:index')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard:index')
        else:
            messages.info(request,"Username or Password Incorrect")
 
    context ={}
    return render(request,'dashboard/login.html',context)

@login_required(login_url='dashboard:user-login')
def logoutPage(request):
    logout(request)
    messages.info(request,"Logout Successfully")
    return redirect('dashboard:user-login')






class LedStatus(APIView):
    '''Provides Led Status'''
    permission_classes = [IsAuthenticated]
    def get(self,request):
        queryset = Led.objects.get(user=request.user)
        serialized_data = LedSerializer(queryset,many=False)
        return Response(serialized_data.data)


class TestView(APIView):
    ''' This is test view publicly available not authentication required'''
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        message = {
            'message':"This is a random message {}".format(str(random.randint(25,50)))
        }
        return Response(message)





class SensorReading(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()

    def get_queryset(self):
        user =self.request.user
        return Sensor.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # queryset = Sensor.objects.filter(user = request.user)
    # def post(self,request):
    #     sensor = SensorSerializer(data = request.data)
    #     return Response({'ok':"ok"})
# class UserView(ListAPIView):

#     serializer_class = UserSerializer
#     queryset= User.objects.all()



from rest_framework.authtoken.models import Token



@login_required(login_url='dashboard:user-login')

def get_token(request):

    token,created = Token.objects.get_or_create(user=request.user)

    my_token = str(token)
    context = {
        'token': my_token
    }

    return render(request,'dashboard/token.html',context)



def register_user(request):
    user_form = UserCreationForm()
    if request.method == 'POST':
        user_form =UserCreationForm(request.POST or None)
        if user_form.is_valid():
            c_user = user_form.save()
            messages.success(request,"Registered Successfully")
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            # print(username,password)
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard:index')
            return redirect('dashboard:index')
    context = {
        'user_form':user_form,
    }

    return render(request,'dashboard/register.html',context)