# -*- coding: utf-8 -*-
# @Time    : 2017/10/22 20:01
# @Author  : Mrxn
# @File    : run.py
# @Software: PyCharm
# @Desc     :The DeFault DeSc for Mrxn
# @license : Copyright(C), Mrxn
# @Contact : admin@mrxn.net
# @Blog    : https://mrxn.net


from scrapy import cmdline


name = 'douban_movie_top250'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())