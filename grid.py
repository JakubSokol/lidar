from sensor_parser import get_data 
import matplotlib.pyplot as plt
import numpy as np
import math

if __name__=="__main__":
    data = get_data("out.txt")
    a=[]
    b=[]
    number_of_cycle = 4
    print(type(data[0][0].accuracy))
    for i in range(0,len(data[number_of_cycle])):
        if data[number_of_cycle][i].accuracy ==0:
            continue
        else:
            a.append(math.radians((data[number_of_cycle][i].angle)))
            b.append(data[number_of_cycle][i].distance)
    fig, ax =plt.subplots(subplot_kw={'projection':'polar'})
    ax.plot(a,b, 'ro', markersize=2)
    plt.show()
