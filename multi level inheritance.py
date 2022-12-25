class office():
    emp_id=''
    emp_name=''
    salary=''
    manager=''

emp1=office()
emp1.emp_id="001"
emp1.emp_name="Sorna sree"
emp1.salary="50,000"
emp1.manager="nil"



emp2=office()
emp2.emp_id="002"
emp2.emp_name="Riyaswari"
emp2.salary="40,000"
emp2.manager=emp1.emp_name


emp3=office()
emp3.emp_id="003"
emp3.emp_name="Thamarai selvi"
emp3.salary="30,000"
emp3.manager=emp2.emp_name


emp4=office()
emp4.emp_id="004"
emp4.emp_name="senthamil kumaran"
emp4.salary="20,000"
emp4.manager=emp3.emp_name

emp5=office()
emp5.emp_id="005"
emp5.emp_name="Vignesh kumar"
emp5.salary="10,000"
emp5.manager=emp4.emp_name


def output(ans):
    print(f"employee id: {ans.emp_id}")
    print(f" employee name: {ans.emp_name}")
    print(f"employee salary is {ans.salary}")
    print(f"{ans.emp_name} manager is {ans.manager}")


output(emp1)
print()
output(emp2)
print()
output(emp3)
print()
output(emp4)
print()
output(emp5)



