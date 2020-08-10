import sqlite3
class myconnect:
      
      def __init__(self):
              
            try:
                self.conn = sqlite3.connect("emp.db")
                self.conn.execute('create table if not exists emp (name text, salary interger, emp_type char)')
                print('table created')
            except:
                pass
                 
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
          pass
      def display(self):
          pass