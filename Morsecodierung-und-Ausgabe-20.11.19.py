# Jonas Ertle,20.11.2019
import RPi.GPIO as GPIO
from signal import pause
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Lampe = 14
GPIO.setup(Lampe,GPIO.OUT)
GPIO.output(Lampe,GPIO.LOW)

Ende = 1
Satz = 1
ts = 0.3
tl = 0.7
tz = 1

#Dictionary enthält die Morsecodes je Zeichen
MorseAlphabet = {
    #Buchstaben
    "A":".-", "B":"-...", "C":"-.-.",
    "D":"-..", "E":".", "F":"..-.", "G":"--.",
    "H":"....", "I":"..", "J":".---", "K":"-.-", 
    "L":".-..", "M":"--", "N":"-.", "O":"---",
    "P":".--.", "Q":"--.-", "R":".-.",
    "S":"...", "T":"-", "U":"..-", "V":"...-",
    "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..",
    "Ä":".-.-","Ö":"---.","Ü":"..--","ß":"...--..",
    #Zahlen
    "1":".----", "2":"..---", "3":"...--", "4":"....-",
    "5":".....", "6":"-....", "7":"--...", "8":"---..",
    "9":"----.", "0":"-----",
    #Satzzeichen
    ", ":"--..--", ".":".-.-.-", "?":"..--..","#":"#",
    " ":" "
}

def k():
    GPIO.output(Lampe,GPIO.HIGH),time.sleep(ts)
    GPIO.output(Lampe,GPIO.LOW),time.sleep(ts)            
def l():
    GPIO.output(Lampe,GPIO.HIGH),time.sleep(tl)
    GPIO.output(Lampe,GPIO.LOW),time.sleep(ts)    

while Ende == 1:
    try:
        Satz = input("""Bitte Nachricht eingeben und mit Enter bestätigen.
Zeichen "#" um das Programm zu beenden!
Eingabe:""")
        Satz = Satz.upper() 
        for y in range(0,len(Satz)):            
            #holt den richtigen Morsecode aus dem Dictionary
            beeps = MorseAlphabet[Satz[y]]
            if beeps == " ":
                time.sleep(2*tz)
            #iteriert über alle Signale eines Morsecodes
            for x in range(0,len(beeps)):
                if beeps[x] == ".":
                    k()
                elif beeps[x] == "-":
                    l()
                elif beeps[x] == "#":
                    print("Beendet")
                    Ende = 0
                elif beeps[x] == " ":
                    time.sleep(2*tz)
                else:
                    raise Exception("Buchstabe nicht gefunden, bitte erneut starten")
                time.sleep(tz)        
    except KeyboardInterrupt:
        GPIO.cleanup()
GPIO.cleanup()
