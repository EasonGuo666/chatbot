# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:16:26 2019

@author: Guo
"""

'''
重新训练模型需要先删除sample下的.pkl和model下的一堆文件，否则会按照保存的模型继续
训练：命令输入:--corpus lightweight --datasetTag chat
测试：命令输入:--test
         或者:--test interactive
'''

from chatbot import chatbot


if __name__ == "__main__":
    chatbot = chatbot.Chatbot()
    chatbot.main()
