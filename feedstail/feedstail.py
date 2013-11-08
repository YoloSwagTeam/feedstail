# -*- coding: utf-8 -*-
# Copyright (C) 2011 Romain Gauthier <romain.gauthier@masteri2l.org>
# Copyright (C) 2011 Laurent Peuch <cortex@worlddomination.be>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Import from the standard library
import re

# Import from FeedParser
from feedparser import parse
from config import Config

def isnew(tail, config, entry):
    if config.key not in entry:
        if config.ignore_key_error:
            return False
        raise FeedKeyError(config.key)

    for item in tail:
        if entry[config.key] == item[config.key]:
            return False
    return True


def show(config, entry):
    try:
        output = config.formatFct(entry)
        if config.no_endl:
            output = re.sub(r"[\t\r\n\s]+", r" ", output)
    except KeyError, key:
        raise FeedKeyError(key.args[0])
    else:
        return output.encode('utf-8')

def feedGenerator(config):
    def cycle(tail, number=None):
        result = []
        try:
            entries = parse(config.url, agent="FeedsTail/0.* +https://gitorious.org/feedstail").entries
        except MemoryError:
            return

        if config.reverse:
            entries.reverse()

        if number is not None and number <= len(entries):
            for entry in entries[number:]:
                tail = [entry] + tail[:100]
            entries = entries[:number]

        for entry in entries:
            if isnew(tail, config, entry):
                tail = [entry] + tail[:100]
                result.append( show(config, entry) )
        return (tail, result)

    tail = []
    (tail, result) = cycle(tail, config.number)
    yield result
    while True:
        (tail, result) = cycle(tail)
        yield result


class FeedKeyError(KeyError):

    def __init__(self, key):
        self.key = key


    def __str__(self):
        return str(self.key)
