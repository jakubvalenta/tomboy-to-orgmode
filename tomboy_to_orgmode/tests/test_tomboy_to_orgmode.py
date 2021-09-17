from io import StringIO
from pathlib import Path
from unittest import TestCase

from tomboy_to_orgmode.tomboy_to_orgmode import tomboy_to_orgmode


class TestTomboyToOrgmode(TestCase):
    def test_tomboy_to_orgmode(self):
        path = Path(__file__).parent / 'test_data'
        out = StringIO()
        tomboy_to_orgmode(path, out)
        out.seek(0)
        self.assertEqual(
            out.read(),
            '''* Note with missing date

Spam

<2021-09-17 Fri>

* Nested note with missing text



<2018-07-13 Fri>

* Note with first line of text same as title



<2018-07-13 Fri>

* Basic note

Foo

bar

baz

<2018-04-22 Sun>

''',
        )
