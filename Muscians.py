#GLobals
import random

class Band(object):
    def __init__(self, sounds):
        self.members = {}

    def hire(self):
        new_member = input("Whats the new members name?")
        member_type = input("What does the member play?")
        if member_type == "bass":
            self.members[new_member] = Bassist()
        elif member_type == "guitar":
            self.members[new_member] == Guitarist()
        else:
            member_type == "drums"
            self.members[new_member] == Drummer() 
    
    def fire(self, fired_member):
        del self.members[fired_member]

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        #call the __init__method of the parent class
        super().__init__(["Bang", "Clang", "Crash"])

    def combust(self):
        print("COMBUST")
        
    def count(self):
        for c in range(1,5):
            print(c)
            

        
def main():
  trementina = Band()
  trementina.hire()
  trementina.hire("Ralph")
  trementina.hire()
  trementina.fire("Ralph")
  print (trementina.members)
  acdc.play_solos(6)

# def main()
#def main():
#   results = find_preference()
#    print("\nGreat! Based on your choices, I recommend a cocktail with a:")
#    for drink in make_drink(results):
#        print("    " + drink)    

#if __name__ == "__main__":
#    main()  