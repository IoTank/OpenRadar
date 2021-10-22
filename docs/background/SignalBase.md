---
title: SignalBase
date: 2020-07-1 16:00:04
author: liudongdong1
img: https://gitee.com/github-25970295/blogImage/raw/master/img/sunset-over-meadow-and-trees.jpg
cover: false
categories: AIOT
tags:
  - mmwave
---

### 1. IQ Signals

#### 1. Basic signal

$$
basic \quad wave: v(t)=A*sin(2\pi ft+\phi)\\
$$

#### 2. Simple Amplitude Modulation

$$
simple\quad amplitude \quad modulation: v(t)=A(t)*sin(2\pi ft +\phi)\\
$$

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014103258531.png)



#### 3. Quadrature signals(正交信号)

- the amplitude of the "in-phase" signal =I:  $I*cos(2\pi ft)$;
- the amplitude of the "90 degree" signal=Q: $Q*sin(2\pi ft)$

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014104709972.png)

#### 4. Digital Modulation--Binary Phase Shift Keying

- $I(t)$ varies between [+1, -1];
- $Q(t)= \phi$;

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014105352652.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014105842054.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014110119616.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015204500312.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015202435959.png)

数字通信系统需要将信息0-1比特流（例如 0101110101），从发端通过无线信道发送到收端。在发端发送前，需要将0-1比特流调制到模拟信号上。常用的调制方式有`BPSK, QPSK, 16QAM, 64QAM`等。其理论基础是通过图1所示的星座图，根据比特流确定调制信号：

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015192744797.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015192903255.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015193125512.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015193246398.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015193559310.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015193642942.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015193741310.png)

> An object at a distance d results in an IF tone of frequency S2d/c;
>
> two tones can be resolved in frequency as long as the frequency difference $\theta f> 1/T$;
>
> range resolution($d_{res}$) depends on the bandwidth(B): $d_{res}=c/2b$;
>
> the ADC sampling rate $F_s$ limits the max range ($d_{max}$) to :$ d_{max}=F_sc/S$;
>
> `measure range, velocity, angle;`

### 2.FMCW

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502141026273.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502141115497.png)![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502141827806.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502141304241.png)

1. **距离分辨率(Range Resolution)**

雷达需要具备区分两个距离非常近的目标的能力. 比如, 当雷达的距离分辨率为4米时, 它就不能区分相距1m的行人和汽车. 距离分辨率完全取决于啁啾的带宽*B_sweep*.

![[公式]](https://gitee.com/github-25970295/blogpictureV2/raw/master/equation)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502134925116.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502135412193.png)	 ![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502135813371.png)![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502135856510.png) 	

1. **速度分辨率(Velocity Resolution)**

如果两个目标有相同的距离, 但是当它们以不同的速度移动, 它们仍然可以被区分开来. 速度分辨率取决于啁啾的个数. 正如讨论我们的情况下, 我们选择发送128个啁啾. 较高的啁啾数量增加了速度分辨率, 但它也需要更长的时间来处理信号.

1. **角度分辨率(Angle Resolution)**

雷达能够在空间上分离两个目标. 即使两个目标在相同的距离以相同的速度运动, 它们仍然可以通过雷达坐标系中的角度分辨出来.

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502142204305.png) 	

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502142443247.png) 	![image-20210502142530586](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502142530586.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502142759519.png)



Application:

- mmWave-based human sensing:
  - detects minute variations caused by human withoud body contact.  1,24;
  - activity recognition: 23, 32, 79;
  - emotion recognition: 78
  - detection of biometrics: 72,78
    - 48 measure the respiration and heart rates 10m;
    - 34 user authentication;
    - 33, 69 voice-related information to facilitate voice-user interface.

- Voice authentication:
  - based on the distinction between human and loudspeaker 58, 59;
  - RF reflections 41
  - ultrasonic reflection 76
  - magnetic field from the loudspeaker 10;
  - pop music in human utterances 67
  - VAuth 18 contact based sensors for voice authentication, vocal resonance 35.

