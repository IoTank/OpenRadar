---
title: mmPaperRecord
date: 2020-07-1 16:00:04
author: liudongdong1
img: https://gitee.com/github-25970295/blogImage/raw/master/img/snowdrop-flowers-spring-flower-plant-close-macro.jpg
cover: false
categories: AIOT
tags:
  - mmwave
---

### Authors:

- https://scholar.google.com/citations?hl=zh-CN&user=TvI47boAAAAJ&view_op=list_works&sortby=pubdate  
- https://scholar.google.com/citations?hl=en&user=c5yUtPsAAAAJ&view_op=list_works&sortby=pubdate  
- https://scholar.google.com/citations?hl=en&user=OxKLBqwAAAAJ&view_op=list_works&sortby=pubdate  
- https://scholar.google.com/citations?hl=en&user=q9llreMAAAAJ&view_op=list_works&sortby=pubdate  
- https://scholar.google.com/citations?hl=en&user=5-FDAmAAAAAJ&view_op=list_works&sortby=pubdate  
- https://scholar.google.com/citations?hl=en&user=OxKLBqwAAAAJ&view_op=list_works&sortby=pubdate

Application:[*vocalPrint_SenSys20.pdf](file:///D:/work_OneNote/OneDrive - tju.edu.cn/文档/work_组会比赛/mmwave/mmWave-sensing/papers/vocalPrint_SenSys20.pdf)

- mmWave-based human sensing: 
  - detects `minute variations` caused by human withoud body contact.  1,24;
  - `activity recognition`: 23, 32, 79;
  - `emotion recognition`: 78
  - `detection of biometrics`: 72,78s
    - 48 measure the `respiration and heart rates` 10m;
    - 34 `user authenticatio`n;
    - 33, 69 `voice-related information` to facilitate voice-user interface.

- Voice authentication:
  - based on the `distinction between human and loudspeaker` 58, 59;
  - `RF reflections` 41
  - `ultrasonic reflection` 76
  - `magnetic field from the loudspeaker` 10;
  - `pop music in human utterances` 67
  - `VAuth` 18 contact based sensors for voice authentication, `vocal resonance` 35.

Limitation:

- Long sensing distance:
  - distance increases, velocity resolution of the range profile degrade.	
  - by increase the bandwidth of IF signals in mmWave waveform design.
- Sensing orientation:
  - collect data covering different orientations,
  - using beam forms;

- Compatibility with IoT Devices:
  - high sampling rate produce massive data samples.
  - using high-speed DSP processors;

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210704155649955.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210704155706723.png)

### Security

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210704155730041.png)

### FineDisplacement Sensing

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210704155800494.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210704155818208.png)

### Tag for MMwave

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210704155843456.png)

### Tracking&Location

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210704155908981.png)

### Image

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210704155929043.png)

### MultiPerson

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210704155953025.png)

>Huang, Jui-Te, et al. "Cross-Modal Contrastive Learning of Representations for Navigation using Lightweight, Low-Cost Millimeter Wave Radar for Adverse Environmental Conditions." arXiv preprint arXiv:2101.03525 (2021).  [[pdf](chrome-extension://ikhdkkncnoglghljlkmcimlnlhkeamad/pdf-viewer/web/viewer.html?file=https%3A%2F%2Farxiv.org%2Fpdf%2F2101.03525v1.pdf)]  [[code](https://github.com/huangjuite/radar-navigation)]

------

# Paper: Navigation

<div align=center>
<br/>
<b>Cross-Modal Contrastive Learning of Representations for Navigation using Lightweight, Low-Cost Millimeter Wave Radar for Adverse Environmental Conditions</b>
</div>


#### Summary

1. 

#### Research Objective

  - **Application Area**:
- **Purpose**:  

#### Proble Statement

- 

previous work:

- 

#### Methods

- **Problem Formulation**:

- **system overview**:



【Qustion 1】

#### Evaluation

  - **Environment**:   
    - Dataset: 
- 

#### Conclusion

- 

#### Notes <font color=orange>去加强了解</font>

  - 

**level**: CCF_A
**author**: Chengkun Jiang;  Junchen Guo;  Yunhao Liu
**date**: 2020
**keyword**:

- mmwave, vibration detection

> Jiang, Chengkun, et al. "mmVib: micrometer-level vibration measurement with mmwave radar." *Proceedings of the 26th Annual International Conference on Mobile Computing and Networking*. 2020.

------

# Paper: mmVib

<div align=center>
<br/>
<b>mmVib: Micrometer-Level Vibration Measurement with
mmWave Radar</b>
</div>
#### Summary

1. propose MSC, that comprehensively describes the composition of the reflected mmWave signals. MSC captures the multi-frequency and multi-antenna properties of the reflected signal from the vibrating object in the multi-path rich environments;
2. the design of mmVib address critical challenges in achieving the micrometer-level accuracy:
   1. pinpoint the vibrating object in the mixed reflected signal;
   2. recovering the micrometer-level vibration under the influence of noise and other reflected signals;
   3. mmVib achieves 8.2% relative amplitude error and 0.5% relative frequency error in median. the median amplitude error is 3.4 um fo rthe 100um-amplitude vibration, reduce 80% amplitude error by 62.9% and 68.9% compared to existing two methods;

#### Research Objective

  - **Application Area**: vibration measurement for checking machinery health, identifying anomalies, and diagnosing faults.

**Previous work:**

- specialized sensors like piezoelectric sensors;
- optical devices like laser vibrometers;          high precision and accuracy but prohibitive cost in deployment and maintenance;
- **Wireless Methods:**    precision is limited due to the relatively long wavelengths;
  - acoustic signal 21, 31
  - RF signal  18,32, 36

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014175433699.png)

#### Methods

- **Prelimilary Knowledge and Phenomenon**:

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014193957186.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014194252167.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014194425898.png)

