import sqlite3
import unittest
from get_user_media import WebScrapper
from webscraper import get_all_relevant_data
from defines import get_creds
from statistics import (
    engagment_per_post,
    engagment_per_follower,
    reach_rate,
)


class TestWebscraperAndStatisticsMethods(unittest.TestCase):
    # This tests wether the engagment_per_post formula works as intended.
    def test_engagment_per_post(self):
        self.assertEqual(0.5, engagment_per_post(5, 10))
        self.assertEqual(0.5, engagment_per_post(50, 100))
        self.assertEqual(0.3, engagment_per_post(300, 1000))

    # This tests wether the engagment_per_follower fromula works as intended.
    def test_engagment_per_follower(self):
        self.assertEqual(0.5, engagment_per_follower(5, 10))
        self.assertEqual(0.5, engagment_per_follower(50, 100))
        self.assertEqual(0.3, engagment_per_follower(300, 1000))

    # This tests the reach_rate function works as intended.
    def test_reach_rate(self):
        self.assertEqual(50, reach_rate(5, 10))
        self.assertEqual(50, reach_rate(50, 100))
        self.assertEqual(30, reach_rate(300, 1000))