Limitation:

- Long sensing distance:
  - distance increases, velocity resolution of the range profile degrade.	
  - by increase the bandwidth of IF signals in mmWave waveform design.[11]
- Sensing orientation:
  - collect data covering different orientations,
  - using beam forms;

- Compatibility with IoT Devices:
  - high sampling rate produce massive data samples.
  - using high-speed DSP processors;

- 学习视频：https://training.eeworld.com.cn/TI/video/10162

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502200627857.png)

> 连续波雷达发射的信号可以是单频连续波(CW)或者调频连续波(FMCW)，调频方式也有多种，常见的有三角波、锯齿波、编码调制或者噪声调频等。其中，单频连续波雷达仅可用于测速，无法测距，而FMCW雷达既可测距又可测速，并且在近距离测量上的优势日益明显。

#### 1. 距离测量

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210502194513.png)

-  距离分辨率

> - 区分俩个靠近的物体，通过延长IF信号，可以提高分辨率；而延长IF信号，会增加带宽。
> - 观测窗口（T）可以区分间隔超过1/T hz的频率分量。$\Delta f>1/T_C$; $d_{Res =c/2B}$;

#### 2. 速度测量

- 使用位于同一距离的多个物体

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502200521025.png)

#### 3. 角度测量

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210502201013652.png)

#### 4. Ti Rada Demo

> 回波采样间隔与脉冲重复间隔（脉冲周期）虽然在一个时间轴上，但是在量级上差别非常大，回波采样间隔大概在10^{-8}量级，而脉冲重复周期大概在1 0 − 3  级别，所以在处理的时候可能会不方便。于是将回波采样间隔与脉冲重复周期分成了两个维度，分别称为快时间和慢时间。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527200229296.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527200304094.png)

##### .1. data structure

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527104711123.png)

##### .2. Range FFT 测距

> 针对一个single chirp，若干个接受回来的信号。 从而在多远处有物体，但是不知道在那个方位。range bin 可以转化为实际的距离信息。

```python
# Read in chirp data
adc_samples = np.loadtxt('../assets/chirp.txt', dtype=np.complex_)
# Manually cast to signed ints
adc_samples.real = adc_samples.real.astype(np.int16)
adc_samples.imag = adc_samples.imag.astype(np.int16)
# Take a FFT across ADC samples
range_bins = np.fft.fft(adc_samples)
# Plot the magnitudes of the range bins
plt.plot(np.abs(range_bins))
plt.xlabel('Range Bins')
plt.ylabel('Reflected Power')
plt.title('Interpreting a Single Chirp')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527105006470.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527105454921.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527105554848.png)

```python
# Data sampling configuration
c = 3e8 # Speed of light (m/s)
sample_rate = 2500 # Rate at which the radar samples from ADC (ksps - kilosamples per second)
freq_slope = 60 # Frequency slope of the chirp (MHz/us)
adc_samples = 128 # Number of samples from a single chirp
```

##### 3. Doppler Effect 测速

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527111037378.png)

> Some object in front of the radar will `reflect portions of the first chirp`. Now the `second, third, and so on chirps` hit this object and reflect. For simplicity, let's assume that the object is stayed within a single range bin for the duration of the entire frame and is moving at a constant velocity. There should be some `set of samples across the separate chirps` that hold this valuable information.
>
> - The doppler effect is what happens when `a wave hits a moving object.`
> - 对一个frame数据进行 fft 处理，其中一个fram而数据包括多个chirp

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527111323784.png)

- **Range FFT**

```python
# Read in frame data
frame = np.load('../assets/simple_frame_1.npy')

# Manually cast to signed ints
frame.real = frame.real.astype(np.int16)
frame.imag = frame.imag.astype(np.int16)

# Meta data about the data
num_chirps = 128 # Number of chirps in the frame
num_samples = 128 # Number of ADC samples per chirp
#Perform the range FFt on the entire frame， Output: range_plot [chirps, range_bins]\n 
range_plot = np.fft.fft(frame, axis=1)

