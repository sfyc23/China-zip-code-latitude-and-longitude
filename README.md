汉字五笔转换工具（Python 版）
=============================
[![pypi](https://img.shields.io/badge/pypi-0.0.1-yellow.svg)](https://pypi.org/project/pywubi) 
![python_vesion](https://img.shields.io/badge/python-%3E3-green.svg)  

   
将汉字转为五笔码。现只支持 86 版编码。（ps:因为找到整理出 86 版五笔编码）

## 关于

* GitHub: https://github.com/sfyc23/python-wubi  
* License: MIT license  
* PyPI: https://pypi.org/project/pywubi  
* Python version: 3

## 特性

1. 将词组转成五笔编码。比如词语：生死有命。换成五笔码为：'tgdw'；
2. 返回汉字的所有可能的编码。如汉字：为 。换成五笔码为： 'ylyi', 'yly', 'yl', 'o'；
3. 将一段句子，转成五笔码。如:天气不错，我们去散步吧!：五笔码为：'gdi', 'rnb', 'gii', 'qajg', '，', 'trnt', 'wun', 'fcu', 'aety', 'hir', 'kcn', '!'

## 安装

    $ pip install pywubi

## 使用示例

    >>> from pywubi import wubi
    >>> wubi('我爱你')
    ['trnt', 'epdc', 'wqiy']
    >>> wubi('我爱你',multicode=True)  # 返回汉字的所有可能的五笔编码
    [['trnt', 'trn', 'q'], ['epdc', 'epd', 'ep'], ['wqiy', 'wqi', 'wq']]
    >>> wubi('我爱你', single=False) # 以词组的方法处理这些汉字
    ['tewq']

## Lincese

    MIT License

    Copyright (c) 2019  Thunder Bouble
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
