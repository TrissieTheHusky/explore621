import datetime
import json

from django.db.models import Count

from posts.models import Post
from reports.runners.reference import (
    FIRST,
    NOW,
)
from reports.runners.base import BaseRunner


class PostsOverDay(BaseRunner):

    def run(self):
        self.result = {}
        curr = FIRST.date()
        while curr <= NOW.date():
            date = curr.strftime('%Y-%m-%d')
            self.result[date] = 0
            curr += datetime.timedelta(days=1)
        result_set = Post.objects\
            .values('created_at__date')\
            .annotate(count=Count('created_at__date'))
        for result in result_set:
            self.result[result['created_at__date'].strftime('%Y-%m-%d')] =\
                result['count']
        for date, count in self.result.items():
            self.add_datum('day', date, count)

    def generate_result(self):
        self.set_result(json.dumps(self.result))


class PostsOverHourPastWeek(BaseRunner):

    def run(self):
        self.result = {}
        curr = NOW - datetime.timedelta(weeks=1)
        while curr < NOW:
            date = curr.strftime('%Y-%m-%d %H')
            self.result[date] = 0
            curr += datetime.timedelta(hours=1)
        result_set = Post.objects\
            .filter(
                created_at__gt=NOW - datetime.timedelta(weeks=1))\
            .values(
                'created_at__year',
                'created_at__month',
                'created_at__day',
                'created_at__hour')\
            .annotate(count=Count(
                'created_at__day',
                'created_at__hour'))
        for result in result_set:
            date = '{}-{:0>2}-{:0>2} {:0>2}'.format(
                result['created_at__year'],
                result['created_at__month'],
                result['created_at__day'],
                result['created_at__hour'])
            self.result[date] = result['count']
        for hour, count in self.result.items():
            self.add_datum('hour', hour, count)

    def generate_result(self):
        self.set_result(json.dumps(self.result))