# Visualize Results   #纵坐标对应range-fft的距离信息，可以看出存在移动的上下波动
plt.imshow(np.abs(range_plot).T)
plt.ylabel('Range Bins')
plt.title('Interpreting a Single Frame - Range')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527111429009.png)

> the radar definitely sees something at various ranges. Notably, we can see peak lines at range bins ~40 and ~115. Still, it's hard to tell exactly what. We should now try and also obtain velocity information.

- Doppler-FFT

```python
# Take a sequential FFT across the chirps
range_doppler = np.fft.fft(range_plot, axis=0)

# FFT shift the values (explained later)
range_doppler = np.fft.fftshift(range_doppler, axes=0)

# Visualize the range-doppler plot
# plt.imshow(np.log(np.abs(range_doppler).T))
plt.imshow(np.abs(range_doppler).T)
plt.xlabel('Doppler Bins')
plt.ylabel('Range Bins')
plt.title('Interpreting a Single Frame - Doppler')
plt.show()

plt.plot(np.abs(range_doppler))
plt.xlabel('Doppler Bins')
plt.ylabel('Signal Strength')
plt.title('Interpreting a Single Frame - Doppler')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527112505089.png)

> `line in the middle at doppler bin 64` is called `zero doppler`, meaning `everything along that line is static/not moving relative to the radar`. 
>
> 1. `Much of the received signal translates to having zero doppler,` which makes sense if you think about it because most of the objects around us (and the radar) are not moving and thus zero doppler relative to us.
> 2. The plots show at` range bin ~40`, there is a` grouping of peaks in intensity off to the left`, meaning an object is` most likely moving towards the radar`.
> 3. Also, at `range bin ~115`, we see there is a `peak in the middle of the doppler bins`, meaning there is probably `a highly reflective static object in front of the radar`. These described peaks are more clearly shown in the second plot.

- Range-FFT 和Doppler-FFT 执行先后顺序没有什么影响

```python
# Range FFT -> Doppler FFT
range_bins = np.fft.fft(frame, axis=1)
fft_2d = np.fft.fft(range_bins, axis=0)

# Doppler FFT -> Range FFT
doppler_bins = np.fft.fft(frame, axis=0)
rfft_2d = np.fft.fft(doppler_bins, axis=1)
#Max power difference:  5.64766185425834e-11
print('Max power difference: ', np.abs(fft_2d - rfft_2d).max())
```

- Unit conversion

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527124142284.png)

```python
# Data sampling configuration
c = 3e8 # Speed of light (m/s)
sample_rate = 2500 # Rate at which the radar samples from ADC (ksps - kilosamples per second)
freq_slope = 60 # Frequency slope of the chirp (MHz/us)
adc_samples = 128 # Number of samples from a single chirp

start_freq = 77.4201 # Starting frequency of the chirp (GHz)
idle_time = 30 # Time before starting next chirp (us)
ramp_end_time = 62 # Time after sending each chirp (us)
num_chirps = 128 # Number of chirps per frame
num_tx = 2 # Number of transmitters

# Range resolution
range_res = (c * sample_rate * 1e3) / (2 * freq_slope * 1e12 * adc_samples)
print(f'Range Resolution: {range_res} [meters/second]')

# Apply the range resolution factor to the range indices
ranges = np.arange(adc_samples) * range_res

# Make sure your equation translates to the following
velocity_res = c / (2 * start_freq * 1e9 * (idle_time + ramp_end_time) * 1e-6 * num_chirps * num_tx)
print(f'Velocity Resolution: {velocity_res} [meters/second]')

# Apply the velocity resolution factor to the doppler indicies
velocities = np.arange(num_chirps) - (num_chirps // 2)
velocities = velocities * velocity_res

powers = np.abs(range_doppler)

# Plot with units
plt.imshow(powers.T, extent=[velocities.min(), velocities.max(), ranges.max(), ranges.min()])
plt.xlabel('Velocity (meters per second)')
plt.ylabel('Range (meters)')
plt.show()

plt.plot(velocities, powers)
plt.xlabel('Velocity (meters per second)')
plt.ylabel('Reflected Power')
plt.title('Interpreting a Single Frame - Doppler')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527124339763.png)

