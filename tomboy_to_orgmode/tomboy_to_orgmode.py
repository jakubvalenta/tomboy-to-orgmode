import argparse
import glob
import operator
import os.path
import re
import sys
import pytz
from datetime import datetime
from typing import Iterator

import attr
from bs4 import BeautifulSoup


@attr.s
class Note:
    title = attr.ib()
    text = attr.ib()
    timestamp = attr.ib()


def find_notes_paths(dirpath: str) -> Iterator[str]:
    globpattern = os.path.join(dirpath, '**/*.note')
    yield from sorted(glob.glob(globpattern, recursive=True))

def stub_timestamp():
    patched = datetime.now().replace(tzinfo=pytz.UTC)
    return datetime.strftime(patched, '%Y-%m-%dT%H:%M:%S%z')

def parse_timestamp(s: str) -> datetime:
    simpler = re.sub(r'\.\d+(\S\d+)\:(\d+)$', '\\1\\2', s)
    return datetime.strptime(simpler, '%Y-%m-%dT%H:%M:%S%z')

def parse_note(path: str) -> Note:
    with open(path, 'rb') as f:
        doc = BeautifulSoup(f, 'xml')
    raw_title = doc.find(name='title').text
    raw_text = doc.find(name='text').text
    raw_text_lines = raw_text.splitlines()
    if raw_text_lines[0] == raw_title:
        raw_text = '\n'.join(raw_text_lines[1:])
    raw_timestamp = doc.find(name='last-change-date').text
    lcd = doc.find(name='last-change-date')
    raw_timestamp = lcd.text if lcd else stub_timestamp()
    return Note(
        title=raw_title.strip(),
        text=raw_text.strip(),
        timestamp=parse_timestamp(raw_timestamp)
    )


def format_orgmode_entry(note: Note) -> str:
    content = '{text}\n\n<{timestamp}>'.format(
        text=note.text,
        timestamp=note.timestamp.strftime('%Y-%m-%d %a')
    )
    return '* {title}\n\n{content}\n'.format(
        title=note.title,
        content=content
    )


def tomboy_to_orgmode(dirpath: str):
    paths = list(find_notes_paths(dirpath))
    if not paths:
        print('No .note files found in {}'.format(dirpath), file=sys.stderr)
        sys.exit(1)
    notes = (parse_note(x) for x in paths)
    notes_from_newest = reversed(
        sorted(notes, key=operator.attrgetter('timestamp'))
    )
    orgmode_entries = (format_orgmode_entry(x) for x in notes_from_newest)
    for orgmode_entry in orgmode_entries:
        print(orgmode_entry)


def main():
    parser = argparse.ArgumentParser(
        description='Tomboy to org-mode: Convert tomboy notes to an .org file'
    )
    parser.add_argument(
        dest='inputdir', help='path to the directory with the .note files')
    args = parser.parse_args()

    tomboy_to_orgmode(args.inputdir)


if __name__ == '__main__':
    main()
