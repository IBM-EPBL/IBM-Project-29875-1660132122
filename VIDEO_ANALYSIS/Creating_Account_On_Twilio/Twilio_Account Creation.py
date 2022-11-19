from twilio.rest import Client 
 
account_sid = 'ACd25e6a3d1138d64458d6158045c69e95' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG40d6c62ace254fb354735d59dfe62cf1', 
                              body='Fire Has been Detected Successfully....Be Alert ',      
                              to='+916379808180' 
                          ) 
 
print(message.sid)