##### 4. 测角度利用多个接收天线

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527124605853.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527124736245.png)

```python
# Read in frame data
frame = np.load('../assets/doppler_example_1.npy')

# Manually cast to signed ints
frame.real = frame.real.astype(np.int16)
frame.imag = frame.imag.astype(np.int16)

print(f'Shape of frame: {frame.shape}')  #Shape of frame: (128, 8, 128)  理解这个维度数据

# Meta data about the data
num_chirps = 128 # Number of chirps in the frame
num_samples = 128 # Number of ADC samples per chirp

num_tx = 2
num_rx = 4
num_vx = num_tx * num_rx # Number of virtual antennas  
```

- Range-FFT

```python
# range-dopplor
range_plot = np.fft.fft(frame, axis=2)

# Visualize Results
plt.imshow(np.abs(range_plot.sum(1)).T)
plt.ylabel('Range Bins')
plt.title('Interpreting a Single Frame - Range')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527125331978.png)

- doppler FFT

```python
range_doppler = np.fft.fft(range_plot, axis=0)
range_doppler = np.fft.fftshift(range_doppler, axes=0)

# Visualize Results
plt.imshow(np.log(np.abs(range_doppler).T).sum(1))
plt.xlabel('Doppler Bins')
plt.ylabel('Range Bins')
plt.title('Interpreting a Single Frame - Doppler')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527125418414.png)

- Azimuth FFT

