---
title: DeviceSurvey
date: 2020-11-19 16:00:04
author: liudongdong1
img: https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124211750356.png
cover: false
categories: AIOT
tags:
  - mmwave
---

> Millimeter wave (mmWave) is a special class of radar technology that uses shortwavelength electromagnetic waves. Radar systems transmit electromagnetic wave signals that objects in their path then reflect. By capturing the reflected signal, a radar system can determine the `range, velocity and angle of the objects`. operating at `76–81 GHz` (with a corresponding wavelength of about `4 mm`

### 0. [mmWave](https://mp.weixin.qq.com/s/9LlyFbDhhklXEjOM9QHCRQ)

![image-20210430193129883](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210430193129883.png)

> Wei T, Zhang X. mtrack: High-precision passive tracking using millimeter wave radios[C]//Proceedings of the 21st Annual International Conference on Mobile Computing and Networking. 2015: 117-129.

- mTrack: 
  - record hand-writing trace from mTrack;
  - export and control mouse of a PC
  - Myscript styles for word detection

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210430193735.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210826191314733.png)

- E-Mi: 
  - model the environment as a sparse set of geometrical structures;
  - reconstruct the structure by tracing back the invisible propagation paths;
    - recover geometries of each path: AoA, AoD, length;
  - search for best topology to achieve best covery;

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210430193900.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210430194109.png)

- mmWave Imaging:
  - estimating object distance, curvature, boundary, and surface material;
    - fix Tx, while moving Rx to different locations; both using single-beam;
    - use reflected RSS patterns to distinguish object geometries/materials;
  - UIysses: leveraging beamforming to improve signal diversity;
    - moving co-located Tx/Rx following predefined trajectory;

![](https://gitee.com/github-25970295/blogImage/raw/master/img/20210430194534.png)

### 1. DCA1000EVM

> The DCA1000 evaluation module (EVM) provides `real-time data capture and streaming` for two- and four-lane low-voltage differential signaling (LVDS) traffic from TI AWR and IWR radar sensor EVMs. The data can be streamed out via `1-Gbps Ethernet` in real time to a PC running the `MMWAVE-STUDIO tool` for capture, visualization, and then can be passed to an application of choice for data processing and algorithm development. The DCA1000EVM is a `capture card for interfacing with Texas Instrument’s 77GHz xWR1xxx EVM` that enables users to stream the ADC data over Ethernet. This design is based on Lattice FPGA LFE5UM85F-8BG381I with DDR3L.
>
> - Supports `lab and mobile` collection scenarios
> - Captures LVDS data from `AWR/IWR` radar sensors
> - Streams output in real time through 1-Gbps Ethernet
> - Controlled via `onboard switches or GUI/library`

#### 1.1. LVDS over Ethernet streaming

- **Raw mode:** all LVDS data is captured and streamed over ethernet;
- **Data separated mode:** add specific headers to different data types; FPGA separates out different data types based on the header and streams it over ethernet interface;

![Function block diagram](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124222514337.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124222957554.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210628154716896.png)

- The DCA1000EVM should be `connected to TI's xWR1xxx EVM` through a 60-pin HD connector by using a 60-pin Samtec ribbon cable
- The DCA1000EVM should be `connected to a PC through a USB cable (J1-Radar FTDI) for configuring the xWR1xxx EVM if the mmWave Studio is used to configure the radar device`. If an embedded application is used to configure the xWR1xxx EVM, then this is not required.

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124221913724.png)

### 2. *IW  mmSensor

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124213955559.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124220548701.png)

#### 2.1. IWR1843

> The IWR1843 is an ideal solution for `low-power, self-monitored, ultra-accurate radar systems` in industrial applications, such as, `building automation, factory automation, drones, material handling, traffic monitoring, and surveillance`. Contains a TI high-performance `C674x DSP` for the radar signal processing. The device includes an `ARM R4F-based processor subsystem`, which is responsible for `front-end configuration, control, and calibration`. 

![IWR1843](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124214058201.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124214846565.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210628155422935.png)

