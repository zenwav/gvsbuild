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
import sys
from pathlib import Path

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import project_add


@project_add
class Pycairo(Tarball, Meson):
    def __init__(self):
        Meson.__init__(
            self,
            "pycairo",
            version="1.28.0",
            repository="https://github.com/pygobject/pycairo",
            archive_url="https://github.com/pygobject/pycairo/releases/download/v{version}/pycairo-{version}.tar.gz",
            hash="26ec5c6126781eb167089a123919f87baa2740da2cca9098be8b3a6b91cc5fbc",
            dependencies=["cairo"],
        )

    def build(self):
        py_dir = Path(sys.executable).parent
        Meson.build(self, meson_params=f'-Dpython="{py_dir}\\python.exe"')
        cairo_inc = Path(self.builder.gtk_dir) / "include" / "cairo"
        self.builder.mod_env("INCLUDE", str(cairo_inc))
        self.exec_vs(r"%(python_dir)s\python.exe -m build -w")
        dist_dir = Path(self.build_dir) / "dist"
        for path in dist_dir.rglob("*.whl"):
            self.exec_vs(r"%(python_dir)s\python.exe -m pip install " + str(path))
        if self.builder.opts.py_wheel:
            self.install_dir("dist", "python")
        self.install(r".\COPYING share\doc\pycairo")
        self.install(r".\COPYING-LGPL-2.1 share\doc\pycairo")
        self.install(r".\COPYING-MPL-1.1 share\doc\pycairo")
