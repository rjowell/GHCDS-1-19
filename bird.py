'''
BIRD
-Color.
-Beak Type
-Species
-Wing Size
-Bird's Size
-Is it a carnivorous bird or herbivore
-Can the bird fly
-Can they tweet
-has long legs
'''

class Bird:

  def fly(self):
    print("Up Up and away!")

  def tweet(self):
    print("Tweet Tweet")

  def eatAWorm(self):
    print("Yummy worm")
  
  #COMMENTS
  #fly
  #eat
  #look for food
  #brith chicks
  #call
  
  
  def __init__(self,_color,_species,_wingSize,_isCarnivore,_canFly,_canTweet):
    self.wingSize = _wingSize
    self.color = _color
    self.species = _species
    self.carnivore = _isCarnivore
    self.canFly = _canFly
    self.canTweet = _canTweet

  def eat(self):
    print("Yummy!")