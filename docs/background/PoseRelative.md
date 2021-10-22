---
title: PoseRelative
date: 2021-06-30 16:00:04
author: liudongdong1
img: https://cdn.pixabay.com/photo/2021/05/10/14/48/rain-6243559__340.jpg
cover: false
categories: AIOT
tags:
  - mmwave
---

> Meng, Zhen, et al. "Gait recognition for co-existing multiple people using millimeter wave sensing." *Proceedings of the `AAAI Conference on Artificial Intelligence`*. Vol. 34. No. 01. `2020`.  `CCF -A`

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629134431230.png)

------

# Paper:  mmGait

<div align=center>
<br/>
<b>Gait recognition for co-existing multiple people using millimeter wave sensing</b>
</div>

#### Summary

1. build and publicly achieve a` first-of-its-kind mmWave gait data set`, which is collected from 95 volunteers and lasts about 30 hours in total;
2. propose a new deep learning model `mmGaitNet to exact features for each attribute of point cloud`.
3. Procedures
   1. using two mmWave devices `capturing reflected signal` from walking persons to `forms point clouds.`
   2. `segment` the point cloud of multi-people who are walking at the same time to get a single person' s gait point cloud data.
      - using clustering algorithm `DBscan` to cluster point cloud;
      - using `Hungarian algorithm` to tack the point cloud clusters of one person's routes;
      - matching the route with corresponding volunteers one by one;
4. the accuracy of gait recognition decreases with the increase of number of co-existent walking people;
5. the accuracy of gait recognition increases if using more mmWave devices.

#### Research Objective

  - **Application Area**: `security check`,  `health monitoring,` `novel human-computer interaction`
- **Purpose**:  accomplish person identification while `preserving privacy `even `under non-line-of-sight scenarios`, such as in `black weak light` or `blockage conditions`.

#### Proble Statement

- each person's unique walking posture leads to a `unique wireless signal variation pattern`.

**previous work:**

- `Computer vision`:  `privacy concerns`,` lighting condition sensitive`;
- `wireless perception`:  difficult ot be segmented to `isolate the impact of each person`.
  -  Channel state information(CSI): `WiFiUm,` `wiwho`, `AutoID`,
- human tracking and identify with mmWave radars (Zhao et al 2019)
  - `autonomous environment mapping` using comodity mmWave;
  - `robot navigation` in dynamic environment
  - `vital sign monitoring`
  - gesture recogniton: soli

#### Advantage

- emerging 5G technologies
- mmWave provide much `fine-grained spatial resolution`

#### Methods

##### 【Module 1】 Data Collection

- `Time Synchronization`:   run time synchronization NTP on two computers, use the client computer to synchronize with the time of the server.

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629170334401.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629170831328.png)

> Figure 2: The number of mmWave `reflection points`. In scene1 (a) and scene2 (c), as `the number of volunteers walking increases simultaneously`, `the number of points in the point cloud increases slowly.` In scene1 (b) and scene2 (d), as the number of walking volunteers increases simultaneously,` the number of points for a volunteer in the point cloud decreases. `
>
> - max cloud point output by devices
> - occlusion increased.

##### 【Module 2】 Data Annotation 

- remove noise points reflected by static objects utilizing static clutter removal [CFAR](https://zhuanlan.zhihu.com/p/269840008).
- adopt [DBSCAN](https://github.com/choffstein/dbscan) clustering to remove the noise points in the point cloud. the closet distance between two side-by-side people is about 0.3m.

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629184431564.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629184538151.png)

##### 【Module 3】 Data Merge

- **Coordinate transformation**

  - rotate the coordinate system of the two devices clockwise to make the two coordinate systems in the same direction.
  - translate the coordinate system of IWR6843 consistent with IWR1443.

  ![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629185105205.png)

- **merge the point cloud from two devices who's time difference is less than specific threshold**

##### 【Module 4】 AI Mode

- input: point clouds' five attributes: spatial location(x,y,z), radial speed, signal strength of the points. the input of each attribute network is a p*t matrix, p: number of points(128), t: time(3s).
- output: the jth person;

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629185510729.png)

#### Evaluation

  - **Environment**:   

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629152330692.png)

> the two devices are configured to use all their three transmitter antennas and four receiver antennas to generate 3D point cloud data, outputing a frame of 3D point cloud in every 0.1s.

