# coding: utf-8

"""
    GIPHY Public API

    A test of what Giphy API docs would look like in Gelato

    OpenAPI spec version: 0.9.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import json
import unittest
import collections

import giphy_client
from giphy_client.rest import ApiException
from giphy_client.apis.default_api import DefaultApi

NoneType = type(None)

KEY = "dc6zaTOxFJmzC"

def flatten(value, key="", sep="."):
    """
    Flattens potentially nested dictionaries into a single flat list of key/value pairs.
    Similiar to dict.items() except it works for nested dictionaries, and all keys start with ".".
    """
    def unhandled_type():
        raise Exception("unhandled type " + str(type(value)))
    return (
            ({
                str: lambda: [(key, value)],
                unicode: lambda: [(key, value)],
                int: lambda: [(key, value)],
                float: lambda: [(key, value)],
                NoneType: lambda: [(key, value)],
                bool: lambda: [(key, value)],
                list:
                    lambda: [
                        item
                        for sublist in [
                            flatten(v, key="")
                            for v in value
                        ]
                        for item in sublist
                    ],
                dict:
                    lambda: [
                        item
                        for sublist in [
                            flatten(v, key=".".join([key, k]))
                            for k,v in value.items()
                        ]
                        for item in sublist
                    ],
            }).get(type(value), unhandled_type)()
    )

class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = giphy_client.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def _validate(self, obj):
        """
        Looks through every key in every object to check for null values.
        If a null value is found where it shouldn't be we raise an exception and the test fails.
        Keys included in `exclude_keys` are ignored, meaning they may be null.
        """
        exclude_keys = [

            # these keys should always be present
            #  ".rating",
            #  ".source_tld",
            #  ".bitly_url",
            #  ".embed_url",
            #  ".content_url",
            #  ".source_post_url",
            #  ".images",
            #  ".slug",
            #  ".url",
            #  ".id",
            #  ".source",
            #  ".username",
            #  ".bitly_gif_url",
            #  ".import_datetime",

            # these keys are sometimes null
            ".pagination.offset",
            ".pagination.total_count",
            ".is_featured",
            ".is_hidden",
            ".is_anonymous",
            ".is_community",
            ".is_removed",
            ".is_realtime",
            ".is_indexable",
            ".is_sticker",
            ".update_datetime",
            ".create_datetime",
            ".trending_datetime",
            ".tags",
            ".featured_tags",
            ".user",
            ".user.twitter",
            ".gif.is_featured",
            ".gif.is_removed",
            ".gif.is_hidden",
            ".gif.is_anonymous",
            ".gif.is_community",
            ".gif.is_sticker",
            ".gif.is_indexable",
            ".gif.is_realtime",
            ".gif.user",
            ".gif.user.twitter",
        ]
        items = flatten(obj.to_dict() if (type(obj) is not dict) else obj)
        #  print items
        for key, value in items:
            if (key not in exclude_keys) and (value is None):
                raise AssertionError("%s == null" % key, json.dumps(obj, default=lambda _: _.to_dict()))
                #  raise AssertionError("%s == null" % key)

    def test_gifs_categories_get(self):
        """
        Test case for gifs_categories_get

        Categories Endpoint.
        """
        r = self.api.gifs_categories_get(KEY, limit=10)
        self._validate(r)
        self.assertEqual(len(r.data), 10) 

    def test_gifs_categories_category_get(self):
        """
        Test case for gifs_categories_category_get

        Category Tags Endpoint.
        """
        r = self.api.gifs_categories_category_get(KEY, "actions", limit=10, offset=0)
        self._validate(r)
        self.assertEqual(len(r.data), 10)

    def test_gifs_categories_category_tag_get(self):
        """
        Test case for gifs_categories_category_tag_get

        Tagged Gifs Endpoint.
        """
        r = self.api.gifs_categories_category_tag_get(KEY, "actions", "crying", limit=10, offset=0)
        self._validate(r)
        self.assertEqual(len(r.data), 10)

    def test_gifs_get(self):
        """
        Test case for gifs_get

        Get GIFs by ID Endpoint
        """
        r = self.api.gifs_get(KEY, "YfCuW2maPixri,BeL3iFbYzAsfu")
        self._validate(r)
        self.assertEqual(len(r.data), 2)

    def test_gifs_gif_id_get(self):
        """
        Test case for gifs_gif_id_get

        Get GIF by ID Endpoint
        """
        r = self.api.gifs_gif_id_get(KEY, "YfCuW2maPixri")
        self._validate(r.data)

    def test_gifs_random_get(self):
        """
        Test case for gifs_random_get

        Random Endpoint
        """
        r = self.api.gifs_random_get(KEY)
        self._validate(r)

    def test_gifs_search_get(self):
        """
        Test case for gifs_search_get

        Search Endpoint
        """
        r = self.api.gifs_search_get(KEY, "cats", limit=25, offset=0)
        self._validate(r)
        self.assertEqual(len(r.data), 25)

    def test_gifs_translate_get(self):
        """
        Test case for gifs_translate_get

        Translate Endpoint
        """
        r = self.api.gifs_translate_get(KEY, "cats")
        self._validate(r.data)

    def test_gifs_trending_get(self):
        """
        Test case for gifs_trending_get

        Trending GIFs Endpoint
        """
        r = self.api.gifs_trending_get(KEY, limit=25)
        self._validate(r)
        self.assertEqual(len(r.data), 25)

    def test_stickers_random_get(self):
        """
        Test case for stickers_random_get

        Random Sticker Endpoint
        """
        r = self.api.stickers_random_get(KEY)
        self._validate(r)

    def test_stickers_search_get(self):
        """
        Test case for stickers_search_get

        Sticker Search Endpoint
        """
        r = self.api.stickers_search_get(KEY, "cats", limit=25)
        self._validate(r)
        self.assertEqual(len(r.data), 25)

    def test_stickers_translate_get(self):
        """
        Test case for stickers_translate_get

        Sticker Translate Endpoint
        """
        r = self.api.stickers_translate_get(KEY, "cats")
        self._validate(r.data)

    def test_stickers_trending_get(self):
        """
        Test case for stickers_trending_get

        Trending Stickers Endpoint
        """
        r = self.api.stickers_trending_get(KEY, limit=25)
        self._validate(r)
        self.assertEqual(len(r.data), 25)


if __name__ == '__main__':
    unittest.main()
