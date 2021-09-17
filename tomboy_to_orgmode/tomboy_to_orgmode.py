import argparse
import operator
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import IO, List

import pytz
from bs4 import BeautifulSoup


@dataclass
class Note:
    title: str
    text: str
    timestamp: datetime


def find_notes_paths(path: Path) -> List[Path]:
    return sorted(path.glob('**/*.note'))


def parse_timestamp(s: str) -> datetime:
    simpler = re.sub(r'\.\d+(\S\d+)\:(\d+)$', '\\1\\2', s)
    return datetime.strptime(simpler, '%Y-%m-%dT%H:%M:%S%z')


def parse_note(path: Path) -> Note:
    with path.open('rb') as f:
        doc = BeautifulSoup(f, 'xml')
    raw_title = doc.find(name='title').text
    raw_text = doc.find(name='text').text
    raw_text_lines = raw_text.splitlines()
    if raw_text_lines and raw_text_lines[0] == raw_title:
        raw_text = '\n'.join(raw_text_lines[1:])
    last_change_date = doc.find(name='last-change-date')
    if last_change_date:
        timestamp = parse_timestamp(last_change_date.text)
    else:
        timestamp = datetime.now().replace(tzinfo=pytz.UTC)
    return Note(
        title=raw_title.strip(),
        text=raw_text.strip(),
        timestamp=timestamp,
    )


def format_orgmode_entry(note: Note) -> str:
    timestamp_str = note.timestamp.strftime('%Y-%m-%d %a')
    content = f'{note.text}\n\n<{timestamp_str}>'
    return f'* {note.title}\n\n{content}\n'


def tomboy_to_orgmode(path: Path, out: IO = sys.stdout):
    paths = find_notes_paths(path)
    if not paths:
        print(f'No .note files found in {path}', file=sys.stderr)
        sys.exit(1)
    notes = (parse_note(x) for x in paths)
    notes_from_newest = reversed(
        sorted(notes, key=operator.attrgetter('timestamp'))
    )
    orgmode_entries = (format_orgmode_entry(x) for x in notes_from_newest)
    for orgmode_entry in orgmode_entries:
        print(orgmode_entry, file=out)


def main():
    parser = argparse.ArgumentParser(
        description='Tomboy to org-mode: Convert tomboy notes to an .org file'
    )
    parser.add_argument(
        dest='inputdir', help='path to the directory with the .note files'
    )
    args = parser.parse_args()

    path = Path(args.inputdir)
    tomboy_to_orgmode(path)


if __name__ == '__main__':
    main()
