中国地区邮编经纬度/工具（Python 版）
=============================
[![pypi](https://img.shields.io/badge/pypi-0.0.11-yellow.svg)](https://pypi.org/project/china-region/) 
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
    # 获取满足条件的所有地址
    >>> import china_region
    >>> china_region.search_all(county='华安')
    [{'province': '福建省', 'city': '漳州市', 'county': '华安县', 'longitude': 117.53, 'latitude': 25.02, 'zipCode': '363800'}]
    >>> china_region.search_all(province='福建省',city='华安')
    [{'province': '福建省', 'city': '漳州市', 'county': '华安县', 'longitude': 117.53, 'latitude': 25.02, 'zipCode': '363800'}]
    >>> china_region.search_all(province='贵州',city='贵阳',county='白云')
    [{'province': '贵州省', 'city': '贵阳市', 'county': '白云区', 'longitude': 106.65, 'latitude': 26.68, 'zipCode': '550014'}]

    # 获取满足条件的第一个地址
    >>> china_region.search('辽宁 铁岭')
    {'province': '辽宁省', 'city': '铁岭市', 'county': '铁岭市', 'longitude': 123.83, 'latitude': 42.28, 'zipCode': '112000'}
    
    # 获取一个随机的地址
    >>> china_region.sample()
    {'province': '山西省', 'city': '临汾市', 'county': '洪洞县', 'longitude': 111.67, 'latitude': 36.25, 'zipCode': '041600'}

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
    