```python
"""
    Task: Perform the range FFt on the entire frame
    Output: range_azimuth [azimuth_bins, range_bins]
    
    Details: There are three basic things you will need to do here:
                1. Zero pad each virtual antenna array (axis 1) from 8 elements to num_angle_bins elements
                2. Perform the Azimuth FFT
                3. Accumlate result over all doppler bins (for visualization purposes)
"""
num_angle_bins = 64
""" REMOVE """
padding = ((0,0), (0,num_angle_bins-range_doppler.shape[1]), (0,0))
range_azimuth = np.pad(range_doppler, padding, mode='constant')
range_azimuth = np.fft.fft(range_azimuth, axis=1)
range_azimuth = range_azimuth

# Visualize Results
plt.imshow(np.log(np.abs(range_azimuth).sum(0).T))
plt.xlabel('Azimuth (Angle) Bins')
plt.ylabel('Range Bins')
plt.title('Interpreting a Single Frame - Azimuth')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527125611567.png)

### 3. FFT transform

#### 1. 旋转表示

> 指数函数中，以 ee 为底的函数有着特殊的性质，如下面动图所示，ππ 单位的 e6.28ie6.28i 就表示一个单位圆的360°旋转，则 e2πite2πit 表示的就是**一秒钟一圈**的旋转方程，感觉速度有点太快了，所以加一个 ff 频率，控制**旋转的速度** ，图中为 110110 ，合起来表示**一秒钟十分之一圈**

![](https://gitee.com/github-25970295/blogImage/raw/master/img/fe.gif)

#### 2. 缠绕表示

> 在傅立叶变换中，我们**规定**旋转是顺时针的（规定只是为了统一标准，并且有时候也会考虑**书写简洁**和**方便计算**），所以先加一个负号。假设原来的函数是 g(t)，将两者的**幅值相乘**就能得到缠绕图像， 

![circle](https://gitee.com/github-25970295/blogImage/raw/master/img/circle.gif)

#### 3. 质心表示--》采样； 积分；

![](https://gitee.com/github-25970295/blogImage/raw/master/img/sample1.gif)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/sample2.gif)

> 看到常数项系数 1t2−t11t2−t1 ，如果忽略表达倍数关系的系数，对应的含义也会发生变化，不再是质心，而是**信号存在的时间越久**，位置是质心位置乘以一个倍数，它的值**就越大**。参看下面的动图，持续时长为3秒，那么新的位置就是原来质心位置的三倍；为6秒，就是原来的6倍

![](https://gitee.com/github-25970295/blogImage/raw/master/img/limit.gif)

#### 4. 原始信号长度影响

> 假设我们的信号有4.5s。那么考虑**原信号的长度的变化**呢？首先，假设**信号的长度很长**，那么缠绕圆上的线就会更多，每次接近稳定图像质心的变化速度更快（即频域图像更加密集），参看下面动图

![relation](https://gitee.com/github-25970295/blogImage/raw/master/img/relation.gif)

> 那么对应的，如果**原信号的长度缩短**呢？如下面动图所示，频域图像会更加稀疏。原因同理，当**缠绕的内容少的时候，重心变化的速度也相应的变慢了**

![](https://gitee.com/github-25970295/blogImage/raw/master/img/relation2.gif)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/seeF.gif)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015210331867.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/7cc829d3gw1egu4mtx2sjg2074074tha.gif)

![271734071031740](https://gitee.com/github-25970295/blogImage/raw/master/img/271734071031740.gif)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015210539831.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/summary.gif)

> Phase of the peak is equal to the initial phase of the sinusoid.

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201013154354936.png)

### 4. 波束管理

#### 1. 任意观察点O的电厂计算

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015195807102.png)

#### 2. 远场阈观察点O电场

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015200717700.png)

#### 3. 波束成形设计

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015201312623.png)

- [**BeamForm(波束成形):**](http://blog.sina.com.cn/s/articlelist_1010013104_0_1.html)  

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015100147434.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015171921773.png)

> 数据流通过数字权值加权后映射到不同的天线子阵上，每个天线子阵由m1×m2个天线阵子组成，每个阵子乘以1个模拟权值向量（AWV——Antenna Weight Vector）后进行迭代处理，形成一个符合期望指向和宽度的波束，即每个天线阵子分别根据一个m1×m2个模拟权值向量构成的模拟权值码本形成一个波束将数据发送出去。由发送SSB信号的多个波束的覆盖组合形成小区完整的覆盖范围，即图1中由N个广播波束覆盖的范围为该小区的覆盖范围。N个波束由N个m1×m2的权值码本（Code Book）形成，即一个小区由针对广播信道的N个模拟码本（Analog Code Book）形成完整的小区覆盖，通过修改这N个模拟码本，就可以满足不同的覆盖要求。

> 在毫米波组网方面，考虑毫米波波长太短，传输特性受环境影响非常大。空气、玻璃、建筑、降雨等都会对毫米波的传播带来致命影响。所以毫米波通常应用于视野较好、无明显遮挡物的场景，如室内场景（包括体育馆场景）、街道等室外空旷区域场景。

- **Beam Management(波束管理):**毫米波基站采用较宽的波束发送SSB信道和系统消息，而针对某个UE的业务传输采用较窄的波束，不同的波束设计和管理思路如下。

  ![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015101106018.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015105133401.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015104712921.png)

**传输时：**

> - 当gNB正在发送时，gNB通过评估来自UE的多个波束的特定参考信号的质量来找出该方向。gNB评估来自多个波束中的每个波束的参考信号的质量并选择最佳波束。来自UE的参考信号称为SRS。
>
> - 当UE正在发送时，UE通过评估来自gNB的多个波束的特定参考信号的质量来找出该方向。UE评估来自多个波束中的每个波束的参考信号的质量并选择最佳波束。在这种情况下来自gNB的参考信号可以根据情况而变化。有时它可能是SSB，有时它可能是CSI-RS。（注意：除了波束管理和非常复杂的主题之外，CSI-RS还扮演着许多不同的角色。有关详细信息，请参阅[CSI-RS信号生成](http://www.sharetechnote.com/html/5G/5G_CSI_RS.html)和[CSI报告页面](http://www.sharetechnote.com/html/5G/5G_CSI_Report.html)）。

**收到时：**

> - 当gNB从UE接收信号时（在此之前），gNB应该以CSI报告的形式从UE获得最佳方向的信息。
> - 当UE从gNB接收信号时（在此之前），UE应该从gNB获得最佳方向的信息（gNB已经基于来自UE的多个波束的SRS信号质量的测量来检测到最佳方向，并且指示UE的UE最好的方向）

- **P-1**：用于在不同**TRP Tx**波束上启用**UE**测量以支持**TRP Tx**波束**/ UE Rx**波束的选择。对于**TRP**处的波束形成，其通常包括来自一组不同波束的帧内**/**帧间**TRP Tx**波束扫描。对于**UE**处的波束成形，其通常包括来自一组不同波束的**UE Rx**波束扫描。![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015102300814.png)
- **P-2**：用于在不同的**TRP Tx**波束上启用**UE**测量以可能改变帧间**/**帧内**TRP Tx**波束。从一组可能较小的光束进行光束细化而不是**P-1**。注意，**P-2**可以是**P-1**的特例。![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015102419137.png)
- **P3:**：用于在相同的**TRP Tx**波束上进行**UE**测量，以在**UE**使用波束成形的情况下改变**UE Rx**波束。

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015102512674.png)

### 5. CSI 介绍

#### 1. OFDM 正交频复用调制技术

> OFDM的基本思想是在频域内将给定信道分成许多正交子信道，在每个子信道上使用一个子载波进行调制，并且各子载波间并行传输。OFDM允许子载波频谱部分重叠，进而在支持OFDM技术的终端设备上同时获取多个子载波的信道状态信息。

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015205422865.png)

#### 2. CSI 状态信息

> CSI其实描述了无线信号在发射机和接收机之间的传播过程，其中包含了距离、散射、衰落等对信号的影响。

$$
Y=HX+N
$$

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015205624391.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015205747638.png)

### 6. Music Algorithm

> 空间谱估计是阵列信号处理中很重要的一部分，而空间谱估计的一个主要内容就是<font color=red>估计空间信号源的方向，即DOA(Direction of arrival)的估计</font>。MUSIC是一种有效的DOA估计方法。MUSIC(1969年提出)即多重信号分类(Multiple Signal Classification)算法，实现了想相待超分辨率侧向技术的飞跃，也促进了特征子空间算法的兴起。

> 通过对阵列接收数据的数学分解，将接收数据划分为两个相互正交的子空间：一个是与信号源的阵列流形一致的信号子空间，另一个是与信号子空间相交的噪声子空间。子空间分解类方法就是利用两个子空间的正交特性构造出“针状”空间谱峰，从而大大提高算法的分辨力。
>
> 使用条件：比如信号源互不相干，信号源数目小于阵列元素，噪声为加性高斯白噪声等。

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201013221707575.png)

### 7. Range-Doppler

- [没看懂](https://blog.csdn.net/qq_41248471/article/details/104276739)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210502202329.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210502203259.png)

- 接受到差频信号的第一个周期信号，复数表现形式：**B**为扫频带宽，**f0**为起始频率，**N**表示一个周期的采样点数，**R**和**v**为目标的距离和速度信息。

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210502202614.png)

- 快时间和慢时间维度接受信号差频信号:

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210502202727.png)

```matlab
%% generate receive signal

