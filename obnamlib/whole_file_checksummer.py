# Copyright 2016  Lars Wirzenius
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
#
# =*= License: GPL-3+ =*=


import hashlib

import obnamlib


class WholeFileCheckSummer(object):

    '''Compute a whole-file checksum.

    Ask the repository its preferred checksum algorithm. Use that.

    If the algorithm is MD5, compute the checksum from all the bytes
    in the file. For everything else, compute the checksum from (size,
    checksum) pairs for all the chunks in the file. This convoluted
    thing is because the latter is necessary for speed, and the former
    is necessary for backwards compatibilty.

    '''

    def __init__(self, repo):
        self._summer = self._create_checksum_algorithm(repo)

    def _create_checksum_algorithm(self, repo):
        file_key = repo.get_file_checksum_key()
        if file_key is None:
            return _NullChecksum()
        name = obnamlib.get_checksum_algorithm_name(file_key)
        return obnamlib.get_checksum_algorithm(name)

    def append_chunk(self, chunk_data, token):
        self._summer.update(chunk_data)

    def get_checksum(self):
        '''Get the current whole-file checksum.'''
        return self._summer.hexdigest()


class _NullChecksum(object):

    def update(self, data):
        pass

    def hexdigest(self):
        return None
