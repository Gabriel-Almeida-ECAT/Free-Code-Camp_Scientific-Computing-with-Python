# https://replit.com/@GabrielAlmeid57/boilerplate-probability-calculator-1#py

import copy
import random

class Hat:
  contents = []
  
  def __init__(self, *values, **kwargs):
    supArray = []
    for key in kwargs:
      for i in range(kwargs[key]):
        supArray.append(str(key))

    self.contents = copy.copy(supArray)
  
  def draw(self, numBals):
    if numBals > len(self.contents):
      numBals = len(self.contents)
    
    drawLis = []

    for ind in range(numBals):
      num = random.randrange(0, len(self.contents))
      drawLis.append(self.contents.pop(num))
    
    return drawLis

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for ind in range(num_experiments):
    obj = copy.deepcopy(hat)
    test = copy.deepcopy(obj.draw(num_balls_drawn))
    flag1 = True
    for key in expected_balls:
      if(test.count(key) < expected_balls[key]): 
        flag1 = False
    if flag1:
      M += 1
      
  return (100*(M/num_experiments))


if __name__ == '__main__':  
  random.seed(95)
  hat = Hat(blue=4, red=2, green=6)
  probability = experiment(
      hat=hat,
      expected_balls={"blue": 2,
                      "red": 1},
      num_balls_drawn=4,
      num_experiments=3000)
  print("Probability:", probability)