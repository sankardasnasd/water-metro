from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    username=request.POST['username']
    password=request.POST['password']

    var=Login.objects.filter(username=username,password=password)
    if var.exists():
        var2 = Login.objects.get(username=username, password=password)
        if var2.usertype=='admin':
            return JsonResponse({'status': 'ok', 'lid': str(var2.id), 'type': var2.usertype})
        elif var2.usertype=='user':
            return JsonResponse({'status': 'ok', 'lid': str(var2.id), 'type': var2.usertype})

        else:
            return JsonResponse({'status': 'not ok'})
    else:
        return JsonResponse({'status': 'not ok'})

def view_book_tickets(request):
    var=Booking.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,
                  'BOAT':i.SCHEDULE.BOAT.boatname,
                  'USER':i.USER.fname,
                  'date':i.date,
                  'time':i.time,'amount':i.amount,
                  'status':i.status,
                  'totalticket':i.totalticket})
    return JsonResponse({'status':'ok','data':l})


def view_compliants(request):
    # var2=Student.objects.get(LOGIN=var)
    var=Complaint.objects.all()
    l =[]
    for i in var:
        l.append({'id':i.id,'date':i.date,'reply':i.reply,'status':i.status,'USER':i.USER.fname,  'title':i.title,
                  'description':i.description,})
    return JsonResponse({'status': "ok", 'data':l})


def sent_reply(request):
    reply=request.POST['reply']
    rid=request.POST['rid']
    var=Complaint.objects.get(id=rid)
    # var.USER=User.objects.
    var.status='Replied'
    var.reply=reply
    var.save()
    return JsonResponse({'status':'ok'})



def add_service(request):


    BOAT=request.POST['BOAT_id']
    fromplace=request.POST['fromplace']
    time=request.POST['time']
    destination=request.POST['destination']
    capacity=request.POST['capacity']
    amount=request.POST['amount']

    
    var=Metro_Service()
    var.BOAT=Boat.objects.get(id=BOAT)
    var.time=time
    var.destination=destination
    var.capacity=capacity
    var.amount=amount
    var.fromplace=fromplace
    var.save()
    return JsonResponse({'status':'ok'})



def admin_changepassword(request):
    lid = request.POST['lid']
    old = request.POST['old']
    newpass = request.POST['new']
    confirm = request.POST['confirm']

    var = Login.objects.filter(id=lid, password=old)
    if var.exists():
        if newpass == confirm:
            var2 = Login.objects.filter(id=lid).update(password=confirm)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'Not ok'})
    else:
        return JsonResponse({'status': 'NoT Ok'})



def add_station(request):
    station_name=request.POST['station_name']
    var=Metro_Station()
    var.station_name=station_name
    var.save()
    return JsonResponse({'status': 'ok'})


def view_station(request):
    var=Metro_Station.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'station_name':i.station_name})
    return JsonResponse({'status': 'ok','data':l})


def delete_station(request):
    sid=request.POST['sid']
    var=Metro_Station.objects.get(id=sid)
    var.delete()
    return JsonResponse({'status': 'ok'})


def add_boat(request):
    boatname=request.POST['boatname']
    var=Boat()
    var.boatname=boatname
    var.save()
    return JsonResponse({'status': 'ok'})

def view_boat(request):
    var=Boat.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'boatname':i.boatname})
    return JsonResponse({'status': 'ok','data':l})


def delete_boat(request):
    sid=request.POST['sid']
    var=Boat.objects.get(id=sid)
    var.delete()
    return JsonResponse({'status': 'ok'})


def view_payments(request):
    var=Payment.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'USER':i.BOOKING.USER.fname,'amount':i.amount,'date':i.date,'BOAT':i.BOOKING.SCHEDULE.BOAT.boatname,'status':i.status})
    return JsonResponse({'status': 'ok','data':l})


def add_schedule(request):
    BOAT = request.POST['bid']
    time = request.POST['time']
    date = request.POST['date']
    fromplace =request.POST['fromplace']
    destination = request.POST['destination']
    capacity = request.POST['capacity']
    amount = request.POST['amount']


    var=Schedule()
    var.BOAT=Boat.objects.get(id=BOAT)
    var.time=time
    var.date=date
    var.fromplace=fromplace
    var.destination=destination
    var.capacity=capacity
    var.amount=amount+'/person'
    var.save()
    return JsonResponse({'status': 'ok'})






def view_users(request):
    var=User.objects.all( )
    l=[]

    for i in var:
        l.append({'id': i.id, 'fname': i.fname, 'lname': i.lname, 'contact': i.contact, 'email': i.email,
                  'dob': i.dob, 'place': i.place, 'pin': i.pin, 'post': i.post, 'district': i.district})


    return JsonResponse({'status':'ok','data':l})


def admin_view_services(request):
    sid=request.POST['sid']
    var=Schedule.objects.filter(BOAT_id=sid)
    l=[]
    for i in var:
        l.append({'id':i.id,'time':i.time,
                  'date':i.date,'fromplace':i.fromplace,'destination':i.destination,'capacity':i.capacity,'amount':i.amount})
    return JsonResponse({'status': 'ok','data':l})








# user



