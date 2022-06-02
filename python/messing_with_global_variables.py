workers = 20

def employeeWage():
    averageWage = int(input("what is the average hourly wage per employee to the nearest whole number?: "))
    print(f'The business has {workers} workers')
    totalWage = workers * averageWage
    print('You pay ' + str(totalWage) + ' total for ' + str(workers) + ' workers')

employeeWage()




