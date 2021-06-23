import pandas as pd
import plotly.express as px

while True:
    
    try:
        
        amb_temp = float(input("Enter ambient room temeperature (Celsius): "))
        rad_distance = float(input("Enter the Horizontal distance between the fire and sprinkler head (meters): "))
        height_above_fire = float(input("Enter the vertical distance between the fire and sprinkler head (meters): "))
        RTI = float(input("Enter RTI value of the sprinkler head: "))
        c = float(input("Enter conduction value of the sprinkler head: "))
        activation = float(input("Enter sprinkler activation temperature: "))
        break
    
    except ValueError as e:
        print("Error: Enter a valid number")
        
#then make a growth_rate list
t_sq_list = ['slow', 'medium', 'fast', 'ultra-fast']
t_sq = None

#not sure that this is
while t_sq not in t_sq_list:
    
    t_sq = input("Enter fire's growth rate, selection from list [slow, medium, fast, ultra-fast]: ") 
    
if t_sq == "slow":
    growth = 0.00293
    
elif t_sq == "medium":
    growth = 0.01172
    
elif t_sq == "fast":
    growth = 0.0469
    
print("fire growth rate coefficient is: " + str(growth))

#they make a dataframe that will accomodate all of the rates and it will take 1307 seconds to reach 5MW
index = pd.RangeIndex(0, 1380, 1)
columns = ['time', 'HRR', 'gas temp 1', 'gas temp 2', 'gas vel 1', 'gas vel 2', 'gas temp', 'temp sprinkler']
df = pd.DataFrame(index = index, columns = columns)
df = df.fillna(0)

#now populate the growth
df['Time'] = df.index
df['HRR'] = df['Time'] * df['Time'] * growth

#this will be for the gas temperatures
if rad_distance / height_above_fire > 0.18:
    
    df['gas temp 1'] = (5.38 * (df['HRR'] / rad_distance) ** (2/3)) / height_above_fire
    df['gas temp']  = df['gas temp 1'] + amb_temp
    a = 'one'
    
else:
    
    df['gas temp 2'] = (16.9 * (df['HRR']) ** (1/3)) / height_above_fire ** (5/3)
    df['gas temp'] = df['gas temp 2'] + amb_temp
    a = 'two'
    
    