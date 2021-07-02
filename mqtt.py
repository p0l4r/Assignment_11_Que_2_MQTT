#Author: Shantanu Kumar Rahut
#Email: shantanurahut@gmail.com
#Date: 01.07.2021

import paho.mqtt.client as mqtt
import time

#the global variable was being reset because of loop_forever() , because of the time constraint I have decided to use txt files


# The callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):  
    print("Connected with result code {0}".format(str(rc)))
    client.subscribe("7015438/UUID")  
    print("subscribed to the topic")
    client.publish("login","7015438")
    print("message published")
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):  
    print("message received " ,str(message.payload.decode("utf-8")))
    mes = str(message.payload.decode("utf-8"))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    if(mes != "CMD1" and mes != "CMD2" and mes != "CMD3" 
       and mes != "CMD4" and mes != "CMD5" 
       and mes != "CMD6" and mes != "CMD7" 
       and mes !="Apple" and mes !="Cat" 
       and mes !="Dog" and mes !="Rat" 
       and mes !="Boy" and mes !="Girl" 
       and mes !="Toy" and mes!="Well done my IoT!"):
        client.subscribe(mes)
        f = open("assignment11.txt", "w")
        f.write(mes)
        f.close()
    else:  
        with open('assignment11.txt', 'r') as file:
            u = file.read().replace('\n', '')
            
        if(mes=="CMD1"): 
            u = u + "/" + "CMD1"
            msgstring = "Apple"
            client.subscribe(u)
            client.publish(u,msgstring)
        elif(mes=="CMD2"):
            u = u + "/" + "CMD2"
            msgstring = "Cat"
            client.subscribe(u)
            client.publish(u,msgstring)
        elif(mes=="CMD3"):
            u = u + "/" + "CMD3"
            msgstring = "Dog"
            client.subscribe(u)
            client.publish(u,msgstring)
        elif(mes=="CMD4"):
            u = u + "/" + "CMD4"
            msgstring = "Rat"
            client.subscribe(u)
            client.publish(u,msgstring)
        elif(mes=="CMD5"):
            u = u + "/" + "CMD5"
            msgstring = "Boy"
            client.subscribe(u)
            client.publish(u,msgstring)
        elif(mes=="CMD6"):
            u = u + "/" + "CMD6"
            msgstring = "Girl"
            client.subscribe(u)
            client.publish(u,msgstring)
        elif(mes=="CMD7"):
            u = u + "/" + "CMD7"
            msgstring = "Toy"
            client.subscribe(u)
            client.publish(u,msgstring)
            
    if(mes=="Well done my IoT!"):
        client.disconnect()
    



def on_log(client, userdata, level, buf):
    print("log: ",buf)

#creating client instance
client = mqtt.Client(
    client_id="shantanukumarrahut_7015438_riffatsharmin_7015660_team_47"
    )
print("client created ......")
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message
client.on_log = on_log # Define callback function for log

#connecting to broker/server
#give the host/server/broker name
hostname = "inet-mqtt-broker.yakshaving.de" 
#give the port number
portnumber = 1883 
#give the username and password for the broker/server/host
client.username_pw_set("student", "i_make_mqtt_cool") 
client.connect(host= hostname ,port= portnumber)
print("client connected to- ",hostname," on port_number:",portnumber)

client.loop_forever()  # Start networking daemon



