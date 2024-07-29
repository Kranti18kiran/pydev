import math
#print(math.ceil(2.9))

'''
n = input("Enter value: ");
even = 0;
odd = 0;

for i in n:
    if int(i)%2==0:
        even = even+int(i)
    else:
        odd = odd+int(i)
print(even, odd)
'''
'''
name = input('Enter new patient: ');
age = int(input('enter age: '));
is_new = True;

if age > 20:
    print('he already exist');
else:
    
    print('Hi ' + name, age, 'New Patient')

name = input('What is your name: ');
color = input('What is your favourite color? ');

print(name + ' likes ' + color );

# weight conversion from lbs to kg
name = input('What is your name: ');
weight = float(input('What is your weight in lbs: '));
weight_convert = weight * 0.453;
roundup_con_weight = round(weight_convert, 2)
print('Your weight in kg:' roundup_con_weight);

#entering names and extracting the total
name_first = input('What is your First name: ').capitalize();

while name_first == (''):
    print("Please Enter First name it can't be Empty")
    name_first = input('What is your First name: ').capitalize();
    
name_middle = input('What is your Middle name: ').capitalize();

while name_middle == (''):
    print("Please Enter Middle name it can't be Empty or type 'NA'")
    name_middle = input('What is your Middle name: ').capitalize();

name_last = input('What is your Last name: ').capitalize();
while name_last == (''):
    print("Please Enter Last name it can't be Empty")
    name_last = input('What is your Last name: ').capitalize();
    
if name_middle == 'NA':
    print(name_last, name_first);
else:
    
    print(name_last, name_middle, name_first);
    
print(len(name_last), len(name_middle), len(name_first));
L_val = int(len(name_last));
m_val = int(len(name_middle));
f_val = int(len(name_first));
print(f'{L_val}+{m_val}+{f_val}');
total_val = L_val+m_val+f_val;
print(total_val);

# conditions
price_house = 1000000;
good_credit =False;

if good_credit:
    print("Need 10% Desposit");
    down_payment = 0.1 * price_house;
else:
    print("Need 20% Desposit");
    down_payment = 0.2 * price_house;
    
print(f'Down Payment: ${down_payment}');

#weight conversion
weight = int(input("Weight: ")); 
unit = input('(L)bs or (K)gs: ')
if unit.upper() == 'L':
    converted = weight * 0.453;
    roundup_converted = round(converted, 2)
    print(f'you are {roundup_converted} kgs')
     
else:
    converted = weight / 0.453;
    roundup_converted = round(converted, 2)
    print(f'you are {roundup_converted} pounds')


# Car Game to start and stop
command = '';
started = False;
while True:
    command =  input('> ').lower();
    if command == "start":
        if started:
            print("Car already started !")
        else:
            started =True
            print("Car started...");
    elif command == "stop":
        if not started:
            print("Car alredy stopped !");
        else:
            started = False
            print("Car stopped...");
    elif command == "help":
       print("""
Start -> to start the car
Stop  -> to Stop the car
quit  -> to quit    
            """);
    elif command == "quit":
        break;
    else:
        print("Sorry, I don't understand that!");
 '''         
        
        
       

 





    
