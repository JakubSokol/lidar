from sensor_parser import get_data 
if __name__=="__main__":
    print(get_data("out.txt"))
    """
    TODO:
    1 filter out invalid data
    2. create variable which consist of one 360 degree meeasurement
    3. create two axis: horizontal and vertical with markings at each 10cm
    4. display a dot representing a single point (first elem from 360 degree measurement)
    5. display every points
    """