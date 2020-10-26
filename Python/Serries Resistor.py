num_resistors = 5
resistors = []
voltage_drop = []

print( '%d resistors are in series.' % num_resistors)
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print (input_voltage)
print('Input ohms of %d resistors' % num_resistors)
for i in range(num_resistors):
    res = float(input('%d)' % (i + 1)))
    print(res)
    resistors.append(res)

current = input_voltage / sum(resistors)
print('Total current is :',current)
for n, f in enumerate(resistors) :
    print('The voltage drop of number %d ressistor, the %0.2f ohm ressistor is %0.2f' % (f , n , (current * n)))