- **system overview**:

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014223723103.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014194946697.png)

#### Evaluation

  - **Environment**:   

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014195008409.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014195218753.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014195318337.png)

#### Conclusion

- 

#### Notes <font color=orange>去加强了解</font>

  - 7, 11, 16, 19, 23, 29, 33, 35, 37, 42  



**level**: CCF_A
**author**:  Baicheng Chen, Huining Li, Zhengxiong Li, Xingyu Chen, Chenhan Xu, Wenyao Xu
**date**: 2020 
**keyword**:

- Temperature wireless sense;

> Chen, Baicheng, et al. "ThermoWave: a new paradigm of wireless passive temperature monitoring via mmWave sensing." *Proceedings of the 26th Annual International Conference on Mobile Computing and Networking*. 2020.

------

# Paper: ThermoWave

<div align=center>
<br/>
<b>ThermoWave: a new paradigm of wireless passive temperature monitoring via mmWave sensing</b>
</div>

#### Summary

1. investigate the thermal scattering effect that causes a temperature-related frequency shift modulation in scattered RF signal, and study the mathematical model that captures and characterizes changes with low-cost and ecological cholesteryl materials;
2. based on the thermal scattering effect, the paper implement the Thermowave system:
   1. design a cholesteryl based ThermoTag as temperature sensing film or sticker that attaches to an object of interest;
   2. prototype a mmWave based ThermoScanner to interrogate and receive the thermal scattering response;
   3. a thermosense software to extract dot-wise temperature and thermal image from the thermal scatterign response;
3. evaluate the thermowave systems performance from following aspects:
   1. thermotag shape and size;
   2. different scanning distance, orientations, and occlusion conditions;
   3. real word scenario usage and some limitations;

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20201014163202825.png)

#### Research Objective

  - **Application Area**:  temperature monitor in temperature-sensitive products, including food and medicines to maintain best quality in storage and transportation;
- **Purpose**:  

#### Proble Statement

- **Thermal Scattering Effect for cholesteryI**: Cholesteryl material’s temperature dependent molecular alignment directly impacts the frequency of scattering response under the illumination of mmWave.

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014163522304.png)

> Thermal scattering responses from cholesteryl material show evident frequency shift in spectrum analysis. Compared to response at 70 °F, the frequency shifted response at 90 °F have a tone that is few kHz lower.

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014163604991.png)

previous work:

- **Wireless temperature sensors:**  high cost, harms environment and lacks thermal imaging capability;
- **Thermal imaging devices:** read temperature distribution across space in front of the sensor;   such mechanism fails to read temperature from target object with as little as a thin sheet of paper in between

#### Methods

- **system overview**:

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014163654706.png)

【**Thermodot sensing scheme**】using Empirical Wavelet Transform to perform frequency domain analysis by detecting local maximas in the wavelet spectrum.![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014164222264.png)

