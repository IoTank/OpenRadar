---
title: TIDeviceCoding
date: 2021-07-1 16:00:04
author: liudongdong1
img:  https://cdn.stocksnap.io/img-thumbs/280h/bird-perched_RDHWPJKENF.jpg
cover: false
categories: AIOT
tags:
  - mmwave
---

> Since each of the samples are taken at equally spaced time intervals, we have a time log of what happened during the chirp. `Every sample is a complex number`, meaning we have captured some `magnitude of power as well as the phase` of the wave at that time. So, our object will theoretically appear as an increase in power in our samples. On the other hand, we can use the distinct phases of each sample to obtain distance. ` (Frame, chirp,virtual antennas(tx*rx),Datasample)`
>
> - Power - $P = \sqrt{I^2+Q^2}$
> - Phase - $\angle = \arctan{(\frac{I}{Q})}$
>
> ($I$​​​=Imaginary Component $Q$​​​=Real Component)
>
> - `rangeFFT （对一个chirp 的sample）`和`dopplerFFT（对一个Frame的不同chirp) `，`AzimuthRRF(对virtual antenna 维度)`

![chirp data](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901095219270.png)

### 1. Profile

#### .1. 配置参数

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901170138432.png)

##### .1. start frequency

##### .2. frequency slope

##### .3. Idle time

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901170333232.png)

##### .4. ADC start time(不懂)

- `Synthesizer PLL ramp-up settling time, which is a function of ramp slope`
- `HPF step response settling, which is a function of HPF corner frequencies`
- `IF/DFE LPF settling time, which is a function of DFE output mode and sampling rate`

##### .5. Ramp end time

`The ramp end time is the sum of (a) the ADC start time, (b) the ADC sampling time and (c) the excess ramping time at the end of the ramp.  `

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901170741261.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901170108543.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901164155446.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901164232154.png)

#### .2. procedure

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901171106832.png)

```python
# Imports
import numpy as np
import matplotlib.pyplot as plt
```

### 1. 距离计算

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901100023673.png)

#### 1. Range FFT

> The first step to `obtaining range is by performing an FFT across our ADC samples for a single chirp`. This unfortunately does not leave you with a single range. Instead, we obtain multiple "range bins". These are exactly what they sound like, bins that store the information for various ranges.

