#!/usr/bin/env python3
#coding: utf-8
#STDLIB imports
import os
import random
import re
from typing import Iterator, List
#LOCAL imports
from anki_vector_news_anchor import READ_FILE_FLAG
from anki_vector_news_anchor.story import Story

STRIP_UNSPEAKABLES_PATTERN = r"([^\d\s\w\$\-=+/\%!?\.,()＠@[\]<>＃#'\":;]|_)+"
STRIP_UNSPEAKABLES_REGEX = re.compile(STRIP_UNSPEAKABLES_PATTERN, re.UNICODE)

HASHTAG_PATTERN = r"(?:^|\s)[＃#]{1}(\w+)"
HASHTAG_REGEX = re.compile(HASHTAG_PATTERN, re.UNICODE)

MENTION_PATTERN = r"(?:^|\s)[＠@]{1}([^\s#<>[\]|{}]+)"
MENTION_REGEX = re.compile(MENTION_PATTERN, re.UNICODE)

def get_speakable_text(text: str) -> str:
    return re.sub(r"’",  "'", re.sub(r"[“”]", "\"", re.sub(r"\s+", " ", re.sub(HASHTAG_REGEX, r" hash tag \1", 
                  re.sub(STRIP_UNSPEAKABLES_REGEX, "", str(text)))
           .replace("&", " and ")
           .replace("+", " plus ")
           .replace("=/=", " does not equal ")
           .replace(r"=\\=", " does not equal ")
           .replace("=", " equals ")
           .replace("%", " percent ")
           .replace("@", " at ")
           .replace("/", " slash ")
           .replace(r"\\", " slash ")))).strip()

def get_brief_description_lead_in_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "brief_description_lead_in_phrases.txt"), READ_FILE_FLAG).readlines()

def get_introductory_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "introductory_phrases.txt"), READ_FILE_FLAG).readlines()

def get_outro_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "outro_phrases.txt"), READ_FILE_FLAG).readlines()

def get_outer_space_news_segment_lead_in_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "outer_space_news_segment_lead_in_phrases.txt"), READ_FILE_FLAG).readlines()

def get_sports_news_segment_lead_in_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "sports_news_segment_lead_in_phrases.txt"), READ_FILE_FLAG).readlines()
                             
def get_world_news_segment_lead_in_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "world_news_segment_lead_in_phrases.txt"), READ_FILE_FLAG).readlines()

def get_story_lead_in_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "story_lead_in_phrases.txt"), READ_FILE_FLAG).readlines()

def get_story_lead_out_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "story_lead_out_phrases.txt"), READ_FILE_FLAG).readlines()

def get_story_citation_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "story_citation_phrases.txt"), READ_FILE_FLAG).readlines()

def get_unknown_source_apology_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "unknown_source_apology_phrases.txt"), READ_FILE_FLAG).readlines()

def get_vector_news_segment_lead_in_phrases() -> List[str]:
    return open(os.path.join("resources", "data", "parts_of_speech", 
                             "vector_news_segment_lead_in_phrases.txt"), READ_FILE_FLAG).readlines()

def get_announcement_from_story(story: Story) -> str:
    speakable_title = story.title \
        if story.title[-1] in ["?", "!", "."] else story.title+"."
    speakable_hostname = None
    if story.hostname:
        speakable_hostname = story.hostname.replace(".", " dot ")
    return " ".join([random.choice(get_story_lead_in_phrases()), 
                    speakable_title,
                    random.choice(get_story_lead_out_phrases()), 
                    " ".join([random.choice(get_story_citation_phrases()), 
                              speakable_hostname]) if speakable_hostname 
                              else random.choice(get_unknown_source_apology_phrases())])

def get_announcements_from_stories(stories: List[Story]) -> Iterator[str]:
    for story in stories:
        yield get_announcement_from_story(story)