S1 = zeros(L,N);
for l = 1:L
    for n = 1:N
        S1(l,n) = exp(1i*2*pi*(((2*B*(tarR(1)+tarV(1)*T*l)/(c*T)+(2*f0*tarV(1))/c)*T/N*n+((2*f0)*(tarR(1)+tarV(1)*T*l))/c)));
    end
end

S2 = zeros(L,N);
for l = 1:L
    for n = 1:N
        S2(l,n) = exp(1i*2*pi*(((2*B*(tarR(2)+tarV(2)*T*l)/(c*T)+(2*f0*tarV(2))/c)*T/N*n+((2*f0)*(tarR(2)+tarV(2)*T*l))/c)));
    end
end

sigReceive = S1+S2;
```

- 峰值与位置、速度转化关系

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210502202923.png)

```matlab
%% range fft processing

sigRfft = zeros(L,NumRFFT);
for ii = 1:L
    sigRfft(ii,:) = fft(sigRWin(ii,:),NumRFFT);
end
%% doppler fft processing

sigDfft = zeros(NumDFFT,NumRFFT);
for ii = 1:NumRFFT
    sigDfft(:,ii) = fft(sigDWin(:,ii),NumDFFT);
end
tarR = [50; 90];                 % Target range
tarV = [3; 20];                  % Target velocity
```

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210502203112.png)

```python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from mpl_toolkits.mplot3d import Axes3D

