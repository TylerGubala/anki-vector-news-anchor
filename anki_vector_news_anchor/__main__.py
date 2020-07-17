#!/usr/bin/env python3
#coding: utf-8

from anki_vector_news_anchor.world_news import get_world_news_announcements

def main():
    for announcement in get_world_news_announcements():
        print(announcement)

if __name__ == "__main__":
    main()