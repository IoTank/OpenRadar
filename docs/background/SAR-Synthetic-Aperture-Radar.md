---
title: SAR-Synthetic-Aperture-Radar
date: 2021-05-1 16:00:04
author: liudongdong1
img: https://cdn.pixabay.com/photo/2015/12/11/09/30/mobile-phone-1087845__340.jpg
cover: false
categories: AIOT
tags:
  - mmwave
  - project
---

> `ISAR`与`SAR`的主要区别在于，`前者要求雷达载体静止不动而目标运动`，作为一种主动发射和接收电磁波的雷达，它相比RGB相机有着不受天气、昼夜影响的优良特性，在军事领域有着广泛的应用前景。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527182530690.png)

### 1. Electromagnetic Spectrum

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527152653132.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527192346294.png)

### 2. Radar Image

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527182230534.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527153647296.png)

#### .0. 原理

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527190957929.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527191114407.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527191134212.png)

#### .1. 距离分辨率

> 距离分辨率和频率有关，频率越大，则波长越短，那么想象成间隔越细腻，距离分辨率就越高。但波长越短，穿透能力也就有一定的下降

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527164323301.png)

#### .2. 方位分辨率

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527180945316.png)

#### .3. 特点

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527181043550.png)

> 离得传感器越近(传感器在左边)，变形越小，越远越大
>
> 1、透视收缩：`越近那么集中的物体能量就越多，就越亮`
>
> 2、顶底滞移：本来山头在中间的，现在跑到前面去了.
>
> 3、阴影：`背向雷达的坡一般头回有阴影`。这也就可以大致判断雷达的大致位置了

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527181138873.png)

#### .4. 后向散射系数

> `系数越大，图像越亮`。`系数越低，图像越暗`。返射回雷达的波占总的散射的比例。

![image-20210527181333352](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527181333352.png)

##### .1. **反射表面**：`越粗糙，散射越强`

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527181411964.png)

##### .2. 波长越长，穿透性越强（X<C<S<L<P）

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527181634371.png)

##### .3. 入射角

> 随着入射角的增加、后向散射减少

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527181734191.png)

### 3. Radar parameters

#### .1.  wavelength

> - surface penetration is key factor of wavelength selection;
> - 波长越长，穿透能力越好。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527153951874.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527154137146.png)

#### .2. Polarization

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527154241607.png)

#### .3. Incident angle

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527154314915.png)

### 4. Backscatter

- **衍射**：指的是波（如光波）遇到障碍物时偏离原来直线传播的物理现象。也就是说，电磁波具备“绕开”障碍物的能力。波长越长（大于障碍物尺寸），波动性越明显，越容易发生衍射现象。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527162919600.png)

- 穿透：

  - 表面反射：需要`用外面的电场和磁场感应出介质里面的电场和磁场`。电磁波在不同介质的传播速度，取决于介质（障碍物）的介电特性和介磁特性。如果介质是理想导体，导电性能特别好，那么，电场在该理想导体内部永远为0，就不能产生电场。`障碍物是理想导体(超导材料），所有的电磁波都会反射回去。`

  - 对于非理想导体（大部分介质），电磁波在表面上分成`折射和反射的两部分`。两部分的比例跟`波速、入射角有关`，而波速又跟频率有关。电磁波进入物体后： 大部分介质不是理想导体或良导体，而是绝缘体或者有不同电阻率值的导体。

    - 电磁波在绝缘体中的传播较为顺畅。像玻璃，就是一种非常典型的绝缘体。光线在玻璃中传播时，吸收率很低，所以玻璃看着就很透明。**在有电阻率的导体中，频率越高的电磁波，衰减得就越快。**

    - 电磁波`在不均匀介质中传播`，等于是在不同介质之间反复地发生折射、反射、衍射。传播的路径更加复杂，最终射出的方向也非常复杂。过长的路径，也会带来更大的衰减（损耗）。
    - 对于这些`频率极高的电磁波，经典的电动力学不能完全成立`。

  - 从介质到空气，又是一波折射和反射:

