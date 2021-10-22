---
title: mmwavestudio
date: 2021-07-8 16:00:04
author: liudongdong1
img:  https://cdn.stocksnap.io/img-thumbs/280h/fence-background_WUDOJVTLB9.jpg
cover: false
categories: AIOT
tags:
  - mmwave
---

### 1.  安装

1. 下载[mmwave_studio.exe](https://software-dl.ti.com/ra-processors/esd/MMWAVE-STUDIO/latest/index_FDS.html)
2. 安装FTDI驱动，安装包已经在下载的mmwave_studio.包里面了，具体操作过程参考[mmwave studio user guide](http://software-dl.ti.com/ra-processors/esd/MMWAVE-STUDIO/latest/exports/mmwave_studio_user_guide.pdf)
3. 下载安装[MCR_R2015aSP1_win32_installer.exe](https://in.mathworks.com/supportfiles/downloads/R2015a/deployment_files/R2015aSP1/installers/win32/MCR_R2015aSP1_win32_installer.exe)
4. 更改网络IP地址：192.168.33.30

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901184500724.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901184644505.png)

#### .1. connection

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901185009376.png)

- BBS:FW选择ti_studio\mmwave_studio_02_01_01_00\rf_eval_firmware\masterss文件夹下相对应毫米波雷达系列型号的.bin文件。
- MSS:FW选择ti_studio\mmwave_studio_02_01_01_00\rf_eval_firmware\radarss文件夹下相对应毫米波雷达系列型号的.bin文件。

#### .2. staticConfig

>`Tx/Rx Channel 配置`， ` Cascading Mode配置`， `ADC配置`（Bits，Format, IQ Swap),  `Frequency Config`, 

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901185142691.png)

#### .3. DataConfig

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901185406732.png)

#### .4. SensorConfig

>Profile 配置；  Chirp 信息；  Frame 信息； Data Capture;
>
>按提示配置完参数后即可开始采集。首先点击1️⃣DCA1000ARM，其实点击2️⃣Trigger Frame 便开始对雷达数据进行采集，最后采集完成，点击3️⃣PostProc便可查看雷达的数据处理后的效果图。采集到的原始数据存在4️⃣adc_data.bin文件中。  `uniflash101    mmWaveStudio110   python调试100`  

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210901185518672.png)