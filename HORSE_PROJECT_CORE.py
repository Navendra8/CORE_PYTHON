

class Animal(object):
    """Model the behaviour of a generic animal."""
    def __init__(self, name):
        self.name = name
        self.is_sleeping = False

    def draw_picture(self):
        return "<no picture>"

    @property
    def sound(self):
        return "grunt"

    @property
    def sleep(self):
        return self.is_sleeping

    @sleep.setter
    def sleep(self, status):
        self.is_sleeping = status


class Dog(Animal):
    """Model the behaviour of a dog."""
    def __init__(self, name):
        super().__init__(name)

    @property
    def sound(self):
        return "woof"
    
    def draw_picture(self): 
        """To Draw a Picture of Animal Kind"""
        picture = """
                 /~~~~~~~~\                            _
    ##\__/ @)      ~~~~~~~~\                     \ \ ) )
    |              /~~\~~~~~                ((    |  \
     \    /           |                          /   |
      (~~~   /         \____________/~~~~~~~~~~~~   /
       ~~~~|~                                     /
           :                                      |
            \                                     |
            |                               /      \
             \  \_         :         \     /~~~\    |
             /   :~~~~~|   :~~~~~~~~~~|   :     :   :
            /    :    /    :         /    :    /    :
        (~~~     )(~~~     )     (~~~     )(~~~     )
         ~~~~~~~~  ~~~~~~~~       ~~~~~~~~  ~~~~~~~~
        """
        return picture

    def __str__(self):
        return "Dog named " + self.name

class Cat(Animal): 
    """Model the Behaviour of Cat"""
    def __init__(self,name):
        super().__init__(name)
    def draw_picture(self): 
        picture = """
         ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
        """
        return picture

    @property
    def sound(self):
        return "meow"
    
    @property
    def anger_noise(self):
        return "hiss"
    
    
    def __str__(self):
        return "Cat named "+ self.name
    
    
class Horse(Animal):
    """Model the behaviour of the Horse """
    def __init__(self,name):
        super().__init__(name)
        
    def draw_pic(self):
        picture="""
         ,--,
  _ ___/ /\|
 ;( )__, )
; //   '--;
  \     |
   ^    ^
        
         """
        return picture
    
    @property
    def sound (self):
        return "neigh"
    @property
    def anger_sound(self):
        return "binny"
    
    def __str__(self):
        return "Horse name "+ self.name

if __name__ == "__main__":
    # testing the classes

    a = Animal("Fluffy")
    print(a)
    print(a.sleep)
    a.sleep = True
    print(a.sleep)
    
    
    ruff = Dog("Ruff")
    print(ruff)
    # Showing the override of the sound property
    print(ruff.sound)
    print(a.sound)
    # Showing the picture of Dog 
    print(ruff.draw_picture())

    # Describing a Cat 
    kitty = Cat("Kitty")
    print(kitty)
    print("Sound of kitty is ",kitty.sound)
    print("Picture of kitty is ")
    print(kitty.draw_picture())
    print("Anger Noise of kitty is ",kitty.anger_noise)
    print("*"*70)
    h=Horse("Hey")
    print(h)
    print("Sound of horse is ",h.sound)
    print("Picture of  is ")
    print(h.draw_pic())
    print(h.anger_sound)
    print(h.sleep)
    print(h.sound)
    print(h.setter)

