slabs = list(map(int,input().split()))
tax_rate = list(map(int,input().split()))
rebate = int(input())
tax_paid = list(map(int,input().split()))
num_employees = len(tax_paid)
salary = [0] * num_employees
for i in range(num_employees):
    paid_by_curr_employee = tax_paid[i]
   # print( paid_by_curr_employee)                              
    salary[i] =salary[i]+slabs[0]
    for  j in range(1,len(slabs)):
        max_slab = tax_rate[j-1]*(slabs[j]-slabs[j-1])/100
        if max_slab <= paid_by_curr_employee:
            salary[i]=salary[i]+(slabs[j]-slabs[j-1])
            paid_by_curr_employee= paid_by_curr_employee-max_slab
        else:
            slab_paid = ((employee_paid*100)/tax_rate[j-1])
            salary[i] = salary[i] + slab_paid
            paid_by_curr_employee = paid_by_curr_employee - slab_paid
    if paid_by_curr_employee > 0:
       salary[i] = salary[i]+(( paid_by_curr_employee*100))/tax_rate[-1]
    salary[i]  = salary[i]  + rebate
    salary[i] = int(salary[i])
   # print(salary)

total_salary_emp = sum(salary)

print(total_salary_emp)
