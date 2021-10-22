---
title: zoomFFT
date: 2021-07-4 16:00:04
author: liudongdong1
img:  https://cdn.stocksnap.io/img-thumbs/280h/butterfly-insect_QHJQCSOGES.jpg
cover: false
categories: AIOT
tags:
  - mmwave
  - signal
---

> 1. 移频 （将选带的中心频率移动到零频）
> 2. 数字低通滤波器 （防止频率混叠）
> 3. 重新采样 （将采样的数据再次间隔采样，间隔的数据取决于分析的带宽，就是放大倍数）
> 4. 复FFT （由于经过了移频，所以数据不是实数了）
> 5. 频率调整 （将负半轴的频率成分移到正半轴）

### 1. 栅栏效应

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901135244708.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901135301685.png)

#### .1.复调制移频

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901135356619.png)

#### .2. 低通滤波

为了`保证重新采样后的信号在频谱分析时不发生频谱混叠`，需进行抗混叠滤波，滤出需要分析的频段信号，则数字低通滤波器的截止频率 f c ≤ f s / 2 D.

#### .3. 重新抽样

信号经过移频、低通滤波后，分析信号点数变少，再以较低的采样频率进行重新采样，在`通过补零保证相同的采样点数时，样本的总长度加大，频谱的分辨率也就得到了提高。`
设原采样频率为 f s,采样点数为N，则频率分辨率为f s / N ，现重采样频率为f s / D，当采样点数仍是N时，其分辨率为f s / ( D ∗ N )，分辨率提高了D 倍。这样就在原采样频率不变的情况下得到了更高的频率分辨率。

#### .4. 复数FFT

重新采样后的信号实部和虚部是分开的，需要对信号进行N点复FFT，从而得出N NN条谱线，此时分辨率为Δ f ′ = f s ′ / N = f s / N D = Δ f / D，可见分辨率提高了D倍。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901135843376.png)

### 2. matlab code

```matlab
clear;
close all;
clc;
fs=1000;   %采样频率
N=2048; %傅里叶变换点数
D=50; %细化倍数
M=200; %滤波器阶数

t=(0:N*D+2*M)/fs; %时间轴
x=4*sin(2*pi*166.4*t)+2*sin(2*pi*165*t+pi/6)... +0.6*randn(1,N*D+2*M+1);  %信号

xf=fft(x,N); %傅里叶变换
xf=abs(xf(1:N/2))/N*2;
subplot(211);
plot((0:N/2-1)*fs/N,xf);
axis([163.5 169 0 4])
grid on
xlabel('f/Hz');ylabel('Amplitude')
title('直接进行傅里叶变换结果')
fe=167; %中心频率

k=1:M; w=0.5+0.5*cos(pi*k/M); %Hanning函数

fl=max(fe-fs/(4*D),-fs/2.2); %频率下限
fh=min(fe+fs/(4*D),fs/2.2); %频率上限

yf=D*fl; 
df=fs/D/N; %分辨率
f=fl:df:fl+(N/2-1)*df;
xz=zeros(1,N/2);
wl=2*pi*fl/fs; %归一化角频率
wh=2*pi*fh/fs;
hr(1)=(wl-wh)/pi;
hr(2:M+1)=(sin(wl*k)-sin(wh*k))./(pi*k).*w;
hi(1)=0;
hi(2:M+1)=(cos(wl*k)-cos(wh*k))./(pi*k).*w;

p=0:N-1;
w=0.5-0.5*cos(2*pi*p/N);
xrz=zeros(1,N/2);
xiz=zeros(1,N/2);
L=10;   %循环次数
for i=1:L for k=1:N kk=(k-1)*D+M; xrz(k)=x(kk+1)*hr(1)+sum(hr(2:M+1).*(x(kk+2:kk+M+1)+x(kk:-1:kk-M+1))); xiz(k)=x(kk+1)*hi(1)+sum(hi(2:M+1).*(x(kk+2:kk+M+1)-x(kk:-1:kk-M+1))); end xzt=(xrz+1j*xiz).*exp(-1j*2*pi*(0:N-1)*yf/fs); xzt=xzt.*w; xzt=xzt-sum(xzt)/N; xzt=fft(xzt); xz=xz+(abs(xzt(1:N/2))/N*2).^2;
end
xz=(xz./L).^0.5;
subplot(212);
plot(f,xz);
axis([163.5 169 0 4])
grid on
xlabel('f(Hz)');ylabel('Amplitude')
title('Zoom-FFT细化后的频谱')
```

### 3. python code

