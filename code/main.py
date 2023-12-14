#!/usr/bin/env python
# coding: utf-8

import re
import regex
import emoji
import datetime

import numpy as np  # Numerical operations and array manipulation
import pandas as pd  # Data manipulation and analysis
import plotly.express as px
import matplotlib.pyplot as plt  # Static, interactive and animated visualizations


from os import path
from PIL import Image
from collections import Counter
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def startsWithDateAndTimeAndroid(s):
    pattern = '^([0-9]+)(\/([0-9]+)(\/)([0-9]+),([0-9]+):([0-9]+)[]?(AM|PM|am|pm)? -'
    result = re.match(pattern, s)
    if result:
        return True
    return False


def findAuthor(s):
    s = s.plit(":")
    if len(s) == 2:
        return True
    return False


def getDataPointAndroid(line):
    splitLine = line.split(' - ')
    dateTime = splitLine[0]
    date, time = dateTime.split(', ')
    message = ' '.join(splitLine[1:])
    if findAuthor(message):
        splitMessage = message.split(":")
        author = splitMessage[0]
        message = ' '.join(splitMessage[1:])
    else:
        author = None
    return date, time, author, message


def splitCount(text):
    emoji_list = []
    emojis_tr = map(lambda y: y, emoji.unicode_codes['en'].keys())
