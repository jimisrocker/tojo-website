from flask import render_template,request,flash
from flask import Blueprint
from .models import Business,Message


views=Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        if request.form.get('cf-phone'):
            #register business code
            phone=request.form.get('cf-phone')
            name=request.form.get('cf-name')
            email=request.form.get('cf-email')
            message=request.form.get('cf-message')
        else:
            #send message code
            name=request.form.get('cf-name')
            email=request.form.get('cf-email')
            message=request.form.get('cf-message')

        if len(message)<10:
            flash('Please add some details in your message, at least 100 characters', category='error')
        elif len(name)<4:
            flash('Name must be greater than 3 characters', category='error')
        else:
            if request.form.get('cf-phone'):
                new_business= Business(name=name, email=email,phone=phone,message=message).save()
                flash('Business registered, we will contact you soon!', category='success')
                print('Business registered')
            else:
                flash('Message sent, we will contact you soon!', category='success')
                new_message= Message(name=name, email=email,message=message).save()
                print('Message sent')

    return render_template("index.html")