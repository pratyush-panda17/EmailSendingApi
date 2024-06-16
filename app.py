from flask import Flask,request
import smtplib
from validate_email import validate_email

email = "joeypractice17@gmail.com"
password ="xkna egiu zzoa cfih"


app = Flask(__name__) #creating the app
 
@app.route("/sendemail",methods=["POST"]) #creating new endpoint which only take post requests
def sendEmail():
    rec_email = request.args.get('reciever_email') #Parsing all user inputs
    subject = request.args.get('subject')
    body = request.args.get("body_text")

    if subject == None: #If no subject parameter is present 
        subject=""      #intializing subject to empty string
        

    if rec_email==None or body==None or email=="" or body=="": #Checking if user sent reciever email and body text
        return {"code":422,
                "message":"Please send reciever_email and body_text parameters"}

    return sendAnEmail(rec_email,subject,body) #Function that will send the email and 
                                               #return appropriate response code

def sendAnEmail(rec_email,subject,body):
    is_valid = validate_email(rec_email,verify=True) #Checking if user email is valid
    if is_valid:
        connection  = smtplib.SMTP("smtp.gmail.com") #Creating an smtp connection
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs=rec_email,
                            msg = f"Subject:{subject}\n\n {body}")
        connection.close() #Closing connection
        return {"code":201,
                "message":"Email sent successfully!"} #Ensuring user knows email was sent
    
    return {"code":404, #Error Code sent in case user has not given a valid email
            "message":"The email address does not exist"}



 


