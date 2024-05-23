from sensor_parser import Measurement
from rplidar import RPLidar
import matplotlib.pyplot as plt
import math


PORT_NAME = '/dev/cu.usbserial-0001'

def update_canvas(data, fig, line):
    parsed_data=list()
    for measurement in data:
        if measurement.accuracy==0:
            continue
        else:
            parsed_data.append(measurement)
    a=list()
    b=list()
    for i in range(len(parsed_data)):
        a.append(math.radians(parsed_data[i].angle))
        b.append(parsed_data[i].distance)
    print(a)
    print(b)
    line.set_data(a, b)
    fig.canvas.draw()
    fig.canvas.flush_events()

                        

def run():
    '''Main function'''
    lidar = RPLidar(PORT_NAME,timeout=3)
    snapshot = list()
    plt.ion()
    fig, ax =plt.subplots(subplot_kw={'projection':'polar'})
    line, =ax.plot([0],[1200], 'ro', markersize=2, markeredgecolor="r")
    try:
        print('Recording measurments... Press Crl+C to stop.')
        counter = 1
        for measurment in lidar.iter_measurments():
            if measurment[0]==True:
                counter -= 1
                if counter == 0:
                    counter = 2
                    update_canvas(snapshot, fig, line)
                snapshot=list()
                snapshot.append(Measurement(accuracy=measurment[1], angle=measurment[2], distance=measurment[3]))
            else:
                if measurment[0]==False:
                    snapshot.append(Measurement(accuracy=measurment[1], angle=measurment[2], distance=measurment[3]))
    except KeyboardInterrupt:
        print('Stopped.')
    lidar.stop()
    lidar.disconnect()

if __name__ == '__main__':
    run()