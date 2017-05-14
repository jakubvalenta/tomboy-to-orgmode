import argparse
from datetime import datetime
import glob
import operator
import os.path
import re
import sys
import textwrap
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


def parse_timestamp(s: str) -> datetime:
    simpler = re.sub('\.\d+(\S\d+)\:(\d+)$', '\\1\\2', s)
    return datetime.strptime(simpler, '%Y-%m-%dT%H:%M:%S%z')


def parse_note(path: str) -> Note:
    with open(path, 'rb') as f:
        doc = BeautifulSoup(f, 'xml')
    raw_title = doc.find(name='title').text
    raw_text = doc.find(name='text').text
    raw_timestamp = doc.find(name='last-change-date').text
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
        content=textwrap.indent(content, '  ')
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