# parameters setting

B = 135e6  # Sweep Bandwidth
T = 36.5e-6  # Sweep Time
N = 512  # Sample Length
L = 128  # Chirp Total
c = 3e8  # Speed of Light
f0 = 76.5e9  # Start Frequency
NumRangeFFT = 512  # Range FFT Length
NumDopplerFFT = 128  # Doppler FFT Length
rangeRes = c/2/B  # Range Resolution
velRes = c/2/f0/T/NumDopplerFFT  # Velocity Resolution
maxRange = rangeRes * NumRangeFFT/2  # Max Range
maxVel = velRes * NumDopplerFFT/2  # Max Velocity
tarR = [50, 90]  # Target Range
tarV = [3, 20]  # Target Velocity

# generate receive signal

S1 = np.zeros((L, N), dtype=complex)
for l in range(0, L):
    for n in range(0, N):
        S1[l][n] = np.exp(np.complex(0, 1) * 2 * np.pi * (((2 * B * (tarR[0] + tarV[0] * T * l))/(c * T) + (2 * f0 * tarV[0])/c) * (T/N) * n + (2 * f0 * (tarR[0] + tarV[0] * T * l))/c))

S2 = np.zeros((L, N), dtype=complex)
for l in range(0, L):
    for n in range(0, N):
        S2[l][n] = np.exp(np.complex(0, 1) * 2 * np.pi * (((2 * B * (tarR[1] + tarV[1] * T * l))/(c * T) + (2 * f0 * tarV[1])/c) * (T/N) * n + (2 * f0 * (tarR[1] + tarV[1] * T * l))/c))

sigReceive = S1 + S2

# range win processing

sigRangeWin = np.zeros((L, N), dtype=complex)
for l in range(0, L):
    sigRangeWin[l] = sp.multiply(sigReceive[l], sp.hamming(N).T)

# range fft processing

sigRangeFFT = np.zeros((L, N), dtype=complex)
for l in range(0, L):
    sigRangeFFT[l] = np.fft.fft(sigRangeWin[l], NumRangeFFT)

# doppler win processing

sigDopplerWin = np.zeros((L, N), dtype=complex)
for n in range(0, N):
    sigDopplerWin[:, n] = sp.multiply(sigRangeFFT[:, n], sp.hamming(L).T)

# doppler fft processing

sigDopplerFFT = np.zeros((L, N), dtype=complex)
for n in range(0, N):
    sigDopplerFFT[:, n] = np.fft.fft(sigDopplerWin[:, n], NumDopplerFFT)
```

### 8. 学习链接

- https://zhuanlan.zhihu.com/p/243364504
- https://zhuanlan.zhihu.com/p/141475685
- https://zhuanlan.zhihu.com/p/68667697
- https://charlesliuyx.github.io/2018/02/18/%E3%80%90%E7%9B%B4%E8%A7%82%E8%AF%A6%E8%A7%A3%E3%80%91%E8%AE%A9%E4%BD%A0%E6%B0%B8%E8%BF%9C%E5%BF%98%E4%B8%8D%E4%BA%86%E7%9A%84%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2%E8%A7%A3%E6%9E%90/#%E5%A3%B0%E9%9F%B3%E7%9A%84%E8%A1%A8%E7%A4%BA  
- [TI Board](https://training.eeworld.com.cn/TI/video/10162)

