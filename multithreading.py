import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"Hai finito di portare a spasso il {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("Hai portato fuori la spazzatura")

def get_email():
    time.sleep(4)
    print("Hai ricevuto l'email")

chore1 = threading.Thread(target = walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target = take_out_trash)
chore2.start()

chore3 = threading.Thread(target = get_email)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("Tutte le task sono state completate")