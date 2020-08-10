import sqlite3
class myconnect:
      
      def __init__(self):
            self.conn = sqlite3.connect("emp.db")
            
            try:
                  self.conn.execute('create table if not exists emp (name text, salary interger, emp_type char)')
                  print('table created')
            except:
                  pass
                 
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6

      # def display(self):
      #       #7