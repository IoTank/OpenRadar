---
title: WalabotRelative
date: 2021-2-19 07:56:09
author: liudongdong1
img: https://cdn.pixabay.com/photo/2015/06/24/16/36/office-820390__340.jpg
cover: false
categories: mmwave
tags:
  - device
---

> Walabot is a pocket-sized device that provides cutting-edge technology for `Radio Frequency (RF) `tridimensional `(3D) sensing and image processing`, enabling sophisticated applications such as:
>
> - `Breathing monitoring`
> - `Object tracking and fall detection`
> - `In-wall pipe and wire detection`

<iframe width="1904" height="768" src="https://www.youtube.com/embed/rW7N5ieC2LQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210610174235594.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210610174343123.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210610174402390.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210610174251858.png)

### .1. Image Features

#### .1. Scan Profiles

> - **Short-range**: Short-range, penetrative scanning` inside dielectric materials` such as walls.
> - Profiles for distance scanning:
>   - **Sensor:** High-resolution images, but slower capture rate.
>   - **Sensor narrow**: Lower-resolution images for a fast capture rate. Useful for tracking quick movement.

#### .2. Actions

> - **Raw image**: Provides tridimensional (3-D) image data.
> - **Raw image slice**: Provides `bidimensional (2-D) image data` (3D image is projected to 2D plane) of the slice `where the strongest signal is produced`.
> - **Image energy**: Provides `a number representing the sum of all the raw image’s pixels’ signal power.`
> - **Imaging targets** (if the short-range scan profile was used) and **Sensor targets** (if one of the sensor scan profiles was used): Provide `a list of and the number of identified targets `(in the current API version, Imaging targets provides only the single target with the strongest signal).
> - **Raw Signals** raw signals as recorded by the sensor. Each signal` (*i,\*j) `represents the reflected pulse transmitted from antenna \*i, reflected from the target and recieved in antenna \*j.****

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210610162318161.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210610162335363.png)

- **Dynamic-imaging filter**: removes static signals, leaving only changing signals. Moving Target Identification (**MTI) filter, the Derivative filter is available for the specific frequencies typical of breathing.

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210610172856216.png)

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210610173059524.png)

### .2. Procedure

> 1. **Connect:** Establish communication with Walabot.
> 2. **Configure:** Set scan profile and arena; optionally, set a dynamic-imaging filter and/or change the sensitivity threshold.
> 3. **Calibrate:**` Ignore or reduce the signals of fixed reflectors` such as walls according to environment. Must be performed initially (to avoid delays – preferably before Start), upon any profile change, and is recommended upon possible changes to environment.
> 4. **Start:** Start the system in preparation for scanning. Requires a scan profile to have been set.
> 5. **Trigger:** Scan (sense) according to profile and record signals to be available for processing and retrieval. Should be performed before every Get action.
> 6. **Get action**: Process as relevant and provide image data for the current arena, according to specified get action, current dynamic-imaging filter (if any), and current sensitivity threshold. Get actions retrieve the last completed triggered recording, and Walabot automatically makes sure the application doesn’t receive the same recording twice (so, you have the option of implementing Trigger and Get action in parallel).
> 7. **Stop** and **Disconnect**.

### .3. Opensource

- [*Walabot*-PeopleCounter](https://github.com/Walabot-Projects/Walabot-PeopleCounter)
- [*Walabot*-AirPiano](https://github.com/Walabot-Projects/Walabot-AirPiano)
- [Breathing_heart_rate_radar](https://github.com/arun1993/Breathing_heart_rate_radar)
- [*Walabot*-DistanceMeasure](https://github.com/Walabot-Projects/Walabot-DistanceMeasure)
- [*Walabot*-SeeThroughDemo](https://github.com/Walabot-Projects/Walabot-SeeThroughDemo)
- [*Walabot*-RobotGestures](https://github.com/Walabot-Projects/Walabot-RobotGestures)
- [smart3DSensorForAlexa](https://github.com/rondagdag/smart3DSensorForAlexa)
- [*Walabot*BabyMonitor](https://github.com/shijiong/WalabotBabyMonitor)
- [*walabot*-sleep-tracker](https://github.com/ckuzma/walabot-sleep-tracker)
- [Eye*Walabot*](https://github.com/daveyclk/EyeWalabot)
- [vehicle-rear-vision](https://github.com/Nyceane/vehicle-rear-vision)
- [*walabot*-tremor-mapper](https://github.com/vaidhyamookiah/walabot-tremor-mapper)
- [*Walabot*-Wheelchair](https://github.com/chrisdeely/Walabot-Wheelchair)
- [Radar Explore](https://github.com/wzhaha/Radar_explore)

### Resource

- [API](https://api.walabot.com/_pythonapi.html#_installingwalabotapi)
- http://www.tip-lab.com/article/?uuid=883cfd89f9834ce592d6c0c715d72cb1