- **Transmit Subsystem:** 
  -  three parallel transmit chains, each with independent phase and amplitude control;
- **Receive Subsystem:**
  - A single receive channel consists of an `LNA, mixer, IF filtering, A2D conversion, and decimation`. All four receive channels can be operational at the same time an individual power-down option is also available for system optimization.
  - complex baseband architecture, which uses quadrature mixer and dual IF and ADC chains to provide complex I and Q outputs for each receiver channel.

### 3. Tools

- Models:

  - [IWR1843 BSDL model](http://www.ti.com/lit/zip/SWRM048)  `Boundary scan database of testable input and output pins` for IEEE 1149.1 of the specific device.

  - [IWR1843 IBIS model](http://www.ti.com/lit/zip/SWRM047)    `IO buffer information model for the IO buffers of the devic`e. For simulation on a circuit board, see IBIS Open Forum.

- Tools:

  - [UniFlash Standalone Flash Tool](http://www.ti.com/tool/UNIFLASH):  program on-chip flash memory through a GUI, command line, or scripting interface.
  - [Code Composer Studio™ (CCS) Integrated Development Environment (IDE)](http://www.ti.com/tool/ccstudio):  develop and debug embedded applications. It includes an optimizing C/C++ compiler, source code editor, project build environment, debugger, profiler, and many other features.
  - [some experiment and labs](http://dev.ti.com/tirex/explore/node?node=AE0hA69g.mclu0y.xMWklg__VLyFKFf__LATEST)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201125122221538.png)

#### .1. mmWave Studio GUI

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210826192051238.png)

### 4. Application

- Liquid and solid level sensing;
- industrial proximity sensing, non-contact sensing for security, traffic monitoring, industrial transportation;
- sensor fusion of camera and radar instruments for security, factory automation, robotics;
- sensor fusion of camera and radar instruments for object identification, manipulation, and flight avoidance for security, robotics, material handling or drone devices;
- people counting;
- gesturing;
- motion detection;

#### 4.1. Automotive mmWave radar sensors 

##### 1. Front Long range radar

> achieve both `superior angular and distance resolution` at `short ranges over a wide field of view` while `extending out to long distances`. Relying on other optical sensors may be challenging in certain weather and visibility conditions. Smoke, fog, bad weather, and light and dark contrasts are challenging visibility conditions that can inhibit optical passive and active sensors such as cameras and LIDAR, which may potentially fail to identify a target. TI mmWave sensors, however, maintain robust performance `despite challenging weather and visibility conditions`.

##### 2. [Ultra short range radar](blob:https://www.ti.com/a649951c-4fee-4356-957e-e24b6f6c58eb)

> mmWave sensors for low-power, self-monitored, ultra-accurate radar systems in the automotive space.

##### 3. Medium/short range radar

> allow `estimation and tracking of the position and velocity of objects` and can be `multi-mode for objects at a distance and close-by`.

##### 4. Driver vital sign monitoring

> measuring `driver vital signs`, such as `heart rate and breathing rate`. This information could enable applications to `detect the fatigue state or sleepiness state` of a driver.

##### 5. Obstacle detection sensor

> `detect obstacles when parking or opening doors`.

##### 6. Vehicle occupant detection

> TI’s scalable 60GHz and 77GHz single-chip mmWave sensors enable `robust detection of occupants (adults, children, pets) inside of a car` for applications including `child presence detection, seat belt reminder, and more`.

#### 4.2. Industrial

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201125112702533.png)

- [Smart/Automatic door openers Industrial sensor for measuring range, velocity, and angle](http://www.ti.com/sensors/mmwave/iwr/applications/automated-doors-gates.html)
- [Tank level probing radar](http://www.ti.com/sensors/mmwave/iwr/applications/level-transmitter.html)
- [Displacement sensing](http://www.ti.com/sensors/mmwave/iwr/applications/level-transmitter.html)
- [Field transmitters](http://www.ti.com/sensors/mmwave/iwr/applications/level-transmitter.html)
- [Traffic monitoring](http://www.ti.com/sensors/mmwave/iwr/applications/radar-for-transport.html)
- [Proximity sensing](http://www.ti.com/sensors/mmwave/iwr/applications/safety-guards.html)
- [Security and surveillance](http://www.ti.com/sensors/mmwave/iwr/applications/building-automation.html)
- [Factory automation safety guards](http://www.ti.com/sensors/mmwave/iwr/applications/safety-guards.html)
- [People counting](http://www.ti.com/sensors/mmwave/iwr/applications/building-automation.html)
- [Motion detection](http://www.ti.com/sensors/mmwave/iwr/applications/building-automation.html)

### 5. Background

#### 5.1. LVDS

> LVDS（Low-Voltage Differential Signaling ,低电压差分信号）是美国国家半导体（National Semiconductor, NS，现TI）于1994年提出的一种`信号传输模式的电平标准`，它采用`极低的电压摆幅高速差动传输数据`，可以实现`点对点或一点对多点`的连接，具有`低功耗、低误码率、低串扰和低辐射`等优点，已经被广泛应用于`串行高速数据通讯`场合当，如高速背板、电缆和板到板数据传输与时钟分配，以及单个PCB内的通信链路。
>
> 差分信号`有别于单端信号一根信号线传输信号然后参考GND作为高(H)、低（L）逻辑电平的参考并作为镜像流量路径的做法`，差分传输`在两根传输线上都传输信号`，这两个信号的`振幅相等，相位相差180度，极性相反，互为耦合`。
>
> - 很容易地识别小信号;
> - 对外部电磁干扰(EMI)是高度免疫的;
> - 降低供电电压不仅减少了高密度集成电路的功率消耗，而且减少了芯片内部的散热，有助于提高集成度。LVDS减少供电电压和逻辑电压摆幅，降低了功耗。

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124213059569.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124213109265.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201124212942225.png)

### 6. 学习资源

- https://zhuanlan.zhihu.com/p/94470041
- [IWR1843 document](https://www.ti.com/document-viewer/IWR1843/datasheet/tools-and-software-x2434#x2434)
- 淘宝购买链接：
  - [DCA1000EVM TI 雷达感应应用实时数据捕捉适配器评估模块开发工具](https://detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.4.343d7484FUcozs&id=610896384431)  4790
  - [IWR1843BOOST TI 76GHz至81GHz工业雷达传感器评估模块原厂原装](https://detail.tmall.com/item.htm?id=611642691580)    2790
- [Texas 购买链接](https://www.ti.com/product/IWR1843#design-development##hardware-development)
- [DCA1000 Quik tutorial](https://www.ti.com/lit/ml/spruik7/spruik7.pdf?ts=1606224790990&ref_url=https%253A%252F%252Fwww.ti.com%252Ftool%252FDCA1000EVM)
- [mmWave Studio user guide](http://www.ti.com/lit/pdf/SWRU529)
- [Sensors overview and Relative Application](https://www.ti.com/sensors/mmwave-radar/automotive/overview.html)
- [Fundamation of mmwave](https://www.ti.com/lit/wp/spyy005a/spyy005a.pdf?ts=1606269600853&ref_url=https%253A%252F%252Fwww.ti.com%252Fsensors%252Fmmwave-radar%252Findustrial%252Fapplications%252Fapplications.html)
- [mmWave Radar Sensors: Object Versus Range](https://www.ti.com/lit/an/swra593/swra593.pdf?ts=1606230692721&ref_url=https%253A%252F%252Fwww.ti.com%252Fsensors%252Fmmwave-radar%252Findustrial%252Fapplications%252Fapplications.html)
- project: https://github.com/vilari-mickopf/mmwave-gesture-recognition

> Swipe Up,Swipe Down, spin cw, spin ccw, letter z, x, s

- mmwave SDK: https://github.com/bigheadG/mmWave
- mmwave beanforming: https://github.com/gante/mmWave-localization-learning#papers
- [DCA1000_Quick_Start_Guide.pdf](https://software-dl.ti.com/ra-processors/esd/MMWAVE-STUDIO/02_01_01_00/exports/DCA1000_Quick_Start_Guide.pdf)