- Result

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629190024594.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629190137949.png)

#### Notes

##### [NTP 时间同步：](https://zhuanlan.zhihu.com/p/138339057)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629191006843.png)

##### [CFAR](https://zhuanlan.zhihu.com/p/269840008)

> 全称是Constant False Alarm Rate Detector，恒定虚警概率下的检测器，是雷达目标检测的一种常见的手段。在含有噪声的情况下确定信号**存在**还是**不存在**。恒虚警检测器首先对输入的噪声进行处理后确定一个门限，将此门限与输入端信号相比，如输入端信号超过了此门限，则判为有目标，否则，判为无目标。一般信号由信号源发出，在传播的过程中受到各种干扰，到达接收机后经过处理，输出到检测器，然后检测器根据适当的准则对输入的信号做出判决。

- 噪声和信号同时存在： $x(t)=s(t)+n(t)$;
- 只有噪声存在： $x(t)=n(t)$

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629191850177.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629192052515.png)

```matlab
%--------------------------------------------------------------------------
%   初始化
%--------------------------------------------------------------------------
clear;clc;


sig = randn(1000,1);                                                        %构造噪声信号
sig(300) = 15;                                                              %构造目标信号
sig_pow = sig.^2;                                                           %信号平方

[detected,th] = rt.cfar_detector(sig_pow,[1e-6 1e-6],[8 3 1 3 8]);          %CFAR检测器，输出检测结果

%--------------------------------------------------------------------------
%   可视化
%--------------------------------------------------------------------------
figure(1)
plot(sig_pow);hold on
plot(th);
plot( find(detected==1),sig_pow(detected),'ro')
grid on
hold off
legend('回波信号','判决门限','判决结果')
```

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629192251178.png)

- [radar tools/TOF camera tools/Optimization Tools工具箱](https://github.com/qwe14789cn/radar_tools)

##### [DBSCAN](https://blog.csdn.net/u013181595/article/details/80452914)

> DBSCAN:(Density-Based Spatial Clustering of Applications with Noise)是一个比较有代表性的`基于密度的聚类算法`。与划分和层次聚类方法不同，它将簇定义为密度相连的点的最大集合，能够把具有足够高密度的区域划分为簇，并可在噪声的空间数据库中发现任意形状的聚类。[code](https://github.com/choffstein/dbscan)

- Ε邻域：给定对象半径为Ε内的区域称为该对象的Ε邻域；
- 核心对象：如果给定`对象Ε领域内的样本点数大于等于MinPts，`则称该对象为核心对象；
- 直接密度可达：对于样本集合D，如果`样本点q在p的Ε领域内`，并且`p为核心对象`，那么对象q从对象p直接密度可达。
- 密度可达：对于样本集合D，给定一串样本点p1,p2….pn，p= p1,q= pn,假如对象pi从pi-1直接密度可达，那么对象q从对象p密度可达。
- 密度相连：存在样本集合D中的一点o，如果对象o到对象p和对象q都是密度可达的，那么p和q密度相联。

　　可以发现，密度可达是直接密度可达的传递闭包，并且这种关系是非对称的。密度相连是对称关系。DBSCAN目的是找到密度相连对象的最大集合。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629193050758.png)

##### **Hungarian algorithm**

> 匈牙利算法是一种在多项式时间内O(n3)求解任务分配问题的组合优化算法。它之所以被称作匈牙利算法，是因为算法很大一部分是基于以前匈牙利数学家的工作之上创建起来的。此后该算法被称为Kuhn–Munkres算法或Munkres分配算法（The Munkres Assignment Algorithm）。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210629193522634.png)

