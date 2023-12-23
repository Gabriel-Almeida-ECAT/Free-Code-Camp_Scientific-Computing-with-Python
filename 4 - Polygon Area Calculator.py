# https://replit.com/@GabrielAlmeid57/boilerplate-polygon-area-calculator#py

class Rectangle:
  width = 0
  pheight = 0
  
  def __init__(self, Pwidth, pheight):
    self.width = Pwidth
    self.height = pheight

  def set_width(self, Pwidth):
    self.width = Pwidth

  def set_height(self, pheight):
    self.height = pheight

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2 * (self.height + self.width)

  def get_diagonal(self):
    return ((self.height ** 2 + self.width ** 2) ** 0.5)

  def get_picture(self):
    if(self.height > 50 or self.width > 50):
      return "Too big for picture."
    
    rectangleStr = ""
    for i in range(self.height):
      rectangleStr += "*"*self.width
      rectangleStr += "\n"
    
    return rectangleStr

  def get_amount_inside(self, obj):
    objArea = obj.get_area()
    if(objArea > self.get_area()):
      return 0;
    else:
      return int(self.get_area()/objArea)

  def __str__(self):
    string = "Rectangle(width=%.d, height=%d)"%(self.width, self.height) 
    return string


class Square(Rectangle):
  width = 0
  pheight = 0

  def __init__(self, plength):
    self.width = plength
    self.height = plength

  def set_side(self, pside):
    self.width = pside
    self.height = pside

  def set_width(self, Pwidth):
    self.set_side(Pwidth)

  def set_height(self, Pheight):
    self.set_side(Pheight)
  
  def __str__(self):
    string = "Square(side=%d)"%(self.width) 
    return string


if __name__ == '__main__':
  rect = Rectangle(5, 10)
  print(rect.get_area())
  rect.set_width(3)
  print(rect.get_perimeter())
  print(rect)

  sq = Square(9)
  print(sq.get_area())
  sq.set_side(4)
  print(sq.get_diagonal())
  print(sq)