![Features](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014164418566.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014164831160.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014164855486.png)

**【Thermonet sensing scheme】**

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014165025479.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014165651094.png)

1. adopt STFT for transforming the thermal scattering response signal from one signal from one dimensional spectral-temporal function into a two dimensional spectral-image function;
2. in order to solve the spectrogram image to thermal imaging mapping problem, pixels in spectrogram image must be mapped to pixels in thermal image; mapping capture the general color to color relationship and the image structure to encapsulates the temperature distribution over the thermal image;

#### Evaluation

  - **Environment**:   

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014174100859.png)

- **Metrics**
  - **Structure Similarity Index:** ![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014172322644.png)
  - **Percentage accuracy：** counting the number of pixels in generated thermal image(I) that are with $\delta$ distance from ground truth thermal image(T) and divided by the total number of pixels in thermal image;
  - **Peak Signal to Noise Ratio:** to verify the estimated thermal image quality；![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014172121026.png)

![three typical regressor algorithm](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014170056205.png)

![different ThermoTag shapes](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014170131343.png)

![different ThermoTag sizes](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014170214870.png)

![Different Scanning Orientation](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014170818774.png)

![Sampling Rate Effect](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014170915988.png)

![Two Days Realworld test](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014171214317.png)

![Environment Inference](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201014171324164.png)

#### Notes <font color=orange>去加强了解</font>

  - 在信号处理部分，multipath 会产生影响吗，还是小波变换去除了这部分影响；
  - “Wavespy: Remote and through-wall screen attack via mmwave sensing,” in To appear in IEEE Symposium on Security and Privacy 2020, ser. S&P’20, 2020.
  - Waveear: Exploring a mmwave-based noise-resistant speech sensing for voiceuser interface,” in Proceedings of the 17th Annual International Conference on Mobile Systems, Applications, and Services, 2019, pp. 14–26.
  - u, “Ferrotag: A paper-based mmwave-scannable tagging infrastructure,” in To appear in Proceedings of the 17th ACM Conference on Embedded Networked Sensor Systems, ser. SenSys’19, 2019
  -  “Soli: Ubiquitous gesture sensing with millimeter wave radar,” ACM Transactions on Graphics (TOG), vol. 35, no. 4, p. 142, 2016.
  - , “E-eye: Hidden electronics recognition through mmwave nonlinear effects,” in Proceedings of the 16th ACM Conference on Embedded Networked Sensor Systems. ACM, 2018, pp. 68–81.

# Paper: 3D Location

>Pefkianakis I, Kim K H. Accurate 3d localization for 60 ghz networks[C]//Proceedings of the 16th ACM Conference on Embedded Networked Sensor Systems. 2018: 120-131. [[pdf](chrome-extension://ikhdkkncnoglghljlkmcimlnlhkeamad/pdf-viewer/web/viewer.html?file=https%3A%2F%2Fdl.acm.org%2Fdoi%2Fpdf%2F10.1145%2F3274783.3274852)]

# Paper:  MicroGestures on Augmented Objects

> Klen Čopič Pucihar, Christian Sandor, Matjaž Kljun, Wolfgang Huerst, Alexander Plopski, Takafumi Taketomi, Hirokazu Kato, Luis A. Leiva.  "The Missing Interface: MicroGestures on Augmented Objects" *Extended Abstracts of the 2019 CHI Conference on Human Factors in Computing Systems*, 2019.

#### **Relative**   

- **remote interaction**: 

  -  interaction is dislocated from the augmented object
  -  based on captured RGB or RGB-D data streams [13] （`ight`）
  -  `electric field sensing` for full-body gestures [2], fingertip tracking [8], audio-based doppler  shift sensing [7], and `capacitive sensing` [10] (*without light*)
  -  `acceleration-sensitive` finger rings [4] or a wristband device that recognizes hand gestures and forearm movements [10] (*wearables*)
- **direct interaction**:

  -  `interaction is performed on the augmented object`

  -  `multi-touch` interaction around small devices [1]

  -  `capacitive sensing` techniques enabling detection of touch events on humans, screens, liquids, and everyday objects [12]

  -  `electromyograpy(EMG)` systems that measure muscle tension [3]
 - **MICO-GESTURES ON AUGMENTED PHYSICAL OBJECTS**
   - Millimeter-wave radar sensing technology has recently shown promising results in the context of detecting micro-gestures [9, 15].
   - the Soli sensor has been shown to be successful at classifying everyday objects and materials [16–18]

