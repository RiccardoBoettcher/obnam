# Copyright (C) 2008  Lars Wirzenius <liw@liw.fi>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import unittest

import obnamlib


class HostTests(unittest.TestCase):

    def setUp(self):
        self.host = obnamlib.Host(id="id")

    def test_has_no_genrefs_initially(self):
        self.assertEquals(self.host.genrefs, [])

    def test_has_no_genref_components_initially(self):
        self.assertEquals(self.host.find(kind=obnamlib.GENREF), [])

    def test_allows_appending_to_genrefs(self):
        self.host.genrefs.append("foo")
        self.assertEquals(self.host.genrefs, ["foo"])

    def test_allows_plusequals_to_genrefs(self):
        self.host.genrefs += ["foo"]
        self.assertEquals(self.host.genrefs, ["foo"])

    def test_gets_genrefs_from_components_the_first_time(self):
        genref = obnamlib.GenRef("foo")
        self.host.components = [genref]
        self.assertEquals(self.host.genrefs, ["foo"])

    def test_removes_genrefs_from_components_after_first_get(self):
        genref = obnamlib.GenRef("foo")
        self.host.components = [genref]
        genrefs = self.host.genrefs
        self.assertEquals(self.host.components, [])

    def test_prepare_puts_genrefs_in_components(self):
        self.host.genrefs = ["foo"]
        self.host.prepare_for_encoding()
        self.assertEquals(self.host.find_strings(kind=obnamlib.GENREF),
                          ["foo"])

    def test_has_no_maprefs_initially(self):
        self.assertEquals(self.host.maprefs, [])

    def test_allows_appending_to_maprefs(self):
        self.host.maprefs.append("foo")
        self.assertEqual(self.host.maprefs, ["foo"])

    def test_allows_plusequals_to_maprefs(self):
        self.host.maprefs += ["foo"]
        self.assertEquals(self.host.maprefs, ["foo"])

    def test_gets_maprefs_from_components_the_first_time(self):
        mapref = obnamlib.MapRef("foo")
        self.host.components = [mapref]
        self.assertEquals(self.host.maprefs, ["foo"])

    def test_removes_maprefs_from_components_after_first_get(self):
        mapref = obnamlib.MapRef("foo")
        self.host.components = [mapref]
        genrefs = self.host.maprefs
        self.assertEquals(self.host.components, [])

    def test_prepare_puts_maprefs_in_components(self):
        self.host.maprefs = ["foo"]
        self.host.prepare_for_encoding()
        self.assertEquals(self.host.find_strings(kind=obnamlib.MAPREF),
                          ["foo"])
                          
    def test_prepare_empties_genrefs(self):
        self.host.genrefs = ["foo"]
        self.host.prepare_for_encoding()
        self.assertEquals(self.host._genrefs, None)
                          
    def test_prepare_empties_maprefs(self):
        self.host.maprefs = ["foo"]
        self.host.prepare_for_encoding()
        self.assertEquals(self.host._maprefs, None)

    def test_has_no_contmaprefs_initially(self):
        self.assertEquals(self.host.contmaprefs, [])

    def test_allows_appending_to_contmaprefs(self):
        self.host.contmaprefs.append("foo")
        self.assertEqual(self.host.contmaprefs, ["foo"])

    def test_allows_plusequals_to_contmaprefs(self):
        self.host.contmaprefs += ["foo"]
        self.assertEquals(self.host.contmaprefs, ["foo"])

    def test_gets_contmaprefs_from_components_the_first_time(self):
        contmapref = obnamlib.ContMapRef("foo")
        self.host.components = [contmapref]
        self.assertEquals(self.host.contmaprefs, ["foo"])

    def test_removes_contmaprefs_from_components_after_first_get(self):
        contmapref = obnamlib.ContMapRef("foo")
        self.host.components = [contmapref]
        genrefs = self.host.contmaprefs
        self.assertEquals(self.host.components, [])

    def test_prepare_puts_contmaprefs_in_components(self):
        self.host.contmaprefs = ["foo"]
        self.host.prepare_for_encoding()
        self.assertEquals(self.host.find_strings(kind=obnamlib.CONTMAPREF),
                          ["foo"])
                          
    def test_prepare_empties_contmaprefs(self):
        self.host.contmaprefs = ["foo"]
        self.host.prepare_for_encoding()
        self.assertEquals(self.host._contmaprefs, None)


class GenerationNamesTests(unittest.TestCase):

    def setUp(self):
        self.host = obnamlib.Host(id="id")
        self.host.genrefs = [str(i) for i in range(10)]
        
    def test_first(self):
        self.assertEqual(self.host.get_generation_id("first"), "0")
        
    def test_oldest(self):
        self.assertEqual(self.host.get_generation_id("oldest"), "0")
        
    def test_latest(self):
        self.assertEqual(self.host.get_generation_id("latest"), "9")

    def test_other(self):
        self.assertEqual(self.host.get_generation_id("5"), "5")

