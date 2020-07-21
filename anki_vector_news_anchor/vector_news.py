#!/usr/bin/env python3
#coding: utf-8
#STD Lib imports
from typing import Iterator
from urllib.parse import urlparse
from urllib.request import urlopen
#PYPI imports
import bs4
from bs4 import BeautifulSoup as soup
from dateutil import parser as dateparser
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.utils import get_stop_words
#LOCAL imports
from anki_vector_news_anchor.story import LANGUAGE

class RedditPost():
    def __init__(self, author: str, post: str, link: str, content: str):
        self.author = author
        self.post = post
        self.link = link
        self.content = content
    def get_summary(self, summary_length: int = 10) -> Iterator[str]:
        parser = HtmlParser.from_string(self.content, Tokenizer(LANGUAGE), self.link)
        stemmer = Stemmer(LANGUAGE)
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        for sentence in summarizer(parser.document, summary_length):
            yield sentence

def get_reddit_vector_posts(url: str = 
                           "https://www.reddit.com/r/AnkiVector/"
                           ".rss") -> Iterator[RedditPost]:
    with urlopen(url= url) as reddit_feed:
        reddit_xml = reddit_feed.read()
        reddit_soup = soup(reddit_xml, "xml")
        for entry in reddit_soup.findAll("entry"):
            author = entry.author.find("name").text[3:]
            post = entry.title.text
            content = entry.content.text
            yield RedditPost(author, post, entry.link.text, content)
