class Per_Emp:

      basic_salary = 5000
      def calculatesalary(self,exp):
            if exp > 15:
                  self.basic_salary = self.basic_salary + ((self.basic_salary*20)/100)
                  return self.basic_salary
            elif exp >=10 and exp <=15:
                  self.basic_salary = self.basic_salary + ((self.basic_salary*10)/100)
                  return self.basic_salary
            else:
                  return self.basic_salary
                  

                  
                  
            
