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
'''

name_first = input('What is your First name: ');

while name_first == (''):
    print("Please Enter First name it can't be Empty")
    name_first = input('What is your First name: ');
    
name_middle = input('What is your Middle name: ');

while name_middle == (''):
    print("Please Enter Middle name it can't be Empty or type 'NA'")
    name_middle = input('What is your Middle name: ');

name_last = input('What is your Last name: ');
while name_last == (''):
    print("Please Enter Last name it can't be Empty")
    name_last = input('What is your Last name: ');
    
if name_middle == 'NA':
    print(name_last, name_first);
else:
    
    print(name_last, name_middle, name_first);
