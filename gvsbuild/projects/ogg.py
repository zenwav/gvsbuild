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
class Ogg(Tarball, CmakeProject):
    def __init__(self):
        Project.__init__(
            self,
            "ogg",
            version="1.3.6",
            repository="https://github.com/xiph/ogg",
            archive_url="https://github.com/xiph/ogg/releases/download/v{version}/libogg-{version}.tar.xz",
            hash="5c8253428e181840cd20d41f3ca16557a9cc04bad4a3d04cce84808677fa1061",
            dependencies=["cmake", "ninja"],
            patches=[],
        )

    def build(self):
        CmakeProject.build(self, use_ninja=True)
        self.install(r".\COPYING share\doc\ogg")