```python
# Read in chirp data
adc_samples = np.loadtxt('../assets/chirp.txt', dtype=np.complex_)
print("datainformation:",type(adc_samples),adc_samples.shape,"data[0]",adc_samples[0]) #<class 'numpy.ndarray'> (128,)data[0] (19+65375j)
# Manually cast to signed ints
adc_samples.real = adc_samples.real.astype(np.int16)
adc_samples.imag = adc_samples.imag.astype(np.int16)
print("adc_samples:",type(adc_samples),adc_samples.shape,"data[0]",adc_samples[0])
# Take a FFT across ADC samples
range_bins = np.fft.fft(adc_samples)  #<class 'numpy.ndarray'> (128,) data[0] (19-161j)
print("range_bins:",type(range_bins),range_bins.shape,"data[0]",range_bins[0])#(128,) data[0] (1212-87j)
# Plot the magnitudes of the range bins
plt.plot(np.abs(range_bins)) 
plt.xlabel('Range Bins')
plt.ylabel('Reflected Power')
plt.title('Interpreting a Single Chirp')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901095419698.png)

#### 2. 单位转化

##### .1. 原理推导

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901164424552.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901164659831.png)

> complex 2x and real smapling modes: IF=0.9*(ADC_sampling)/2

`the objects at some range bin index are indeed farther than the objects at the previous index` and closer than the objects in the next index. That's probably what you didn't want to hear however.

- $f = \frac{S2 d}{c}$ - The *IF signal* frequency produced by a single object at distance $d$ (where the object appears in the frequency spectrum after the range FFT) 
    - $f$ - Frequency
    - $S$ - Frequency slope of the signal emitted by the chirp
    - $d$ - Distance relative to the radar
    - $c$ - Speed of light <br> 
- $\Delta f > \frac{1}{T}$ - The minimum separation needed in the frequency spectrum to be resolved by the radar <br>
    - $T$ - Sampling period

Looking at the first equation and we can see there is a direct relationship between $f$ and $d$...

- $f = \frac{S2 d}{c} \Rightarrow \Delta f = \frac{S2 \Delta d}{c}$

So now we have two separate equations that define $\Delta f$. Substitution can be now used.

- $\frac{S2 \Delta d}{c} = \Delta f \gt \frac{1}{T}$
- $\frac{S2 \Delta d}{c} \gt \frac{1}{T}$

Finally, we can solve for $\Delta d$, or the range resolution we can achieve.

- $\Delta d \gt \frac{c}{2} \cdot \frac{1}{ST}$

Since we know $S$ is in some unit of frequency over time, we can simplify $ST$ to just $B$, or the bandwidth of chirp.

- $\Delta d > \frac{c}{2B}$

In other words,` the range resolution is only dependent on how large a bandwidth the chirp has`. Let's see what information we have to use to try and find this range resolution.

Not exactly what we wanted, but the only thing we're missing is our bandwidth $B$. We can still use these parameters to find bandwidth since it is just the span of frequency of the chirp. So, we just need to calculate how much of a frequency span the chirp takes. Ignoring converting units for now, this should be our equation:

- $B = S \cdot \frac{N}{F_s}$
    - $S$ - Frequency slope (frequency/time)
    - $N$ - Number of ADC samples (samples)
    - $F_s$ - Frequency at which we sample ADC samples (samples / time)

##### .2. 计算代码

```python
# Data sampling configuration
c = 3e8 # Speed of light (m/s)
sample_rate = 2500 # Rate at which the radar samples from ADC (ksps - kilosamples per second)
freq_slope = 60 # Frequency slope of the chirp (MHz/us)
adc_samples = 128 # Number of samples from a single chirpb

# Calculating bandwidth of the chirp, accounting for unit conversion
chirp_bandwidth = (freq_slope * 1e12 * adc_samples) / (sample_rate * 1e3)

# Using our derived equation for range resolution
range_res = c / (2 * chirp_bandwidth)
print(f'Range Resolution: {range_res} [meters]')

# Apply the range resolution factor to the range indices
ranges = np.arange(adc_samples) * range_res
powers = np.abs(range_bins)

# Now we can plot again with an x-axis that makes sense
plt.plot(ranges, powers)
plt.xlabel('Range (meters)')
plt.ylabel('Reflected Power')
plt.title('Interpreting a Single Chirp')
plt.show()

chirp_bandwidth
print(ranges)
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901095734148.png)

### 2. 速度计算

#### .1. Doppler Effect

> In addition to `multiple ADC samples`, we have `multiple chirps.` For an object at range 𝑥 from the radar, when we receive the respective ADC sample, the product will be a complex number with some phase. If the object is moving away from the radar, the respective ADC sample of the second chirp will come in at a very slightly delayed time. This is because the object also moved slightly away in that miniscule amount of time. Althought this movement is miniscule, `the change in phase of the wave can be clearly seen`.

$$
f' = \frac{v+v_0}{v-v_s}f
$$

#### .2. Range FFT

```python
# Read in frame data
frame = np.load('../assets/simple_frame_1.npy')

# Manually cast to signed ints
frame.real = frame.real.astype(np.int16)
frame.imag = frame.imag.astype(np.int16)

# Meta data about the data
num_chirps = 128 # Number of chirps in the frame
num_samples = 128 # Number of ADC samples per chirp

range_plot = np.fft.fft(frame, axis=1)  # axis=1:按行计算
print("range infor:",type(range_plot),range_plot.shape)   #(128,128)
# Visualize Results
plt.imshow(np.abs(range_plot).T)
plt.ylabel('Range Bins')
plt.title('Interpreting a Single Frame - Range')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901101058961.png)

#### .3. Doppler FFT

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

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901101436884.png)

> That line in the `middle at doppler bin 64 is called zero doppler`, meaning everything along that line is `static/not moving relative to the radar`. This means everything to the `left (bins<64) is negative doppler, or moving towards the radar `and the opposite for the other half of the doppler bins.

- `rangeFFT （对一个chirp 的sample）`和`dopplerFFT（对一个Frame的不同chirp) `先后顺序影响不大；

```python
print("frame infor:",type(frame),frame.shape)  #frame infor: <class 'numpy.ndarray'> (128, 128)
# Range FFT -> Doppler FFT
range_bins = np.fft.fft(frame, axis=1)
fft_2d = np.fft.fft(range_bins, axis=0)