```python
import numpy as np
from matplotlib import pyplot as plt
from numpy import pi
from numpy.fft import fft, fftfreq, fftshift
from scipy import signal
import logging
import sys


class ZoomFFT:
    """This class is an implementation of the Zoom Fast Fourier Transform (ZoomFFT).

    The zoom FFT (Fast Fourier Transform) is a signal processing technique used to 
    analyse a portion of a spectrum at high resolution. The steps to apply the zoom 
    FFT to this region are as follows:

    1. Frequency translate to shift the frequency range of interest down to near 
       0 Hz (DC)
    2. Low pass filter to prevent aliasing when subsequently sampled at a lower 
       sample rate
    3. Re-sample at a lower rate
    4. FFT the re-sampled data (Multiple blocks of data are needed to have an FFT of 
       the same length)

    The resulting spectrum will now have a much smaller resolution bandwidth, compared
    to an FFT of non-translated data.

    """

    def __init__(self, low_freq, high_freq, fs, signal=None):
        """Initialize the ZoomFFT class.

        Args:
            low_freq (int): Lower frequency limit
            high_freq (int): Upper frequency limit
            fs (int): sampling Frequency
            signal (np.ndarray): Signal to perform the ZoomFFT on

        """
        self.low_freq = low_freq
        self.high_freq = high_freq
        self.fs = fs

        if (low_freq < 0) or (high_freq > fs) or ((high_freq - low_freq) > fs):
            raise Exception("invalid inputs. Program Terminated! ")

        if signal:
            self.signal = signal
            self.length = len(signal)
        else:
            # the default now is a sine signal, for demo purpose
            pass

    def set_signal(self, signal):
        """Sets given signal as a member variable of the class.

        e.g. ZoomFFT.create_signal(generate_sinewave(a, b, c) + generate_sinewave(d, e, f))

        Args:
            signal (np.ndarray): Signal to perform the ZoomFFT on

        """
        self.signal = signal

    def sinewave(self, f, length, amplitude=1):
        """Generates a sine wave which could be used as a part of the signal. 

        Args: 
            f (int): Frequency of the sine wave
            length (int): Number of data points in the sine wave
            amplitude (int): Amplitude of the sine wave

        Returns:
            x (np.ndarray): Generated sine wave with the given parameters.
        """
        self.length = length
        x = amplitude * np.sin(2 * pi * f / self.fs * np.arange(length))
        return x

    def compute_fft(self):
        """Computes the Fast Fourier Transform (FFT) of the signal.

        Returns:
            X (np.ndarray): A frequency-shifted, unscaled, FFT of the signal.
        """
        try:
            X = fft(self.signal)
            X = np.abs(fftshift(X))  # unscaled
            return X
        except NameError:
            print("signal not defined. Program terminated!")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def plot_fft(self, d=None):
        """Plots the Fast Fourier Transform (FFT) of the signal.

        Args:
            d (int): Sample spacing (inverse of the sampling rate)

        """
        try:
            d = 1 / self.fs if d is None else d
            X = self.compute_fft()
            freq = fftfreq(self.length, d)

            self.original_sample_range = 1 / (self.length * d)

            fig1, ax1 = plt.subplots()
            ax1.stem(fftshift(freq), X / self.length)
            ax1.set_xlabel('Frequency (Hz)', fontsize=12)
            ax1.set_ylabel('Magnitude', fontsize=12)
            ax1.set_title('FFT Two-sided spectrum', fontsize=12)
            ax1.grid()

            plt.show()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def compute_zoomfft(self, resample_number=None):
        """Computes the Zoom Fast Fourier Transform (ZoomFFT) of the signal.

        Args:
            resample_number (int): The number of samples in the resampled signal.

        Returns:
            Xd (np.ndarray): A frequency-shifted, unscaled, ZoomFFT of the signal.
            bw_factor (int): Bandwidth factor
            fftlen (int): Length of the ZoomFFT output
            Ld (int): for internal use
            F (int): for internal use
        """
        try:
            bw_of_interest = self.high_freq - self.low_freq

            if self.length % bw_of_interest != 0:
                logging.warning("length of signal should be divisible by bw_of_interest. Zoom FFT Spectrum may distort!")
                input("Press Enter to continue...")

            fc = (self.low_freq + self.high_freq) / 2
            bw_factor = np.floor(self.fs / bw_of_interest).astype(np.uint8)

            # mix the signal down to DC, and filter it through the FIR decimator
            ind_vect = np.arange(self.length)
            y = self.signal * np.exp(-1j * 2 * pi * ind_vect * fc / self.fs)

            resample_number = bw_of_interest / self.original_sample_range if resample_number is None else resample_number

            resample_range = bw_of_interest / resample_number

            if resample_range != self.original_sample_range:
                logging.warning("resample resolution != original sample resolution. Zoom FFT Spectrum may distort!")
                input("Press Enter to continue...")

            xd = signal.resample(y, np.int(resample_number))

            fftlen = len(xd)
            Xd = fft(xd)
            Xd = np.abs(fftshift(Xd))  # unscaled

            Ld = self.length / bw_factor
            fsd = self.fs / bw_factor
            F = fc + fsd / fftlen * np.arange(fftlen) - fsd / 2
            return Xd, bw_factor, fftlen, Ld, F
        except NameError:
            print("signal not defined. Program terminated!")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def plot_zoomfft(self, resample_number=None):
        """Plots the Zoom Fast Fourier Transform (ZoomFFT) of the signal.

        Args:
            resample_number (int): The number of samples in the resampled signal.
            
        """
        try:
            bw_of_interest = self.high_freq - self.low_freq
            resample_number = bw_of_interest / self.original_sample_range if resample_number is None else resample_number
            Xd, bw_factor, fftlen, Ld, F = self.compute_zoomfft(resample_number)

            fig1, ax1 = plt.subplots()

            ax1.stem(F, Xd / Ld, linefmt='C1-.', markerfmt='C1s')
            ax1.grid()
            ax1.set_xlabel('Frequency (Hz)', fontsize=12)
            ax1.set_ylabel('Magnitude', fontsize=12)
            ax1.set_title('Zoom FFT Spectrum. Mixer Approach.', fontsize=12)
            fig1.subplots_adjust(hspace=0.35)
            plt.show()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
```

