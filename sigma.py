class student:
  uni="NU"
  def __init__(self,name="Unknown",gropa="Unknown",id=0,gpa=1.0):
        self.name=name
        self.gropa=gropa
        self.id=id
        self.gpa=gpa
  def sayhi(self):
      print(f"hi,my name is {self.name} i study eshkere in {self.gropa}" )
  def __bool__(self):
      return self.gpa>=2.0
      
  def __str__(self):
      return f"student {self.name} have gpa{self.gpa}"
  def info(self):
      print("name",self.name)
      print("group",self.gropa)
      print("id",self.id)
      print("name",self.uni)
segma=student("bankai","nfugerug",12,2.5)
print(bool(segma))
print(segma)
