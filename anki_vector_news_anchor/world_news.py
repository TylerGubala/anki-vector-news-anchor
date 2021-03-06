#!/usr/bin/env python3
#coding: utf-8
#STD Lib imports
from datetime import datetime
from typing import Iterator
from urllib.parse import urlparse
from urllib.request import urlopen
#PYPI imports
import bs4
from bs4 import BeautifulSoup as soup
from dateutil import parser as dateparser
#LOCAL imports
from anki_vector_news_anchor.story import Story

def get_world_news(url: str = 
                   "https://news.google.com/news/rss") -> Iterator[Story]:
    with urlopen(url= url) as news_feed:
        news_xml = news_feed.read()
        news_soup = soup(news_xml, "xml")
        for item in news_soup.findAll("item"):
            title = "".join(item.title.text.split("-")[:-1]).strip()
            description = soup(item.description.text, "xml").get_text()
            syndicate = item.title.text.split("-")[-1].strip()
            publish_date = dateparser.parse(item.pubDate.text)
            hostname = urlparse(item.link.text).hostname
            yield Story(title, description, syndicate, item.link.text, hostname, 
                        publish_date)