> Li, Ziheng, et al. "`ThuMouse`: A micro-gesture cursor input through mmWave radar-based interaction." *2020 IEEE International Conference on Consumer Electronics (`ICCE`)*. IEEE, 2020. 国际消费电子年会 B类  [[pdf](https://ieeexplore.ieee.org/document/9043082)] [[code](https://github.com/ApocalyVec/mGesf/tree/21e0bf37a9d11a3cdde86a8d54e2f6c6a2211ab5)] [[video](https://drive.google.com/file/d/1wNtAK8W8OSPjI1Kx1LN0ByB2U8i-aJUJ/view)]

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712092918103.png)

------

# Paper:  ThuMouse

<div align=center>
<br/>
<b>ThuMouse: A micro-gesture cursor input through mmWave radar-based interaction</b>
</div>

#### Summary

- to create a gesture-based and touch-free cursor interaction that accurately tracks the motion of fingers in real-time; builds a foundation for designing `finer micro gesture-based interactions`.
- presents the gesture `sensing pipeline`, with` regressive tracking `though deep neural networks, `data augmentation `for robustness, and `computer vision `as a training base;

#### Contribution

- by leveraging the sensing ability powered by the signal processing chain from 13, we detect the spatial position of objects as well as their velocity, making it possible to track the finger gesture.
- end-to-end gesture pipeline using the radar point cloud combined with several data augmentation methods to enrich the feature and build more robust models.
- illustrate the implementation and evaluation of 3D Concv LSTM model the processed the radar point cloud data to achieve the motion tracking and gesture classification;
- propose a dual-input training system utilizing computer vision to automate labeling the tracking information.

#### Research Objective

- **Purpose**:  meet the demand for` mobile interaction`, with `hands-free gadgets` such as `virtual reality`, `augmented reality`;

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712123923396.png)

#### Proble Statement

**previous work:**

- Sensing technology: pulse-band radar; Google ATAP's Project Soli;
- Detecting different gestures models;

#### Advantage

- Compared to `capacitive sensing` or `optical sensors`, mmWave radar` lacks spatial resolution` due to the fact the the `reflected signals are superimposed;` albeit this is offset by the high temporal/velocity resolution and highly sophisticated prediction model, `distinguishing similar gestures suffers` because the moving parts reside in close proximity to each other;
- Current approaches `using raw analog-to-digital converter output` with minimal pre-processing, the resulting data profile is usually a` range-velocity image` of the object in front of radar, `vary across different platforms in their size and resolution`, but the image data from cameras possess much generality;` The features given by mmWave devices are relatively unique`;
- due to high throughput of data, the` input accuracy mush give away for the real-time interaction`;

#### Methods

![image-20210712094958230](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712094958230.png)

##### 【Module 1】 Data Processing

- **Clustering**: `dynamic noise removing`
  - using `Density-Based Clustering of Applications with Noise` to identifies high density areas and expose outliers;
  - defines there must be at least `3 points to from a cluster `and` two points need to be at most 20cm `apart to be considered as in the same cluster.
- **Voxelization:**
  - create a bounding volume: $x,y,z\epsilon[-R_{bound},R_{bound}]$ the point cloud to filer out any points that lie outside the specified range of the radar, using bound to the extends parts, and using min-max normalization;
  - rasterize $P_{tfilterd}$ into (25*25*25) voxel, adn treated as the hear or color of each voxel;

- **Point Matrix**: 
  - the output points are `clustered` and `filtered to focus only on the hand`, the filter points are then` rasterized in a 3D voxel space, forming a 3D feature`;
  - radar frame: consists of n detected points, defined as n*4 matrix, each row is the `Cartesian coordiantes `and `Doppler` of the detected points;

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712102200001.png)

##### 【Module 2】 Data Augmentation

- translation: changes the spatial coordinates of the detected points while adding small Gaussian noise;
- scale: meant for simulating individuals with different shaped hands;
- rotation: cover the case where participants may perform the gesture at varying tilted angle;

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712103805381.png)

##### 【Module 3】 Model

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712105642772.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712105709879.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712123847405.png)

- user move his/her thumb against the planar surface of the index finger, the temporal displacement of the thumb is reflected in cursor movement; the index finger is emulating the mouse pad;

- convolutional layers extracting the non-linear features of each radar frame;

- LSTM cells retaining the features from the frames in a time regressive manner;  `20PFS;`

- dense layers as output that are adjustable based on given gesture scheme;

- `output the tracked position of the thumb tip in its spatial coordinates(x,y,z)`.

- Ground truth: choose the camera's tracking as ground truth reference for radar's tracking;

  - a Yolo model that identifies the position of the fingertip. (pre-trained with 750 images from 3 participants);
  - using two camera to get the location information of the fingertip;( `not detailed explained`, `time synchronization problem`)
  - according to times tamp, using linearly interpolate the position given by the two photos to get the location of the fingertip at the time when that radar frame is recorded;

  ![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712113422762.png)

