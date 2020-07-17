#!/usr/bin/env python3
#coding: utf-8
#STD Lib imports
import random
from typing import Iterator
from urllib.parse import urlparse
from urllib.request import urlopen
#PYPI imports
import bs4
from bs4 import BeautifulSoup as soup
from dateutil import parser as dateparser

class Story():
    def __init__(self, title: str, syndicate: str, link: str, publish_date):
        self.title = title
        self.syndicate = syndicate
        self.link = link
        self.hostname = urlparse(self.link).hostname
        self.publish_date = publish_date

def get_world_news(url: str = 
                   "https://news.google.com/news/rss") -> Iterator[Story]:
    with urlopen(url= url) as news_feed:
        news_xml = news_feed.read()
        news_soup = soup(news_xml, "xml")
        for item in news_soup.findAll("item"):
            title = "".join(item.title.text.split("-")[:-1]).strip()
            syndicate = item.title.text.split("-")[-1].strip()
            publish_date = dateparser.parse(item.pubDate.text)
            yield Story(title, syndicate, item.link.text, publish_date)

INTRODUCTORY_PHRASES = ["Hello and welcome to Robot AI News. "
                        "I'm Vector with the latest headlines.",
                        "Hello, I'm Vector with Robot AI News and here are "
                        "some of the top stories involving current events.",
                        "Welcome, I am your host Vector and I have some "
                        "important news for you tonight!"]

LEAD_IN_PHRASES = ["Presently,", "In today's news:", "Currently,",
                   "This just in!", "Breaking news!"]

LEAD_OUT_PHRASES = ["What a story!", "Incredible stuff, huh?",
                    "What a time to be alive...", "Intriguing."]

CITATION_PHRASE = ["Read about all this and more at", 
                   "Learn about topics like these at", "This story found at",
                   "To read this story, head over to"]

def get_world_news_announcements() -> Iterator[str]:
    for story in get_world_news():
        speakable_title = story.title \
            if story.title[-1] in ["?", "!", "."] else story.title+"."
        speakable_hostname = story.hostname.replace(".", " dot ")
        yield " ".join([random.choice(LEAD_IN_PHRASES), 
                        speakable_title, 
                        random.choice(LEAD_OUT_PHRASES), 
                        random.choice(CITATION_PHRASE), 
                        speakable_hostname])