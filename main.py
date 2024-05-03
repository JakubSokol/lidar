from rplidar import RPLidar
lidar = RPLidar(port='/dev/cu.usbserial-0001',timeout=3)

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Got %d measures' % (i, len(scan)))
    if i > 10:
        break
lidar.stop()
lidar.stop_motor()
lidar.disconnect()