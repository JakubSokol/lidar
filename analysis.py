f= open("out.txt","r")
#print(f.read())

all_data=[]
full_circle=[]

for line in f:
    if "True" in line:
        all_data.append(full_circle)
        full_circle=[]        
        full_circle.append(line)
    else:
        if "False" in line:
            full_circle.append(line)
        else:
            break

all_data.pop(0)

class measurements:
    def __init__(self, accuracy, angle, distance):
        self.accuracy = accuracy
        self.angle=angle
        self.distance=distance




for i in range(0,len(all_data)):
    print(all_data[i][0])
    print(len(all_data[i]))