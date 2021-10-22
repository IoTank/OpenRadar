---
title: projectRecord
date: 2021-05-1 16:00:04
author: liudongdong1
img: https://cdn.pixabay.com/photo/2016/12/19/08/39/mobile-phone-1917737__340.jpg
cover: false
categories: AIOT
tags:
  - mmwave
  - project
---

### 0. Tools

#### .1. [pymmw](https://github.com/m6c7l/pymmw)

- [ ] chrome-extension://ikhdkkncnoglghljlkmcimlnlhkeamad/pdf-viewer/web/viewer.html?file=https%3A%2F%2Fcore.ac.uk%2Fdownload%2Fpdf%2F225625415.pdf%23page%3D6#page=6  
- [ ] 学习这里的每一个特征

> Constapel, Manfred, Marco Cimdins, and Horst Hellbrück. "A Practical Toolbox for Getting Started with mmWave FMCW Radar Sensors." *4th KuVS/GI Expert Talk on Localization* (2019). [[pdf](https://core.ac.uk/download/pdf/225625415.pdf#page=6)] [[code](https://github.com/m6c7l/pymmw)]

> a toolbox composed of Python scripts to interact with `TI's evaluation module (BoosterPack) for IWRxx43 mmWave sensing devices.`
>
> -  access to particular OOB firmware versions
> -  access to particular OOB firmware versions

- 2D plots
  - `range and noise profile`
  - `Doppler-range FFT heat map`
  - `azimuth-range FFT heat map`
  - `FFT of IF signals`
- 3D plots
  - `CFAR detected objects (point cloud)`
  - `simple CFAR clustering`
- Data capture
  - `range and noise profile with CFAR detected objects`

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527142549064.png)

#### .2. **[ AWR1843-Read-Data-Python-MMWAVE-SDK-3-](https://github.com/ibaiGorordo/AWR1843-Read-Data-Python-MMWAVE-SDK-3-)**

> Python program to `read and plot the data` in real time from the **AWR1843** mmWave radar board (Texas Instruments, MMWAVE SDK 3). The program has been tested with `Windows and Raspberry Pi` and is based on the` Matlab demo from Texas Instruments`.
>
> First, the program configures the Serial ports and sends the CLI commands defined in the configuration file to the radar. Next, the data comming from the radar is parsed to extract the 3D position and doppler velocity of the reflected points. Finally, the 2D position of the reflected points is shown in a scatter plot.

#### .3. [pyroSAR](https://github.com/johntruckenbrodt/pyroSAR)

> The pyroSAR package aims at providing a complete solution for the `scalable organization and processing of SAR satellite data`:
>
> - Reading of data from various past and present satellite missions
> - Handling of acquisition metadata
> - User-friendly access to processing utilities in [SNAP](https://step.esa.int/main/toolboxes/snap/) and [GAMMA Remote Sensing](https://www.gamma-rs.ch/) software
> - Formatting of the preprocessed data for further analysis
> - Export to Data Cube solutions

#### .4. [OpenRadar](https://github.com/PreSenseRadar/OpenRadar)

1. Reading raw ADC data.
2. Preprocessing data in DSP stack.
3. Utilizing preprocessed data for tracking, clustering and machine learning.
4. Different demo implementations from TI and our own explorations.
5. [openradar.readthedocs.io](https://openradar.readthedocs.io/)

#### .5. [mmWaveRadarPro](https://github.com/Mr-Bulijiojio/mmWaveRadarPro)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210625190050369.png)

### 1. Object Detection

#### .1.[CameraRadar Fusion](https://github.com/TUMFTM/CameraRadarFusionNet)

> Nobis, Felix, et al. "A deep learning-based radar and camera sensor fusion architecture for object detection." *2019 Sensor Data Fusion: Trends, Solutions, Applications (SDF)*. IEEE, 2019. [[pdf](chrome-extension://ikhdkkncnoglghljlkmcimlnlhkeamad/pdf-viewer/web/viewer.html?file=https%3A%2F%2Farxiv.org%2Fpdf%2F2005.07431.pdf)]
>
> - provides a neural network for object detection based on camera and radar data.

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527135936250.png)

#### .2. [CenterFusion](https://github.com/mrnabati/CenterFusion)

> Nabati, Ramin, and Hairong Qi. "Centerfusion: Center-based radar and camera fusion for 3d object detection." *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision*. 2021. [[pdf](https://openaccess.thecvf.com/content/WACV2021/papers/Nabati_CenterFusion_Center-Based_Radar_and_Camera_Fusion_for_3D_Object_Detection_WACV_2021_paper.pdf)]
>
> -  first uses a `center point detection network` to detect objects by `identifying their center points on the image`
> - solves the `key data association problem` using `a novel frustum-based method` to associate the` radar detections` to their corresponding `object's center point`
> - The `associated radar detections` are used to generate `radar-based feature maps` to complement the `image features`, and `regress to object properties such as depth, rotation and velocity`.

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527140247672.png)

#### .3. [RODNet](https://github.com/yizhou-wang/RODNet)

> Wang, Yizhou, et al. "Rodnet: Radar object detection using cross-modal supervision." *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision*. 2021.[[Paper\]](https://openaccess.thecvf.com/content/WACV2021/html/Wang_RODNet_Radar_Object_Detection_Using_Cross-Modal_Supervision_WACV_2021_paper.html) [[Dataset\]](https://www.cruwdataset.org/) [[code](https://github.com/yizhou-wang/RODNet)]

#### .4. [Radar-RGB-Attentive-Multimodal-Object-Detection](https://github.com/RituYadav92/Radar-RGB-Attentive-Multimodal-Object-Detection)

> Yadav, Ritu, Axel Vierling, and Karsten Berns. "Radar+ RGB Fusion For Robust Object Detection In Autonomous Vehicle." *2020 IEEE International Conference on Image Processing (ICIP)*. IEEE, 2020. [[pdf](https://ieeexplore.ieee.org/document/9191046)] [[code](https://github.com/RituYadav92/Radar-RGB-Attentive-Multimodal-Object-Detection)]

#### .5. [radar-ml](https://github.com/goruck/radar-ml)

> Radar-based `recognition and localization of people and things` in the home environment has certain advantages over computer vision, including increased `user privacy`, `low power consumption`, `zero-light operation` and `more sensor flexible placement`.
>
> - accurately `detect people, pets and objects` using low-power millimeter-wave radar
> -  self-supervised learning, leveraging conventional camera-based object detection, can be used to generate radar-based detection models. 

> - Arrange a` camera` and a` radar sensor` to share a `common view of the environment`.
> - Run the radar and a camera-based object detection system to `gather information about targets` in the environment.
> - Create `ground truth observations` from the radar when it senses targets at the same point in space as the object detector.
> - Train a machine learning model such as a Support-Vector Machine (SVM) or a deep neural network (DNN) on these observations and check that it has acceptable accuracy for your application.
> - Use the trained machine learning model to predict a novel radar target’s identity.

![Alt text](https://github.com/goruck/radar-ml/raw/master/images/coord_system.jpg?raw=true)

#### .6. [RAI Image based ship detection](https://github.com/MichDeb36/Ship-detection-using-radar-satellite-imagery)

- https://github.com/kriss-kad/NM404_AzmuthStar

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527202645900.png)

#### .7. PersonCount

> Wen, Longyin, et al. "Detection, Tracking, and Counting Meets Drones in Crowds: A Benchmark." *arXiv preprint arXiv:2105.02440* (2021).[论文链接](https://arxiv.org/abs/2105.02440)  [项目链接](https://github.com/VisDrone/DroneCrowd)

> 通过提出 STNNet 方法来共同解决无人机拍摄的拥挤场景中的密度图估计、定位和跟踪。值得注意的是，作者设计了相邻上下文损失来捕捉连续帧中相邻目标之间的关系，对定位和跟踪是有效的。为了更好地评估无人机的性能，作者还收集并标记了一个新的数据集：DroneCrowd。，其中包含了用于密度图估计、人群定位和无人机跟踪的头部标注轨迹。并称希望这个数据集和提出的方法能够促进无人机上`人群定位、跟踪和计数`的研究和发展。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210528112002241.png)

#### .8. [milliEye](https://github.com/sxontheway/milliEye)

> Xian Shuai, Yulin Shen, Yi Tang, Shuyao Shi, Luping Ji, and Guoliang Xing, milliEye: A Lightweight mmWave Radar and Camera Fusion System for Robust Object Detection. In Proceedings of Internet of Things Design and Implementation (IoTDI’21) [[imaging](https://github.com/sxontheway/milliEye/blob/main/pictures/indoor.gif)]

### 2. RainFow Prediction

#### .1. [CIKM-Cup-2017](https://github.com/yaoyichen/CIKM-Cup-2017)

- 赛题提供10,000组的雷达图像样本。每组样本包含60幅图像，为过去90分钟内(间隔6 min,共15帧)，分布在4个高度(0.5km, 1.5km, 2.5km, 3.5km)上的雷达反射率图像。
- 每张雷达图像大小为[101,101]，对应的空间覆盖范围为101×101km。`每个网格点记录的是雷达反射率因子值Z`。反射率因子，表征气象目标对雷达波后向散射能力的强弱，`散射强度一定程度上反映了气象目标内部降水粒子的尺度和数密度`，进而推测其与降水量之间的联系。

[![](https://github.com/Jessicamidi/CIKM-Cup-2017/raw/master/pic/sample_example.jpg)](https://github.com/Jessicamidi/CIKM-Cup-2017/blob/master/pic/sample_example.jpg)

- 目标`：利用各个雷达站点在不同高度上的雷达历史图像序列`，预`测图像中心位于[50,50]坐标位置的目标站点未来1-2小时之间的地面总降水量`，`损失函数为降水量预测值与真实值的均方误差`。

[![](https://github.com/Jessicamidi/CIKM-Cup-2017/raw/master/pic/Input_Output.png)](https://github.com/Jessicamidi/CIKM-Cup-2017/blob/master/pic/Input_Output.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527140808736.png)

- **图像拼接：** 样本与样本之间并不完全独立，图像样本之间存在一定的重叠，可以通过模板匹配的方式寻找样本之间的坐标关联特性。通过样本之间的局部图像拼接，能够将一系列小范围的局部雷达图像恢复到空间更大范围的雷达图像，进而获得关于云团更加整体的特性。[![Item-based filtering](https://github.com/Jessicamidi/CIKM-Cup-2017/raw/master/pic/pintu.png)](https://github.com/Jessicamidi/CIKM-Cup-2017/blob/master/pic/pintu.png)

  [![](https://github.com/Jessicamidi/CIKM-Cup-2017/raw/master/pic/pin2.gif)](https://github.com/Jessicamidi/CIKM-Cup-2017/blob/master/pic/pin2.gif)

- **轨迹追踪：**泰勒冻结假设(Taylor Frozen Hypothesis)，流场中存在显著的时空关联特性，即可以认为雷达反射图中云团在短时间内趋向于在空间以当地平均对流速度平移，短时间内并不会发生外形或者反射强度的剧烈改变。即监测点x处在未来τ时刻后的雷达信号f，能够通过平均对流速度U[![Item-based filtering](https://github.com/Jessicamidi/CIKM-Cup-2017/raw/master/pic/SIFT.png)](https://github.com/Jessicamidi/CIKM-Cup-2017/blob/master/pic/SIFT.png)

- **特征提取：**特征包含`时间外插反射率图像`，`时间空间的矢量`，`云团形状`的统计描述三部分。

  - [![Item-based filtering](https://github.com/Jessicamidi/CIKM-Cup-2017/raw/master/pic/sub-image.png)](https://github.com/Jessicamidi/CIKM-Cup-2017/blob/master/pic/sub-image.png)
  - 在时间和空间方向（高度方向）提取图像像素的统计值（平均值、最大值、极值点个数、方差等等），作为时空特征的描述输入CNN的全连接层。
  - 某些特定的云层形态会对应典型降水事件。从拼接后的全局图像中提取云团形状的整体形态特征，包含`雷达反射率的直方图和统计类信息、云团运动速度和方向、加速度、流线曲率、SIFT描述子的直方图、监测点位置、检测点反射率与最大值比值`等。

#### .2. [RadarGUI](https://github.com/uniquezhiyuan/RadarGUI)

> PyQt 5 CINRAD雷达基数据处理可视化软件。 基于Python 3.6，用于雷达回波绘制和显示，ppi、rhi、三维散点图绘制和交互可视化。 主要功能：  1.单个体扫数据反射率因子各层仰角PPI图像；  2.单个数据反射率因子个方位角RHI图像；  3.某站点一段时间内连续数据0°仰角PPI图像连续显示；  4.单个体扫数据三位散点图交互可视化；  5.生成标准网格化数据。

### 3. Action Rec

#### .1. [Vid2Doppler](https://github.com/FIGLAB/Vid2Doppler)

> Ahuja, Karan, et al. "Vid2Doppler: Synthesizing Doppler Radar Data from Videos for Training Privacy-Preserving Activity Recognition." *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*. 2021. [[pdf](https://dl.acm.org/doi/fullHtml/10.1145/3411764.3445138)] [[video](https://karan-ahuja.com/vid2dop.html)]

![](https://github.com/FIGLAB/Vid2Doppler/raw/main/media/classification.gif?raw=true)

![img](https://github.com/FIGLAB/Vid2Doppler/raw/main/media/radial_velocity.gif?raw=true)

![img](https://github.com/FIGLAB/Vid2Doppler/raw/main/media/signal.gif?raw=true)

#### .2. [RadHAR](https://github.com/nesl/RadHAR)

> Singh, Akash Deep, et al. "Radhar: Human activity recognition from point clouds generated through a millimeter-wave radar." *Proceedings of the 3rd ACM Workshop on Millimeter-wave Networks and Sensing Systems*. 2019. [[pdf](chrome-extension://ikhdkkncnoglghljlkmcimlnlhkeamad/pdf-viewer/web/viewer.html?file=https%3A%2F%2Fdl.acm.org%2Fdoi%2Fpdf%2F10.1145%2F3349624.3356768)] [[code](https://github.com/nesl/RadHAR)]

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527144501488.png)

#### .3. [uDoppler-Classification](https://github.com/edwin-pan/uDoppler-Classification)

> Classification of Human Movement using mmWave FMCW Radar Micro-Doppler Signature.

#### .4. [mmpose](https://github.com/radar-lab/mmpose)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210625184242695.png)

#### .5.[mPose3D](https://github.com/KylinC/mPose3D)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210625184827121.png)

#### .6. [human_motion_recognition](https://github.com/99rishita/human_motion_recognition)

>  implementation of the paper 'Real-Time Human Motion Behavior Detection via CNN Using mmWave Radar'.

#### .7. [mmWave-user-recognition](https://github.com/kdkalvik/mmWave-user-recognition)

> Janakaraj, Prabhu, et al. "STAR: simultaneous tracking and recognition through millimeter waves and deep learning." *2019 12th IFIP Wireless and Mobile Networking Conference (WMNC)*. IEEE, 2019. [[pdf](https://scholar.google.com/scholar_url?url=https://par.nsf.gov/servlets/purl/10185103&hl=zh-CN&sa=T&oi=gsb-gga&ct=res&cd=0&d=698122812222638343&ei=07bVYMbqGdaR6rQPiNGVqAs&scisig=AAGBfm3Mtmshni11plYl_A172HfHPEOlZA)]

### 4. Depth

#### .1. **[ radar_depth](https://github.com/brade31919/radar_depth)**

> Lin, Juan-Ting, Dengxin Dai, and Luc Van Gool. "Depth estimation from monocular images and sparse radar data." *arXiv preprint arXiv:2010.00058* (2020). [[pdf](https://arxiv.org/pdf/2010.00058)] [[code](https://github.com/brade31919/radar_depth)]

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527143525073.png)

#### .2. [Simplified-2D-mmWave-Imaging](https://github.com/meminyanik/Simplified-2D-mmWave-Imaging)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210625184120016.png)

### 5.  Vibration

#### .1. vital signs

> 生命体征就是用来判断病人的病情轻重和危急程度的指征。主要有`心率、脉搏、血压、呼吸、疼痛、血氧、瞳孔和角膜反射的改变`等等。正常人在安静状态下，脉搏为60—100次/分（一般为70—80次/分）。当心功能不全、休克、高热、严重的贫血和疼痛、[甲状腺危象](https://baike.baidu.com/item/甲状腺危象/5187299)、心肌炎，以及阿托品等药物中毒时，心率和脉搏显著加快。当[颅内压增高](https://baike.baidu.com/item/颅内压增高/918595)、[完全性房室传导阻滞](https://baike.baidu.com/item/完全性房室传导阻滞/4010197)时，脉搏减慢。在一般情况下心率与脉搏是一致的，但在[心房颤动](https://baike.baidu.com/item/心房颤动/948317)、频发性[早搏](https://baike.baidu.com/item/早搏/2348255)等[心律失常](https://baike.baidu.com/item/心律失常/2255384)时，脉搏会少于心率，称为[短绌](https://baike.baidu.com/item/短绌/1992083)[脉](https://baike.baidu.com/item/脉/3028876)。
>
> - 生命四大体征包括[呼吸](https://baike.baidu.com/item/呼吸/15418186)、[体温](https://baike.baidu.com/item/体温)、[脉搏](https://baike.baidu.com/item/脉搏/83610)、[血压](https://baike.baidu.com/item/血压)，医学上称为四大体征。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527183148501.png)

##### .1. [TI 德州仪器](https://edu.21ic.com/video/2264)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527183646586.png)

##### .2. [加特兰](https://www.calterah.com/evolution-and-innovation-of-mmwave-radar-ii-application-in-vital-signs-detection-2-2/) [[code](https://github.com/livingstonelee/Calterah_Rhine_60GHz)]

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527184229260.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527183947313.png)

##### .3. IMEC 微电子研究中心

> Experiments have demonstrated the sensor’s ability for `multi-target detection`, `heartbeat detection at 5 meter `and accurate tracking of a pedestrian’s position and velocity.

##### .4. Vayyar

> Future Features Holisitic health and safety monitoring.

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527185701611.png)

##### .5. [mmVital-Signs](https://github.com/KylinC/mmVital-Signs)

![](https://camo.githubusercontent.com/f1868f7fc05a8609aa734aaf2a6fcbf1de0c15a2aafceb94a139f9327dbdcfd6/687474703a2f2f6b796c696e6875622e6f73732d636e2d7368616e676861692e616c6979756e63732e636f6d2f323032312d30312d31372d254536253838254141254535254231253846323032312d30312d313725323025453425423825384125453525384425383831302e33352e35322e6a7067)

##### .6.  [WaveFace](https://github.com/asaayush/WaveFace)

> - Face Verification

#### .2. Health Monitor

##### .1. [Vayyar Home](https://vayyar.com/home/)

> Vayyar's intelligent sensors `monitor location, posture as well as vital signs`, enabling behavioral monitoring such as `time spent at rest`, `in and out of bed`, `nocturnal roaming`, and `restroom visits.` Trends are detected, allowing for pre-emptive predictions of health conditions such as UTI, dementia, and disorders like sleep apnea and psychological ailments including loneliness.
>
> - Real-time fall detection
> - Rich activity data collection
> - Robust sensing in all conditions
> - Maintains privacy
> - Unobtrusive installation

<iframe width="560" height="315" src="https://www.youtube.com/embed/C0IH-6vCp-A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="1182" height="665" src="https://www.youtube.com/embed/JKj70pyaP8Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

##### .2. [patient_monitoring](https://github.com/radar-lab/patient_monitoring)

> [F. Jin et al., "Multiple Patients Behavior Detection in Real-time using mmWave Radar and Deep CNNs," 2019 IEEE Radar Conference (RadarConf), Boston, MA, USA, 2019, pp. 1-6, doi: 10.1109/RADAR.2019.8835656.](https://ieeexplore.ieee.org/abstract/document/8835656)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210625184528428.png)

##### .3. [mmWave_Gait](https://github.com/JasonYang8119/mmWave_Gait)

> Meng, Zhen, et al. "Gait recognition for co-existing multiple people using millimeter wave sensing." *Proceedings of the AAAI Conference on Artificial Intelligence*. Vol. 34. No. 01. 2020. [[pdf](https://scholar.google.com/scholar_url?url=https://ojs.aaai.org/index.php/AAAI/article/download/5430/5286&hl=zh-CN&sa=T&oi=gsb-gga&ct=res&cd=0&d=5845655381948608022&ei=DLTVYMC4KsiE6rQPpbWNQA&scisig=AAGBfm1Vh2xLHofD2gkBxRG9XEuwlGx2tA)] [[code](https://github.com/JasonYang8119/mmWave_Gait)]

#### .3. [Fall Detection](https://github.com/elloh755/Fall-Detection-with-Vayyar-Radar)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527191652649.png)

##### .1. [mmfall](https://github.com/radar-lab/mmfall)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210625184339228.png)

### 6. Position&Tracking

#### .1. **房屋面积测量**

> 根据AiP毫米波雷达具有距离高分辨率这一特性，结合波达角估计算法、恒虚警率检测及相应的边界搜索方法，最终得到了一种实用鲁棒的房间面积测量方法: 例如，通过对房间`面积的测量`，空调可以更好地控制制冷量，提高运行效率；电视、音响等家电可`根据房屋面积以及人员有无调节音量大小`

<video src="../../../../../OneDrive%20-%20tju.edu.cn/%E6%96%87%E6%A1%A3/work_%E7%BB%84%E4%BC%9A%E6%AF%94%E8%B5%9B/mmwave/project/%E5%AE%A4%E5%86%85%E4%BA%BA%E5%91%98%E6%A3%80%E6%B5%8B%E5%92%8C%E5%A7%BF%E6%80%81%E8%AF%86%E5%88%AB.mp4"></video>

#### .2. [Tracking](https://www.calterah.com/application-for-indoor-detection-and-tracking-of-human-body/)

> 加特兰毫米波雷达室内人员检测与跟踪应用是基于60GHz/77GHz毫米波雷达芯片研发，采用FMCW、MIMO等技术，具有距离精度高、速度精度高、角度分辨率高及虚警率低等优点，可以实现室内情况下对`人员的准确检测`、`精确定位和稳定跟踪`，并`有效分类人与非人物体`，`统计室内人员个数`，`稳定输出人员的距离、速度和角度`等信息。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527185340332.png)

#### .3. [mmWave-localization-learning](https://github.com/gante/mmWave-localization-learning)

>  Deep Learning Architectures for Accurate Millimeter Wave Positioning in 5G
>
> - An ML-based algorithm that enables energy efficient accurate positioning from mmWave transmissions, with and without tracking. [[pdf](https://github.com/gante/mmWave-localization-learning#papers)]

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210625183554049.png)

### 7. Dataset

#### .1. [DeepMIMO-codes](https://github.com/DeepMIMO/DeepMIMO-codes)

> Ahmed Alkhateeb, “[DeepMIMO: A Generic Deep Learning Dataset for Millimeter Wave and Massive MIMO Applications](https://arxiv.org/pdf/1902.06435.pdf),” in Proc. of Information Theory and Applications Workshop (ITA), San Diego, CA, Feb. 2019.
>
> a MATLAB code package of the DeepMIMO dataset generated using [Remcom Wireless InSite](http://www.remcom.com/wireless-insite) software. The [DeepMIMO dataset](http://deepmimo.net/) is a publicly available parameterized dataset published for deep learning applications in mmWave and massive MIMO systems.

###  Resource

- 降雨预测：https://github.com/yaoyichen/CIKM-Cup-2017
- mmwave 公司： https://www.calterah.com/news/
- [Vayyar Imaging: a global leader in 4D radar imaging technology,](https://blog.vayyar.com/vayyar-home-remote-health-monitoring)
- Vayyar 公司： https://blog.vayyar.com/
- 学习资源： https://github.com/RadarCODE/awesome-sar  待学习