**The missing interface problem** occurs when physical objects are augmented with digital elements, because those objects were never designed to incorporate digital content and thus they `do not provide a proper user interface` to allow for interaction.

#### Contribution

- explore the possibilities of a “Swiss Army knife”-like interface that would fill in the

  missing interface void

  - reviewing current approaches and similar interaction methods 

  - `proposing and evaluating a novel gesture detection system based on Google Soli’s millimeter wave radar sensing technology`

    ![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201126102434038.png)   

####  Experiment

- Google Soli’s millimeter wave radar:

  - the standard gesture detection pipeline proposed by Google Soli’s SDK

  - 9 built-in core features: `Acceleration, Energy Moving, Energy Total, Movement index,  Range, Spatial dispersion, Velocity, Velocity Dispersion` 

  - 4 meta-features: `mean, standard deviation, sum, and absolute sum`

  - logged sensor data at 100 Hz

  - Random Forest (RF, with forest size of 200 and depth of 10) and Support Vector Machine    (SVM, with RBF kernel and regularization)

  - 80/20 split of the data

  - RF outperforms

    ![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201126102453270.png)



# Paper. TARF

> Francesco Tonolini and Fadel Adib.  "Networking across Boundaries: Enabling Wireless Communication through the Water-Air Interface" *Proceedings of the 2018 Conference of the ACM Special Interest Group on Data Communication*, 2018.

#### **Relative**   

- **Underwater Communication**: 
  -  `SONAR systems`, which leverage sound and ultrasonic signals for submarine communications and for detecting icebergs and U-boats [28, 35]
  -  The US and Soviet navies developed `ELF (extremely low frequency) communication` systems which operate at `30-300 Hz` and are capable of communicating `across the air-water boundary` [9, 41]
  -  To overcome the water-air barrier, these systems rely on nodes that incorporate two communication modules: acoustic and RF [40, 41]
  -  optics [31, 55] and quantum entanglement [26]
- **Wireless Sensing**:
  -   sensing human locations, gestures, and vital signs [6, 7, 39]
  -   the radar community has explored wireless for `sensing coarse water surface levels` and `surface currents` [16]

#### Contribution

- TARF is the first communication technology leveraging sensing that enables a `deeply submerged underwater node to directly communicate with a compact airborne node`.

- `achieve standard underwater data rates` in scenarios where past technologies cannot establish any communication throughput

  ![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201126102528119.png)

#### Experiment

- an `underwater acoustic speaker as a transmitter` and an airborne millimeter wave `FMCW radar as a receiver`

  -  the OSD 75*W* Compact Subwoofer Amplififier [2] and the Pyle 300W Stereo Receiver [3]
  -  transmit signals over a bandwidth of 100Hz between 100Hz and 200Hz
  -  TARF’s transmitter encodes its data using OFDM modulation
  -  transmit 10 back-to-back OFDM symbols (two symbols act as a preamble and 8 as payload) in each experimental trial
  -  FMCW, the reference outputs a frequencyramp with a center frequency of 8.65*GHz* and a bandwidth of 500MHz
  -  enable transmitting and receiving an FMCW signal with a center frequency of 60GHz and a bandwidth of 3GHz
  -  an effective range resolution of 5 cm,  a phase sensitivity of 1.25rad/mm
  -  23 dBi horn antennas
  -  programmed our FMCW generator to sweep its bandwidth every 80μs
  -  USRP N210 software radio [5] equipped with an LFRX daughter board
  -  Ubuntu 16.04, TARF’s decoder in MATLAB

  - 500 experimental trials in total

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201126102631039.png)

-  four configurations: 

   - the first three employ uniform power distribution and modulation
     across all the OFDM subcarriers using BPSK, QPSK and
     16QAM. 

   - the final configuration incorporates TARF’s power
     allocation and rate adaptation schemes

**level**: 
**author**: Wang, Song, Jingqi Huang, and Xinyu Zhang
**date**: 
**keyword**:

- 

> Wang, Song, Jingqi Huang, and Xinyu Zhang. "Demystifying millimeter-wave V2X: Towards robust and efficient directional connectivity under high mobility." *Proceedings of the 26th Annual International Conference on Mobile Computing and Networking*. 2020.

------

# Paper: Demystifying V2X

