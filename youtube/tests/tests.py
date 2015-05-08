from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
import mock
import json


YOUTUBE_RESULTS = {
    'nextPageToken': "CBkQAA",
    'kind': "youtube#searchListResponse",
    'pageInfo': {
        'resultsPerPage': 25,
        'totalResults': 1000000
    },
    'items': [{
        'snippet': {
            'title': "Some title 1",
            'channelId': "UCplkk3J5wrEl0TNrthHjq4Q",
            'liveBroadcastContent': "none",
            'channelTitle': "ChannelTitle 1",
            'description': "Some description 1"
        },
        'kind': "youtube#searchResult",
        'id': {
            'kind': "youtube#video",
            'videoId': 1
        }
    }, {
        'snippet': {
            'title': "Some title 2",
            'channelId': "UCplkk3J5wrEl0TNrthHjq4Q",
            'liveBroadcastContent': "none",
            'channelTitle': "ChannelTitle 2",
            'description': "Some description 2"
        },
        'kind': "youtube#searchResult",
        'id': {
            'kind': "youtube#channel",
            'videoId': 2
        }
    }, {
        'snippet': {
            'title': "Some title 3",
            'channelId': "UCplkk3J5wrEl0TNrthHjq4Q",
            'liveBroadcastContent': "none",
            'channelTitle': "ChannelTitle 3",
            'description': "Some description 3"
        },
        'kind': "youtube#searchResult",
        'id': {
            'kind': "youtube#playlist",
            'videoId': 3
        }
    }]
}


class YoutubeTests(TestCase):

    def setUp(self):
        self.client = Client()

    def assert_successful_json_response(self, response):
        self.assertEqual(200, response.status_code)
        self.assertEqual("application/json", response['content-type'])

    @mock.patch('youtube.api.youtube_search')
    def test_search_filter(self, mock_youtube_search):
        mock_youtube_search.return_value = YOUTUBE_RESULTS
        url = reverse('search', kwargs={})
        res_types = ('video', 'channel', 'playlist')

        for res_type in res_types:
            response = self.client.get(
                '{0}?search_term=test&restype={1}'.format(url, res_type))
            self.assert_successful_json_response(response)
            data = json.loads(response.content)
            for item in data['items']:
                self.assertEquals(
                    item['id']['kind'], 'youtube#{}'.format(res_type))

    @mock.patch('youtube.api.youtube_search')
    def test_search_param(self, mock_youtube_search):
        mock_youtube_search.return_value = YOUTUBE_RESULTS
        url = reverse('search', kwargs={})
        search_term = '~!@#$%^&*() <>:"?,./{}[]|\\_-+='

        response = self.client.get(
            '{0}?search_term={1}'.format(url, search_term))
        self.assert_successful_json_response(response)

        search_term = ''
        response = self.client.get(
            '{0}?search_term={1}'.format(url, search_term))
        self.assert_successful_json_response(response)
