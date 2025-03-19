# area of circle
def area_circle(r):
  area = 3.14*r**2
  return area
  

  # area of traingle
def area_traingle(base,height):
  area = (1/2)*base*height
  return area

# area of rectangle
def area_rectangle(len,breadth):
  area = len*breadth
  return area

# area of traingle
def area_trangle2(a,b,c):
  s = (a+b+c)/2
  area = (s*(s-a)*(s-b)*(s-c))**(1/2)
  return area

# area of parallalogram
def area_parallelogram(base,height):
  area = base*height
  return area

def area_rhombus(dia1,dia2):
  area = (dia1*dia2)/2
  return area

def area_equi_traingle(side):
  area = (3/4)**(1/2)*side**2
  return area

