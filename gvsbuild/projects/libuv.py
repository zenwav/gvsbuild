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

from gvsbuild.utils.base_builders import CmakeProject
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class Libuv(Tarball, CmakeProject):
    def __init__(self):
        Project.__init__(
            self,
            "libuv",
            version="1.51.0",
            repository="https://github.com/libuv/libuv",
            archive_filename="libuv-v{version}.tar.gz",
            archive_url="https://github.com/libuv/libuv/archive/v{version}.tar.gz",
            hash="27e55cf7083913bfb6826ca78cde9de7647cded648d35f24163f2d31bb9f51cd",
            dependencies=[
                "cmake",
                "ninja",
            ],
        )

    def build(self):
        CmakeProject.build(self, use_ninja=True)

        self.install(r".\LICENSE share\doc\libuv")