def reg(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    contact=request.POST['contact']
    email=request.POST['email']
    dob=request.POST['dob']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    district=request.POST['district']
    password=request.POST['password']
    confirm=request.POST['confirm']

    v=Login.objects.filter(username=email)
    if v.exists():
        return JsonResponse({'status': 'not ok'})

    if password==confirm:
        L = Login()
        L.username = email
        L.password=confirm
        L.usertype='user'
        L.save()


        u=User()
        u.LOGIN=L
        u.fname=fname
        u.lname=lname
        u.contact=contact
        u.email=email
        u.dob=dob
        u.place=place
        u.pin=pin
        u.post=post
        u.district=district
        u.save()
        return JsonResponse({'status':'ok'})



def view_profile(request):
    lid=request.POST['lid']
    var=User.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','fname':var.fname,'lname':var.lname,
                         'contact':var.contact,'email':var.email,'dob':var.dob,
                         'place':var.place,'pin':var.pin,'post':var.post,'district':var.district})



def send_complaint(request):
    lid=request.POST['lid']
    title=request.POST['title']
    description=request.POST['description']

    uid = User.objects.get(LOGIN_id=lid)
    # c_obj.STUDENT = uid

    var=Complaint()
    var.reply='pending'
    var.status='pending'
    var.USER=uid
    var.title=title
    var.description=description
    var.date=datetime.now().date().today()
    var.save()
    return JsonResponse({'status': 'ok'})



def user_view_complaints(request):
    lid=request.POST['lid']
    var=Complaint.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'description':i.description,'title':i.title,'date':i.date,'status':i.status,'reply':i.reply})

    return JsonResponse({'status':'ok','data':l})


def userview_boat(request):
    var=Boat.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'boatname':i.boatname})
    return JsonResponse({'status': 'ok','data':l})


def view_services(request):
    sid=request.POST['sid']
    var=Schedule.objects.filter(BOAT_id=sid)
    l=[]
    for i in var:
        l.append({'id':i.id,'time':i.time,
                  'date':i.date,'fromplace':i.fromplace,'destination':i.destination,'capacity':i.capacity,'amount':i.amount})
    return JsonResponse({'status': 'ok','data':l})






def booking(request):
    sid=request.POST['sid']
    lid=request.POST['lid']
    # amount=request.POST['amount_']
    totalticket=request.POST['totalticket']


    sar=Schedule.objects.filter(id=sid)





    var=Booking()
    var.SCHEDULE=Schedule.objects.get(id=sid)
    var.USER=User.objects.get(LOGIN_id=lid)
    var.totalticket=totalticket
    # var.amount=str(amount)*totalticket
    var.date=datetime.now().today().date()
    var.time=datetime.now().today().time()
    var.save()
    return JsonResponse({'status': 'ok'})


def view_payment(request):
    lid=request.POST['lid']
    var=Payment.objects.filter(BOOKING__USER__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'status':i.status,'amount':i.amount,'date':i.date,
                  'SCHEDULE':i.BOOKING.SCHEDULE.BOAT.boatname,
                  'totalticket':i.BOOKING.totalticket})
    return JsonResponse({'status': 'ok','data':l})




def and_userpayment(request):
    accountno = request.POST["accountno"]
    pin = request.POST["pin"]
    ifsc = request.POST["ifsc"]
    amount = request.POST["amount"]
    ulid = request.POST["lid"]
    bid = request.POST["bid"]

    if Bank.objects.filter(account_no=accountno,pin=pin,IFSC=ifsc).exists():
        s=Bank.objects.get(account_no=accountno,pin=pin,IFSC=ifsc)
        if float(s.balance)<float(amount):
            return JsonResponse({"status":"balno"})
        else:
            w = Payment()
            w.accountno = accountno
            w.ifsc = ifsc
            w.amount=int(float(amount))
            w.USER = User.objects.get(LOGIN_id=ulid)
            w.BOOKING = Booking.objects.get(id=bid)
            from datetime import datetime
            date = datetime.now().strftime("%Y-%m-%d")
            w.date = date
            w.status='Paid'
            w.save()
            return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({"status":"acno"})





def view_tickets(request):
    lid=request.POST['lid']
    var=Booking.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'SCHEDULE':i.SCHEDULE.BOAT.boatname,
                  'totalticket':i.totalticket,'amount':i.amount,'date':i.date,'time':i.time,'status':i.status})

    return JsonResponse({'status': 'ok', 'data': l})






def edit_userprofile(request):



    lid = request.POST['lid']
    fname = request.POST['fname']
    lname = request.POST['lname']
    contact = request.POST['contact']
    email = request.POST['email']
    dob = request.POST['dob']
    place = request.POST['place']
    pin = request.POST['pin']
    post = request.POST['post']
    district = request.POST['district']

    result = User.objects.get(LOGIN_id=lid)
    result.fname = fname
    result.lname = lname
    result.dob = dob
    result.pin = pin
    result.district = district
    result.email = email
    result.contact=contact
    result.place=place
    result.post=post


    result.save()
    return JsonResponse({'status': "ok"})


def user_changepassword(request):
    lid = request.POST['lid']
    old = request.POST['old']
    newpass = request.POST['new']
    confirm = request.POST['confirm']

    var = Login.objects.filter(id=lid, password=old)
    if var.exists():
        if newpass == confirm:
            var2 = Login.objects.filter(id=lid).update(password=confirm)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'Not ok'})
    else:
        return JsonResponse({'status': 'NoT Ok'})
