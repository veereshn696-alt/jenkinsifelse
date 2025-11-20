import sys
if len(sys.argv) !=3:
  print("usage : python student.py <name> <rollno>")
  sys.exit(1)
  script_name=sys.argv[0]
  name=sys.argv[1]
  salary=sys.argv[2]
  empid=sys.argv[3]
else :
  script_name=sys.argv[0]
  name="veeresh"
  salary="5000"
  empid="178"
  
print("script name : ",script_name)
print("employee name  : ",name)
print("salary : ",salary)
print("employee id : ",empid)