<div align=center>
<br/>
<b>Demystifying millimeter-wave V2X: Towards robust and efficient directional connectivity under high mobility</b>
</div>



#### Summary

1. lDemystify mmWave V2X with real-life testbed+large-scale 3D ray-tracing;
2. lAvailable source codes;
3. lKey insights:
   1. Conventional beam searching may work well in V2X;
   2. Blockage can be mitigated by simple design;
   3. Simple spatial multiplexing in mmWave V2X is possible;

#### Proble Statement

> 根据3GPP TS38.101协议中的规定，5G NR可以使用FR2频段，FR2频段的频率范围是24.25~52.6GHz，即移动通信领域通常所说的毫米波（严格来说，毫米波传输是指30~300GHz的频段）。

> 5G NR采用将一个特定的波束复形传输在时间上进行分片，具体说就是在不同的时间将特定的波束复形指向不同的角度，从而达到覆盖一个扇区或者360度区域的需求。
>
> - Massive MIMO可以提升10倍能力并且同时提升100倍的辐射能量效率(radiated energy-efficiency)
> - Massive MIMO的建设成本较低，而且功耗较小
> - 由于在抗衰落上的鲁棒性，Massive MMIO在空口时延上有显著减小。
> - Massive MiMO简化了多路存取层。
> - Massive MIMO提升了对无意的人为干扰和恶意的干扰方面的鲁棒性。

#### Methods

- **system overview**:

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015170829877.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015170844677.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015170759908.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015170733774.png)

#### Evaluation

  - **Environment**:   

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201015170930484.png)'

# Paper: Facilitating Robust 60 GHz Network DeploymentBy Sensing Ambient Reflectors

> Wei, Teng, Anfu Zhou, and Xinyu Zhang. "Facilitating robust 60 ghz network deployment by sensing ambient reflectors." *14th {USENIX} Symposium on Networked Systems Design and Implementation ({NSDI} 17)*. 2017. [[pdf](https://scholar.google.com/scholar_url?url=https://www.usenix.org/system/files/conference/nsdi17/nsdi17-wei-teng.pdf&hl=zh-CN&sa=T&oi=gsb-gga&ct=res&cd=0&d=7107477032426048836&ei=VYzMYIfCDMSsywSBmKRw&scisig=AAGBfm1ynS9w875ETmVL8oDm-pQ-QdwoYQ)]  [[ppt](chrome-extension://ikhdkkncnoglghljlkmcimlnlhkeamad/pdf-viewer/web/viewer.html?file=https%3A%2F%2Fwww.usenix.org%2Fsites%2Fdefault%2Ffiles%2Fconference%2Fprotected-files%2Fnsdi17_slides_wei.pdf)]

- **aimbition:** Network performance sensitive to AP deployment and environmental characteristics, sense, predict and optimizethe AP placement from a 60 GHz radio’s eyes
- sense: major reflectors from 60Ghz radio's eyes;

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210618201336108.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210618201658493.png)

- Predict: the performance of arbtrarily located links
- Optimize: the ap placement to maximize capacity and robustness
  - Track how each signal path is attenuated over distance and reshaped by reflectors
  - A fine-grained way to model 60 GHz signals
  - Input: layout/reflectivity for dominant reflectors
  - Output: RSS for arbitrary AP and client locations

# 论文调研：

#### 1.1.  Soli

> Lien, Jaime, Nicholas Gillian, M. Emre Karagozler, Patrick Amihood, Carsten Schwesig, Erik Olson, Hakim Raja, and Ivan Poupyrev. "Soli: Ubiquitous gesture sensing with millimeter wave radar." *ACM Transactions on Graphics (TOG)* 35, no. 4 (2016): 1-19.   378

##### 1.1.2. Contribution

- presents Soli, a new, robust, high-resolution, low-power, miniature gesture sensing technology for human-computer interaction based on `millimeter-wave radar`.
- a radar-based sensor optimized for human-computer interaction, building the sensor architecture from the ground up with the inclusion of `radar design principles`, `high temporal resolution gesture tracking`, a `hardware abstraction layer (HAL)`, a `solidate radar chip and system architecture`, interaction models and gesture vocabularies, and gesture recognition.

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201116162307105.png)

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201116162527982.png)

##### 1.1.3. Experiment

![](https://gitee.com/github-25970295/blogImage/raw/master/img/image-20201116162641142.png)

