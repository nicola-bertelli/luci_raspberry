import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
attesa_pulsante=0.05

# DICHIARAZIONE GPIO INTERRUTTORI
int_uno=21
int_due=20
int_tre=16
int_qua=12

GPIO.setup(int_uno,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(int_due,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(int_tre,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(int_qua,  GPIO.IN, pull_up_down=GPIO.PUD_UP)


# ANALISI E DICHIARAZIONE DELLO STATO INIZIALE DEGLI INTERRUTTORI
stato_int_uno=GPIO.input(int_uno)
stato_int_due=GPIO.input(int_due)
stato_int_tre=GPIO.input(int_tre)
stato_int_qua=GPIO.input(int_qua)

# DICHIARAZIONE GPIO LUCI
luce_uno=26
luce_due=19
luce_tre=13
luce_qua=6

GPIO.setup(luce_uno, GPIO.OUT)
GPIO.setup(luce_due, GPIO.OUT)
GPIO.setup(luce_tre, GPIO.OUT)
GPIO.setup(luce_qua, GPIO.OUT)

# SPENGO TUTTE LE LUCI ALL'AVVIO
GPIO.output(luce_uno, 0)
GPIO.output(luce_due, 0)
GPIO.output(luce_tre, 0)
GPIO.output(luce_qua, 0)

# AZZERO ANCHE LO STATO DEGLI INTERRUTTORI DI HOME ASSISTANT
client = mqtt.Client()
client.connect("192.168.1.11", 1883, 60)
client.publish("prova/state/salotto/luce_uno", 0)
client.publish("prova/state/salotto/luce_due", 0)
client.publish("prova/state/salotto/luce_tre", 0)
client.publish("prova/state/salotto/luce_qua", 0)


print " AVVIO GESTIONE LUCI SALOTTO "

try:
    client = mqtt.Client()
    client.connect("192.168.1.11", 1883, 60)
    topic = "notify/notifica_nicola"
    client.publish(topic, "gestione luci salotto avviato")
except:
    print "errore MQTT"

while True:

    # CONTROLLO INTERRUTTORE 1
    if GPIO.input(int_uno) != stato_int_uno:
        stato_rele_uno=GPIO.input(luce_uno)
        stato_int_uno=GPIO.input(int_uno)
        if stato_rele_uno==1: stato_rele_uno=0
        elif stato_rele_uno==0: stato_rele_uno=1

        GPIO.output(luce_uno, stato_rele_uno)
        client = mqtt.Client()
        try:
            client.connect("192.168.1.11", 1883, 60)
            topic = "prova/state/salotto/luce_uno"
            client.publish(topic, stato_rele_uno)
            print "invio " + str(stato_rele_uno) + " al topic " + topic
        except:
            print "errore MQTT"
        print " luce uno " + str(stato_rele_uno)

    # CONTROLLO INTERRUTTORE 2
    if GPIO.input(int_due) != stato_int_due:
        stato_rele_due=GPIO.input(luce_due)
        stato_int_due=GPIO.input(int_due)
        if stato_rele_due==1: stato_rele_due=0
        elif stato_rele_due==0: stato_rele_due=1

        GPIO.output(luce_due, stato_rele_due)
        client = mqtt.Client()
        try:
            client.connect("192.168.1.11", 1883, 60)
            topic = "prova/state/salotto/luce_due"
            client.publish(topic, stato_rele_due)
            print "invio " + str(stato_rele_due) + " al topic " + topic
        except:
            print "errore MQTT"
        print " luce due " + str(stato_rele_due)

    # CONTROLLO INTERRUTTORE 3
    if GPIO.input(int_tre) != stato_int_tre:
        stato_rele_tre=GPIO.input(luce_tre)
        stato_int_tre=GPIO.input(int_tre)
        if stato_rele_tre==1: stato_rele_tre=0
        elif stato_rele_tre==0: stato_rele_tre=1

        GPIO.output(luce_tre, stato_rele_tre)
        client = mqtt.Client()
        try:
            client.connect("192.168.1.11", 1883, 60)
            topic = "prova/state/salotto/luce_tre"
            client.publish(topic, stato_rele_tre)
            print "invio " + str(stato_rele_tre) + " al topic " + topic
        except:
            print "errore MQTT"
        print " luce tre " + str(stato_rele_tre)

    # CONTROLLO INTERRUTTORE 4
    if GPIO.input(int_qua) != stato_int_qua:
        stato_rele_qua=GPIO.input(luce_qua)
        stato_int_qua=GPIO.input(int_qua)
        if stato_rele_qua==1: stato_rele_qua=0
        elif stato_rele_qua==0: stato_rele_qua=1

        GPIO.output(luce_qua, stato_rele_qua)
        client = mqtt.Client()
        try:
            client.connect("192.168.1.11", 1883, 60)
            topic = "prova/state/salotto/luce_qua"
            client.publish(topic, stato_rele_qua)
            print "invio " + str(stato_rele_qua) + " al topic " + topic
        except:
            print "errore MQTT"
        print " luce quattro " + str(stato_rele_qua)


    time.sleep(attesa_pulsante)
