#  Copyright (C) 2016 The Gvsbuild Authors
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import project_add


@project_add
class Dav1d(Tarball, Meson):
    def __init__(self):
        Meson.__init__(
            self,
            "dav1d",
            version="1.5.1",
            repository="https://code.videolan.org/videolan/dav1d",
            archive_url="https://code.videolan.org/videolan/dav1d/-/archive/{version}/dav1d-{version}.tar.gz",
            hash="fa635e2bdb25147b1384007c83e15de44c589582bb3b9a53fc1579cb9d74b695",
            dependencies=[
                "nasm",
                "ninja",
                "meson",
                "pkgconf",
            ],
        )
        self.add_param("-Denable_tests=false")
        self.add_param("-Denable_tools=false")

    def build(self):
        Meson.build(self)
