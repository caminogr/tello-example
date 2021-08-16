# from tello import Tello
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import asyncio
from tello_asyncio import Tello


async def main():

    drone = Tello()
    try:
        await drone.connect()
        await drone.sdk_version
#        await drone.takeoff()
#        await drone.send('rc 10 0 0 0')
#        time.sleep(2)
#        await drone.land()
    finally:
        await drone.disconnect()

asyncio.run(main())

#fig = plt.figure()

#tello = Tello()
#useTello = True
#if useTello:
#     await drone.connect()
#    tello.send_command('command')
#    tello.send_command('takeoff')
#    time.sleep(5)
#    tello.send_command('rc 0 50 0 0')

#height = 0

##log = tello.get_log()

#def plot(frame):
#    global height
##    stat.print_stats()
#    plt.cla()
#    x = (np.linspace(0, 2*np.pi, 500) + frame) * 1/2
#    y = np.sin(x) * 50
#    plt.plot(x,y)
#    diff = y[0] - height
#    if useTello:
#        if diff > 0:
#            tello.send_command('up '+ str(abs(diff)))
#        else:
#            tello.send_command('down '+ str(abs(diff)))

#    height = y[0]
#    print('height', str(height))
#    print('up '+ str(diff))


#ani = animation.FuncAnimation(fig, plot, interval=100)
#plt.show()
## print('stop')
#if useTello:
#    tello.send_command('land')
