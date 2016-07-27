#GLobals
import random

class Band(object):
    def __init__(self, sounds):
        self.members {}

    def hire(self):
        new_member = input("Whats the new members name?")
        member_type = input"What does the member play?"
            if member_type == "bass"
                self.members[new_member] = Bassist()
            elif member_type == "guitar"
                self.members[new_member] == Guitarist()
                
        


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
            

        
nigel = Guitarist()
nigel.solo(6)
nigel.tune()

bonham = Drummer()
bonham.count()
bonham.solo(5)
bonham.combust()

eddie = Bassist()
eddie.solo(5)

def main()
    

if __name__ == "__main__":
    main() 