#### Evaluation

  - **Environment**:   

>one above the hand to detect the x and y;  the other placed to detect the y and z, and feed into the Yolo framework to resolve the true x,y,z position of the thumb tip;
>
>- all trials are carried out with the hand `at the same relative position to the top camera`

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712113537061.png)

  - **Device:** `IWR6843`; `IWR6843ISK` antenna module (long range on-board antenna with 108 azimuth field of view(FoV) and 44 inclination FoV);
  - **Quantitative Results**

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712113811623.png)



![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712113928275.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712113958109.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210712114028065.png)



> Sengupta, Arindam, et al. "mm-Pose: Real-time human skeletal posture estimation using mmWave radars and CNNs." *IEEE Sensors Journal* 20.17 (2020): 10032-10044.

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210718113700271.png)

- **[Siyang Cao](https://scholar.google.com/citations?hl=en&user=dQvEspMAAAAJ&view_op=list_works&sortby=pubdate):** The [University of Arizona](https://scholar.google.com/citations?view_op=view_org&hl=en&org=12195049151929734221)
  - Sengupta A, Jin F, Cao S.` NLP based Skeletal Pose Estimation using mmWave Radar Point-Cloud: A Simulation Approach`[C]//2020 IEEE Radar Conference (RadarConf20). IEEE, 2020: 1-6.
  - Cao S, Sengupta `A. Systems and methods of remote extraction of skeletal information using millimeter wave radar`: U.S. Patent Application 17/065,476[P]. 2021-4-8.
  - Jin F, Sengupta A, Cao S. `mmFall: Fall Detection Using 4-D mmWave Radar and a Hybrid Variational RNN AutoEncoder`[J]. IEEE Transactions on Automation Science and Engineering, 2020.
  - Zhang R, Cao S. `Robust and Adaptive Radar Elliptical Density-Based Spatial Clustering and labeling for mmWave Radar Point Cloud Data`[C]//2019 53rd Asilomar Conference on Signals, Systems, and Computers. IEEE, 2019: 919-924.
  - Sengupta, Arindam, et al. "`mm-Pose: Real-time human skeletal posture estimation using mmWave radars and CNNs`." *IEEE Sensors Journal* 20.17 (2020): 10032-10044.
  - Zhang R, Cao S. `Real-time human motion behavior detection via CNN using mmWave radar`[J]. IEEE Sensors Letters, 2018, 3(2): 1-4.
  - Jin F, Zhang R, Sengupta A, et al. `Multiple patients behavior detection in real-time using mmWave radar and deep CNNs`[C]//2019 IEEE Radar Conference (RadarConf). IEEE, 2019: 1-6.
  - Sengupta A, Jin F, Cao S. A `Dnn-LSTM based target tracking approach using mmWave radar and camera sensor fusion`[C]//2019 IEEE National Aerospace and Electronics Conference (NAECON). IEEE, 2019: 688-693.
  - Jin F, Sengupta A, Cao S, et al. `Mmwave radar point cloud segmentation using gmm in multimodal traffic monitoring`[C]//2020 IEEE International Radar Conference (RADAR). IEEE, 2020: 732-737.

------

# Paper: mm-Pose

<div align=center>
<br/>
<b>mm-Pose: Real-time human skeletal posture estimation using mmWave radars and CNNs</b>
</div>


#### Summary

1. the first method to detect >15 distinct skeletal joints using mmWave radar reflection signals for a single human scenario for four primary motions, walking, swinging left arm, swinging right arm, swinging both arms.
2. 

#### Research Objective

  - **Application Area**:

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210718133527018.png)

- **Radar-To-Image Data Representation**
  - assign an RGB weighted pixel value to the points, resulting in a 3-D heatmap; maping the reflection power-levels,
  - gray-scale representation: ![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210718134338740.png)
  - solving the problem for extremely sparse data, and reduce the CNN size and parameters;

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210718133814943.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210718134557183.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210718135024044.png)

#### Experiment

- Texas Instruments AWR 1462 boost mmWave radar transceiver;
- using Microsoft Kinect to get 25 joint positoin as wel the UTC time-stamp;

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210718135126473.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210718135152715.png)

