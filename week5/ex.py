def footToMeter(foot):
    f = foot
    m = f * 0.3048
    return m

def meterToFoot(meter):
    m = meter
    f = m * 3.28084
    return f

print("Foot to meter: {:.2f}".format(footToMeter(1)))

print("Meter to feet: {:.2f}".format(meterToFoot(1)))

meters=[]
i = 0
for i in range(0,10):
    meters.append(footToMeter(i+1))
    i+=1

feet=[]
i = 0
for i in range(0,10):
    feet.append(meterToFoot(20+i))
    i+=1

print(meters)
print(feet)

i = 0
for i in range(0,10):
    if i == 0:
        print("Feet|Meters")
    print("{:.2f} {:.2f}".format(i+1,meters[i]))

i = 0
for i in range(0,10):
    if i == 0:
        print("Meters|Feet")
    print("{:.2f} {:.2f}".format(feet[i]/3.28084,feet[i]))

