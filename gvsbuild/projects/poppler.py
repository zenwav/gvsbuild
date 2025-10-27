# gvsbuild/projects/poppler.py

from gvsbuild.utils.base_builders import CmakeProject
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import project_add


@project_add
class Poppler(Tarball, CmakeProject):
    def __init__(self):
        CmakeProject.__init__(
            self,
            "poppler",
            version=25.10.0,
            repository="https://gitlab.freedesktop.org/poppler/poppler",
            archive_url=f"https://poppler.freedesktop.org/poppler-25.10.0.tar.xz",
            hash="6b5e9bb64dabb15787a14db1675291c7afaf9387438cc93a4fb7f6aec4ee6fe0",
            dependencies=["fontconfig", "freetype", "cairo", "libpng", "zlib", "libjpeg-turbo"],
        )
        self.extra_opts = [
            "-DENABLE_LIBOPENJPEG=none",
            "-DBUILD_GTK_TESTS=OFF",
            "-DBUILD_QT5_TESTS=OFF",
            "-DBUILD_QT6_TESTS=OFF",
            "-DBUILD_CPP_TESTS=OFF",
            "-DENABLE_TESTS=OFF",
            "-DENABLE_UTILS=ON",
            "-DENABLE_CAIRO_OUTPUT=ON",
        ]

    def build(self):
        CmakeProject.build(self, use_ninja=True)
