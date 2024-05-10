class Measurement:
    def __init__(self, accuracy, angle, distance):
        self.accuracy = accuracy
        self.angle=angle
        self.distance=distance

def parse_row(row):
    my_var=row.strip("\n").split("\t")
    return Measurement(int(my_var[1]),float(my_var[2]),float(my_var[3]))

def parse_chunk(chunk):
    measurement_list=[]
    for row in chunk:
        measurement_list.append(parse_row(row))
    return measurement_list

def get_raw_data(path_to_file):
    f= open(path_to_file)
    all_raw_data=[]
    full_circle=[]

    for line in f:
        if "True" in line:
            all_raw_data.append(full_circle)
            full_circle=[]        
            full_circle.append(line)
        else:
            if "False" in line:
                full_circle.append(line)
            else:
                break

    all_raw_data.pop(0)
    return all_raw_data

def get_data(path_to_file):
    raw_data_list=get_raw_data(path_to_file)
    data_list=[]
    for chunk in raw_data_list:
        data_list.append(parse_chunk(chunk))
    return data_list