#### .1. Dielectric Constant(介电常数)

> 当我们将一个电场作用于一个宏观介质时，介质中的分子会发生某些变化，使得介质中的平均电场小于外加电场。这个效应叫做介电效应。介电效应与经典光学息息相关，折射率 ![[公式]](https://www.zhihu.com/equation?tex=n++%3D+%5Csqrt%7B%5Cvarepsilon_r+%5Cmu_r%7D+%5Capprox+%5Csqrt%7B%5Cvarepsilon_r%7D) ，这里 ![[公式]](https://www.zhihu.com/equation?tex=%5Cvarepsilon_r) 和 ![[公式]](https://www.zhihu.com/equation?tex=%5Cmu_r) 分别是介电常数和磁导率。
>
> - 介电常数对雷达电磁波的影响体现在俩个方面：
>   - 影响介质表面对电磁波的吸收（反射率）；
>   - 电磁波在穿过介质时波长（频率）发生变化；
>
> - 介质的相对介电常数是`表征介质极化的一个物理量`，它是`由介质本身的属性决定的`。因此，介质不同，相对介电常数也不同。被测介质的介电常数大小直接影响高频脉冲信号的反射率。当电磁脉冲到达介质表面时，电磁波会发生反射和折射。
> - `相对介电常数越大，则反射的损耗越小`，相反`相对介电常数越小，则发射的损耗越大，信号衰减的越严重`。当被测介质的电导率大于10mS/cm，则会全部反射回来，即回波信号越强。
> - 衰减系数与导电率 及磁导率的平方根成正比，与介电常数的平方根成反比。
> - `一般情况下被测介质的相对介电常数越大，反射回来的脉冲信号就越强。`

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527160158733.png)

##### .1.导波雷达液位计

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527155412143.png)

> 依据时域反射原理（TDR）为基础的雷达液位计，采用高频振荡器作为电磁脉冲发生体，发射电磁脉冲，沿导波缆或导波杆向下传播，当遇到被测介质表面时，雷达液位计的部分电磁脉冲被反射回来，形成回波。并沿相同路径返回到脉冲发射装置，通过测量发射波与反射波的运行时间，经 t=2d/c 公式，计算得出液位高度。
>
> 导波雷达液位计发射电磁脉冲时，在通过导波缆顶部的时候，由于`距发射端较近，会产生一个虚假回波`，可通过滤除虚假回波，来消除干扰。电磁脉冲沿导波缆向下传播时，`当信号到达被测介质表面时，回波一部分会被反射，并在回波曲线上产生一个阶跃性变化`。另外一部分信号仍然会继续向下传播，直到损耗在不断发射中。液位计通过检测出液位回波和顶部发射回波之间的时间差，根据这个时间差，经过智能化信号处理器，进行计算就可以得到液位的高度。
>
> 在空罐的时候，没有液位就不会检测到液位回波信号，但是顶部虚假回波同样会存在，电磁脉冲传输到导波缆的底部，罐底会产生一个回波。`假如罐体内有两种不相溶的介质，由于密度不同，两种介质会分为上下两层`。如果且这两种介质的介电常数相差极大，那么就可以通过回波信号的不同来判断两种介质的界面，进而计算出两种介质的高度以及界面的高度。由于电磁脉冲是通过导波缆向下传播，信号衰减比较小，因而可以测量低介电常数的介质。

#### .2. Surface roughness

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527160617343.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527160659543.png)

#### .3. Radar Interaction

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210527164216382.png)

### Resource

- 书籍： chrome-extension://ikhdkkncnoglghljlkmcimlnlhkeamad/pdf-viewer/web/viewer.html?file=http%3A%2F%2Fstaff.ustc.edu.cn%2F~honglee%2Fced%2Fchap4_p.pdf
- https://xueshu.baidu.com/usercenter/paper/show?paperid=d989854581928823eb2e653815e6db79&site=xueshu_se&hitarticle=1