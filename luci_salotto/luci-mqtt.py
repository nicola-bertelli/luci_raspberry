import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

luce_uno=26
luce_due=19
luce_tre=13
luce_qua=6

GPIO.setup(luce_uno, GPIO.OUT)
GPIO.setup(luce_due, GPIO.OUT)
GPIO.setup(luce_tre, GPIO.OUT)
GPIO.setup(luce_qua, GPIO.OUT)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        adesso=time.time()
    	fh=open("/home/pi/luci_salotto/log.txt",'r')
    	leggi=fh.readlines()
    	fh.close()
    	fh=open("/home/pi/luci_salotto/log.txt",'w')
    	fh.writelines(leggi)
    	ora_log=(time.strftime("%H:%M:%S %d/%m/%Y"))
    	fh.write('MQTT disconnesso ' + ora_log + ' ' + '\n')
        fh.close()
        print " disconnesso dal server"



def on_connect(client, userdata, flags, rc):
    #i = 0
    print "connesso"
    client.subscribe("prova/command/salotto/luce_uno")
    client.subscribe("prova/command/salotto/luce_due")
    client.subscribe("prova/command/salotto/luce_tre")
    client.subscribe("prova/command/salotto/luce_qua")


def on_message(client, userdata, msg):
      messaggio=str(msg.payload)
      print messaggio
      topic=str(msg.topic)
      print topic

      if topic=="prova/command/salotto/luce_uno":
         if messaggio=="1" or messaggio=="0":
             GPIO.output(luce_uno, int(messaggio))
             client.publish("prova/state/salotto/luce_uno", messaggio)
             print "luce uno " + messaggio

      if topic=="prova/command/salotto/luce_due":
         if messaggio=="1" or messaggio=="0":
             GPIO.output(luce_due, int(messaggio))
             client.publish("prova/state/salotto/luce_due", messaggio)
             print "luce due " + messaggio

      if topic=="prova/command/salotto/luce_tre":
         if messaggio=="1" or messaggio=="0":
             GPIO.output(luce_tre, int(messaggio))
             client.publish("prova/state/salotto/luce_tre", messaggio)
             print "luce tre " + messaggio

      if topic=="prova/command/salotto/luce_qua":
         if messaggio=="1" or messaggio=="0":
             GPIO.output(luce_qua, int(messaggio))
             client.publish("prova/state/salotto/luce_qua", messaggio)
             print "luce quattro " + messaggio



GPIO.output(luce_uno, 0)
GPIO.output(luce_due, 0)
GPIO.output(luce_tre, 0)
GPIO.output(luce_qua, 0)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
try:
    time.sleep(0.2)
    client.connect("192.168.1.11", 1883, 60)
except:
    print "connessione errata"

client.loop_forever()
