#!/usr/bin/env python3
#coding: utf-8
#standardlibraryimports
from asyncio import CancelledError
import random
import time
#PYPI IMPORTS
from anki_vector import Robot
from anki_vector.util import degrees, distance_mm, speed_mmps
#LOCAL IMPORTS
from anki_vector_news_anchor.outer_space_news import get_outer_space_news
from anki_vector_news_anchor.sports_news import get_sports_news
from anki_vector_news_anchor.vector_news import get_reddit_vector_posts
from anki_vector_news_anchor.world_news import get_world_news
from anki_vector_news_anchor.speech import get_speakable_text,\
                                           get_brief_description_lead_in_phrases,\
                                           get_introductory_phrases,\
                                           get_announcement_from_story,\
                                           get_announcements_from_stories,\
                                           get_outer_space_news_segment_lead_in_phrases,\
                                           get_outro_phrases,\
                                           get_sports_news_segment_lead_in_phrases,\
                                           get_vector_news_segment_lead_in_phrases,\
                                           get_world_news_segment_lead_in_phrases
from anki_vector_news_anchor.vector_news import get_reddit_vector_posts

def main():
    with Robot() as vector:
        vector.behavior.drive_on_charger()
        vector.behavior.drive_off_charger()
        vector.behavior.drive_straight(distance_mm(150), speed_mmps(25))
        vector.behavior.turn_in_place(degrees(180), degrees(45), 
                                      degrees(5), degrees(5))
        # ^ If vector's base is facing away from the camera
        vector.anim.play_animation_trigger(random.choice(["GreetAfterLongTime", "PRDemoGreeting", "ReactToGoodMorning", "ReactToGreeting"]))
        vector.behavior.say_text(get_speakable_text(random.choice(get_introductory_phrases())))
        vector.behavior.say_text(get_speakable_text(random.choice(get_world_news_segment_lead_in_phrases())))
        vector.anim.play_animation_trigger("ExploringQuickScan")
        for story in get_world_news():
            announcement = get_announcement_from_story(story)
            vector.behavior.say_text(get_speakable_text(announcement))
            vector.anim.play_animation_trigger(random.choice(["NeutralFace",
                                                              "NothingToDoBoredIdle",
                                                              "ObservingIdleEyesOnly",
                                                              "ObservingIdleWithHeadLookingStraight",
                                                              "ObservingIdleWithHeadLookingUp",
                                                              "ObservingLookStraight",
                                                              "ObservingLookUp",
                                                              "LookAround"]))
            vector.behavior.say_text(get_speakable_text(random.choice(get_brief_description_lead_in_phrases())))
            for sentence in story.get_summary():
                vector.behavior.say_text(get_speakable_text(sentence))
        vector.behavior.say_text(get_speakable_text(random.choice(get_sports_news_segment_lead_in_phrases())))
        for announcement in [_announcement for _announcement in get_announcements_from_stories(get_sports_news())][:3]:
            vector.behavior.say_text(get_speakable_text(announcement))
        vector.behavior.say_text(random.choice(get_outer_space_news_segment_lead_in_phrases()))
        for announcement in [_announcement for _announcement in get_announcements_from_stories(get_outer_space_news())][:3]:
            vector.behavior.say_text(get_speakable_text(announcement))
        vector.behavior.say_text(get_speakable_text(random.choice(get_vector_news_segment_lead_in_phrases())))
        for post in [_post for _post in get_reddit_vector_posts()][:3]:
            vector.behavior.say_text(get_speakable_text(f"Here is one by {post.author} (thank you, {post.author}). It's titled: {post.post}."))
            vector.behavior.say_text(random.choice(get_brief_description_lead_in_phrases()))
            for sentence in post.get_summary():
                vector.behavior.say_text(get_speakable_text(sentence))
        vector.behavior.say_text(get_speakable_text(random.choice(get_outro_phrases())))
        vector.anim.play_animation_trigger(random.choice(["Feedback_ILoveYou",
                                                          "Feedback_GoodRobot",
                                                          "LookAtUserEndearingly",
                                                          "OnboardingReactToFaceHappy",
                                                          "OnboardingLookAtUser",
                                                          "ReactToGoodBye",
                                                          "ReactToGoodNight"]))
        vector.behavior.drive_on_charger()

def main2():
    for story in get_world_news():
        announcement = get_announcement_from_story(story)
        print(get_speakable_text(announcement))
        for sentence in story.get_summary():
            print(get_speakable_text(sentence))

if __name__ == "__main__":
    main()