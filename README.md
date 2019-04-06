中国地区邮编经纬度/工具（Python 版）
=============================
[![pypi](https://img.shields.io/badge/pypi-0.0.8-yellow.svg)](https://pypi.org/project/china-region/) 
![python_vesion](https://img.shields.io/badge/python-%3E3-green.svg)  

   
根据省市区获取中国经纬度和邮编

## 关于

* GitHub: https://github.com/sfyc23/China-zip-code-latitude-and-longitude  
* License: MIT license  
* PyPI: https://pypi.org/project/china-region/ 
* Python version: >= 3.5

## 特性

1. 根据省市区获取经纬度和邮编。


## 安装

    $ pip install china-region

## 依赖库

    pandas>=0.23.4

## 升级

    $ pip install -U china-region

## 使用示例
```
    >>> import china_region
    >>> china_region.search(county='全州')
    [{'province': '广西壮族自治区', 'city': '桂林市', 'county': '全州县', 'longitude': 111.07, 'latitude': 25.93, 'zipCode': '541500'}]
    >>> china_region.search(province='广西省',city='桂林')
    [{'province': '广西壮族自治区', 'city': '桂林市', 'county': '桂林市', 'longitude': 110.28, 'latitude': 25.28, 'zipCode': '541000'}]
    >>> china_region.search(province='广西省',city='桂林',county='兴安')
    [{'province': '广西壮族自治区', 'city': '桂林市', 'county': '兴安县', 'longitude': 110.67, 'latitude': 25.62, 'zipCode': '541399'}]
```

## 资源文件

* [region.csv](https://github.com/sfyc23/China-zip-code-latitude-and-longitude/blob/c60a0d5ebeabbe4e316105b0f12a036e12928d9d/resource/region.csv)
* [region.txt](https://github.com/sfyc23/China-zip-code-latitude-and-longitude/blob/c60a0d5ebeabbe4e316105b0f12a036e12928d9d/resource/region.txt)
* [region.json](https://github.com/sfyc23/China-zip-code-latitude-and-longitude/blob/c60a0d5ebeabbe4e316105b0f12a036e12928d9d/resource/region.json)

```
北京市	北京市	北京市	116.4	39.9	100000
北京市	北京市	东城区	116.42	39.93	100010
北京市	北京市	西城区	116.37	39.92	100032
北京市	北京市	崇文区	116.43	39.88	100000
北京市	北京市	宣武区	116.35	39.87	100000
北京市	北京市	朝阳区	116.43	39.92	100020
北京市	北京市	丰台区	116.28	39.85	100071
```

相似项目: [https://github.com/radiocontroller/china-location](https://github.com/radiocontroller/china-location)

## Lincese

    MIT License
    
    Copyright (c) 2019  Thunder Bouble
    
