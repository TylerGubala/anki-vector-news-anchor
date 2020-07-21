#!/usr/bin/env python3
#coding: utf-8
#STD LIB imports
from datetime import datetime
from typing import Iterator
#PYPI imports
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.utils import get_stop_words

LANGUAGE = "english"

class Story():
    def __init__(self, title: str, description: str, syndicate: str,
                 link: str, hostname: str, publish_date: datetime):
        self.title = title
        self.description = description
        self.syndicate = syndicate
        self.link = link
        self.hostname = hostname
        self.publish_date = publish_date
    def get_summary(self, summary_length: int = 10) -> Iterator[str]:
        parser = HtmlParser.from_url(self.link, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        for sentence in summarizer(parser.document, summary_length):
            yield sentence
