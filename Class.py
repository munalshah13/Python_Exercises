# Define a new class name member
import datetime as dt


class Member:   #create a new member.
   
   #class varaible
   
   expiry_days = 365   
   

    
    #Constructor
   
   """ Calss create in stance method by init-is short initialize, its just function that's defined inside the class, displya like __init__ """

   def __init__ (self, firstname, lastname, age):   # parameters with __inti__ () methods
        
       # define and giving an object attribute and give them values.
       self.firstname = firstname
       self.lastname = lastname
       self.age = age
        
        #default date_joined to today date
       self.date_joined = dt.date.today()

        # set an expiration date
       self.expiry_date = dt.date.today() + dt.timedelta(days = Member.expiry_days)
        # set is active to true intiative
       self.is_active = True

       

    
   def myinfo(self):  # instance methods
       print("my username is" + self.firstname)
       print("My fullname is" + self.lastname)
       print("My age is " + self.age.title())
        
   def show_datejoined(self):    # instance methods with specific objects
       return f"{self.firstname} joined on {self.date_joined:%m/%d/%y}"

   def activate(self, yesno):# Passing parameters to instance methods
        
        # true for active , false to make inactive
       self.is_activate = yesno  # is_activate is attribute
        


   # Class methods : that is associated with the class as whole rather than instance of the class, not specific instances of the class.
   @classmethod
   
   def setfreedays(cls,days):
      cls.expiry_days = days
       

   @staticmethod

   def currenttime():
      now = dt.datetime.now()
      return f"{now:%I:%M %p}"

   def showexpiry(self):
      return f"{self.firstname} {self.lastname} Account expire on{self.expiry_date}"

   
#Subclass for admin
class Admin(Member):

   expiry_days = 365.2422 * 100
   
   #Adding extra parameter into subclass
   """ Note:Let's admins have some secret code and you want to pass tht from the admin subclass,
       You still have to pass the first and last name, so the name of parameters you want to send to the base class
       this should be everything that's already in the member parameters excluding self.
       Memeber class expect only firstname and lastname, so write as below
   """
   def __init__(self, firstname, lastname, age, secret_code):
      
      # pass Member parameter on up to member class
      super().__init__(firstname, lastname,age)

      # Assign the remaining parameter to this object
      self.secret_code = secret_code

#Subclass for user
class User:
   pass




def main():
   # the class end at the first un-indented line.

   """ create an instance from a class(member class),
      create an instance  of the member class named new_guy """

   new_guy = Member('Ramdo', 'Moe', 19)

   print("Full Name:",new_guy.firstname, new_guy.lastname)
   print("Age:",new_guy.age)
   print(Member.show_datejoined(new_guy)+ "," + Member.currenttime())
   print("Free trial is due on:",new_guy.expiry_date)
   print()

   Ann = Admin('Annie', 'Angest', 27, 'Presto')
   print(Ann.firstname, Ann.lastname, Ann.expiry_date, Ann.secret_code)
   print(Ann.showexpiry())
   print()

   print(new_guy.is_active)
     

     
if __name__ == '__main__':
   
   main()
   

                 
                 
