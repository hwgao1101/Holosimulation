import holoocean
import matplotlib.pyplot as plt
import numpy as np
import manuControl as mc
import saveData as sd

#### GET SONAR CONFIG
scenario = "SimpleUnderwater-HoveringSonar" #
config = holoocean.packagemanager.get_scenario(scenario)
config = config['agents'][0]['sensors'][-1]["configuration"]
azi = config['Azimuth']
minR = config['MinRange']
maxR = config['MaxRange']
binsR = config['BinsRange']
binsA = config['BinsAzimuth']

#### GET PLOT READY
plt.ion()
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'), figsize=(8,5))
ax.set_theta_zero_location("N")
ax.set_thetamin(-azi/2)
ax.set_thetamax(azi/2)

theta = np.linspace(-azi/2, azi/2, binsA)*np.pi/180
r = np.linspace(minR, maxR, binsR)
T, R = np.meshgrid(theta, r)
z = np.zeros_like(T)

plt.grid(False)
plot = ax.pcolormesh(T, R, z, cmap='gray', shading='auto', vmin=0, vmax=1)
plt.tight_layout()
fig.canvas.draw()
fig.canvas.flush_events()

index = 1

#### RUN SIMULATION
# command = np.array([0,0,0,0,-20,-20,-20,-20]) # 给机器人的控制指令，需要修改成从键盘端输入的形式
with holoocean.make(scenario) as env:
    while True:
        if 'q' in mc.pressed_keys: # 退出仿真系统
            break
        filename = './Data/SimpleUnderwater/Data/{}.pkl'.format(index) # 跑不同的仿真环境把数据存储到不同的地方
        command = mc.parse_keys(mc.pressed_keys, mc.force)
        env.act("auv0", command)
        state = env.tick()
        sd.save_pkl(filename,state)

        if 'SonarSensor' in state:
            s = state['SonarSensor']
            plot.set_array(s.ravel())

            fig.canvas.draw()
            fig.canvas.flush_events()

        index = index + 1

print("Finished Simulation!")
plt.ioff()
plt.show()