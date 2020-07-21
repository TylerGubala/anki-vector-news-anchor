#!/usr/bin/env python3
#coding: utf-8
#STD Lib imports
import re
from typing import Iterator
from urllib.parse import urlparse
from urllib.request import urlopen
#PYPI imports
import bs4
from bs4 import BeautifulSoup as soup
from dateutil import parser as dateparser
#LOCAL imports
from anki_vector_news_anchor.speech import STRIP_UNSPEAKABLES_REGEX
from anki_vector_news_anchor.world_news import Story

def get_outer_space_news(url: str = "https://www.jpl.nasa.gov/multimedia/rss/"
                         "news.xml") -> Iterator[Story]:
    with urlopen(url= url) as news_feed:
        news_xml = news_feed.read()
        news_soup = soup(news_xml, "xml")
        for item in news_soup.findAll("item"):
            title = item.title.text
            description = soup(item.description.text, "xml").get_text()
            hostname = urlparse(url).hostname
            syndicate = None
            if hostname:
                syndicate = hostname.upper()
            publish_date = dateparser.parse(item.pubDate.text)
            yield Story(title, description, syndicate, item.link.text,
                        hostname, publish_date)