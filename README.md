# LogicTech-SlimeCustomizer
This is mtl's first slimeCustomizer project.
这是mtl的第一个自定义粘液附属项目

# 安装事项


## 安装如下附属前置
```
  - Slimefun
  - FoxyMachines
  - InfinityExpansion
  - LiteXpansion
  - TranscEndence
  - GuizhanLibPlugin
  - Gastronomicon
  - DynaTech
  - FinalTECH/FinalTech
```
- 注意检查附属名称FIinalTECH的大小写，正常slimecustomizer是接收FinalTech而不接受FinalTECH的，如果你执意要安装FinalTECH，可以用压缩工具打开jar文件修改其中的plugins.yml，或者使用我们在仓库中提供的slimecustomizer 然后在config中关闭自动更新
- 开发使用的FinalTECH版本是FinalTECH 2.0-preview
- 开发使用的FinalTECH已经附加在仓库中了
- 我们不建议安装过高版本的FinalTECH，就FinalTECH自身玩法来说

## 安装如下自定义粘液附属前置
```
  - HaimanTech
```
- 开发使用的海曼研究院版本是Beta1.6
- 但是基本上你能找到的所有版本都是支持的
- 我们开发使用的海曼配置已经附加在仓库中了
- 你可以去 [这里找到最新版本的海曼科技](https://github.com/haiman233/HaimanTech2)



注意事项:
- LogicTECH的配置合并时应该放在自定义粘液附属前置的后面
- 如果你会使用python，可以使用提供的combine_sc.py进行合并
- ~~我们将来会考虑做一个更好的合并程序~~
# 关于LogicTECH
## 我们的目标
- 逻辑工艺(LogicTECH)一款主要基于FinalTECH(乱序技艺)的自定义粘液附属
- 众所周知，乱序的很多强大的机器，比如货运类和反向合成台等会让粘液刻变得糟糕，因为大家都在大量使用，甚至不合理使用
- 所以我们尝试使用这个附属提供一系列的高速率压缩机器和压缩产线，在增加合成表和合成路径的复杂度的同时
- 让服务器资源耗用降低的同时增加玩家的游戏体验
- 同时，我们创立的新的合成途径，让玩家少用合成机
## 我们的实现方式
- 逻辑工艺尝试将玩家产线的复杂性抽象进合成表的复杂性，并用一体机和压缩机器代替
- 机器产速是经过衡量的，并不会超模
## 关于乱序
- 逻辑工艺是基于乱序v2-preview开发的
- 我知道乱序的一些机器和物品可能在某些服务器过于op，例如尘埃反应堆(MATRIX_REACTOR)的复制物品特性
- 这个附属可以正常运行 即使将尘埃反应堆(MATRIX_REACTOR)禁用
- 并且我保证使用它可以降低玩家放置在世界中的乱序货运，反向合成台，网络合成机等的数量
## 关于版本
- 在[README.txt](README.txt)中查看详细信息

 
 
EN-US

# LogicTech-SlimeCustomizer
This is mtl's first slimeCustomizer project.

# How to install


## Install these slimefun addons as depend:
```
  - Slimefun
  - FoxyMachines
  - InfinityExpansion
  - LiteXpansion
  - TranscEndence
  - GuizhanLibPlugin
  - Gastronomicon
  - DynaTech
  - FinalTECH/FinalTech
```

- Please check the name of addon "FinalTECH" as FinalTECH(Capital) may not be in the default pluginlist of slimecustomizer, If you insist on installing FinalTECH instead of FinalTech, please enable it in the plugins.yml in slimecustomizer.jar and disable auto-update .

- The version of FinalTECH used for the development is FinalTECH 2.0-preview

> We don't suggest that you install high version of FinalTECH

- FinalTECH.jar is provided in our repository used for development
- Modified slimecustomizer.jar is provided in our repository used for development

## Install these slimecustomizers as depend:
```
  - HaimanTech
```
- The version of HaimanTech used for the development is Beta1.6

- Configs of HaimanTech are provided in our repository used for development

- You can find the [latest version of HaimanTech here](https://github.com/haiman233/HaimanTech2)



Mark:

 - The config of LogicTECH should be placed after all dependent's sc-config

- If you know how to use python ,you can use 'combine_sc.py' provided

-  ~~We will make a better combiner later~~

# About this slimeCustomizer
## The Aim
- LogicTech is a slimeCustomizer depend mainly on FinalTECH
- As we all know ,FinalTECH's powerful machines like STORAGE_AND_TRANSFER and ITEM_DISMANTLE_TABLE often make server sft worse
- So we aimed to reduce machine number and server lag by increasing the complexity of crafting-recipe and crafting-process
- And make compressed machines with high productivity to provide players better gaming experience
- Also ,we aimed to reduce the CRAFTER player used,by transfering crafting-path
## How
- LogicTech aims to abstract the logic of the complex producing line and reflect it in the complexity of the crafting recipes.
- By creating YITIJI(all_in_one_machine) and COMPRESSED_MACHINE(many_in_one)
## About FinalTech
- LogicTech is based mainly on FinalTech v2 -preview
- I know that some items and machines are overpowered in FinalTECH, like MATRIX_REACTOR and PHONY
- This slimecustomizer CAN work if MATRIX_REACTOR are banned
- And it will probably reduce the number of FINALTECH_TRANSFER, DISMANTLE_TABLE, NTW_CRAFTER and other FinalTECH machines placed in world

## About version
- See detailed information in README.txt
  