# Doppler FFT -> Range FFT
doppler_bins = np.fft.fft(frame, axis=0)
rfft_2d = np.fft.fft(doppler_bins, axis=1)

print('Max power difference: ', np.abs(fft_2d - rfft_2d).max())  #Max power difference:  5.64766185425834e-11
```

#### .4. 单位转化

##### .1. 原理推导

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901164949755.png)

All the units of the data we produced are of some type of "bin". Similarly to range resolution, we `have a doppler resolution aka velocity resolution`. 

- $\omega = \frac{4\pi vT_c}{\lambda}$ - Rotational frequency of phasor due to object moving at $v$ velocity
    - $v$ - Velocity
    - $T_c$ - Sampling period
    - $\lambda$ - Wavelength
- $\Delta\omega \gt \frac{2\pi}{N}$ - Minimum change in rotation of phasor to be resolved by radar
    - $N$​ - Number of sample points

##### .2. 计算代码

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

# Range resolution    ？？ 这里没有看懂
range_res = (c * sample_rate * 1e3) / (2 * freq_slope * 1e12 * adc_samples)
print(f'Range Resolution: {range_res} [meters/second]')  #Range Resolution: 0.048828125 [meters/second]

# Apply the range resolution factor to the range indices
ranges = np.arange(adc_samples) * range_res
```

```python
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

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901105825831.png)

### 3. 角度计算

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901111120724.png)

#### .1. Range FFT

```python
# Read in frame data
frame = np.load('../assets/doppler_example_1.npy')

# Manually cast to signed ints
frame.real = frame.real.astype(np.int16)
frame.imag = frame.imag.astype(np.int16)

print(f'Shape of frame: {frame.shape}')

# Meta data about the data
num_chirps = 128 # Number of chirps in the frame
num_samples = 128 # Number of ADC samples per chirp

num_tx = 2
num_rx = 4
num_vx = num_tx * num_rx # Number of virtual antennas
```

```python
range_plot = np.fft.fft(frame, axis=2)

# Visualize Results
plt.imshow(np.abs(range_plot.sum(1)).T)
plt.ylabel('Range Bins')
plt.title('Interpreting a Single Frame - Range')
plt.show()
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901111228073.png)

#### .2. Doppler FFT

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

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901111309395.png)

#### .3.  Azimuth FFT

```python
num_angle_bins = 64
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

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901111409348.png)

#### .4. 原理推导

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901165336582.png)

### 4. 相关知识

#### 1. FFT

> numpy.fft.**fft**(x, n = 10) 和 scipy.fftpack.fft(x, n = 10)
>
> - 第一个参数x表示输入的序列，
> - 第二个参数n制定FFT的点数，n值如果没有的话，那么就默认输入序列的个数为FFT的点数
> - 两者虽然相同，但是scipy.fftpack.fft的效率更高，推荐优先使用。
>
> numpy和scipy中都有**fftshift**，用于将FFT变换之后的频谱显示范围从[0, N]变为：[-N/2, N/2-1](N为偶数)         或者[-(N-1)/2, (N-1)/2](N为奇数)
>
> **fftfreq：**在画频谱图的时候，要给出横坐标的数字频率；scipy.fftpack.fftfreq(n, d=1.0)
>
> - 第一个参数n是FFT的点数，一般取FFT之后的数据的长度（size）
> - 第二个参数d是采样周期，其倒数就是采样频率Fs，即d=1/Fs

#### 2. resource

- [设备连接](https://blog.csdn.net/qq_40603614/article/details/112706620)