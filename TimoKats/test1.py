from fibooks import balance_sheet, compute

#i guess you have to instantinate the variable
tesla2018 = balance_sheet('tesla in 2018')

#then pass an external JSON file
tesla2018.import_json('tesla2018.json')

#this turns this into a balance sheet objeect
tesla2018.make()

#for 2019 financials
tesla2019 = balance_sheet("tesla in 2019")
tesla2019.import_json('tesla2019.json')
tesla2019.make()

#lets say we wanted to compute the leverage ratio
print("cash ratio:", compute.cash_ratio(tesla2018))
print("cash ratio:", compute.cash_ratio(tesla2019))

print("capital ratio:",compute.debt_to_capital_ratio(tesla2018))
print("capital ratio:",compute.debt_to_capital_ratio(tesla2018))