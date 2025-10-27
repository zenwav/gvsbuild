# gvsbuild/projects/poppler.py

from gvsbuild.utils.base_builders import CmakeProject
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import project_add


@project_add
class Poppler(Tarball, CmakeProject):
    def __init__(self):
        version = "25.10.0"
        
        CmakeProject.__init__(
            self,
            "poppler",
            version=version,
            repository="https://gitlab.freedesktop.org/poppler/poppler",
            archive_url=f"https://poppler.freedesktop.org/poppler-{version}.tar.xz",
            
            # You must generate this hash for the version you use
            hash="6b5e9bb64dabb15787a14db1675291c7afaf9387438cc93a4fb7f6aec4ee6fe0", 
            
            # Updated dependencies based on your project
            dependencies=[
                "fontconfig",
                "freetype",
                "cairo",
                "libpng",
                "zlib",
                "libjpeg-turbo",
            ],
        )

        # CmakeProject uses self.extra_opts to pass parameters
        self.extra_opts = [
            "-DENABLE_LIBOPENJPEG=none",
            "-DBUILD_GTK_TESTS=OFF",
            "-DBUILD_QT5_TESTS=OFF",
            "-DBUILD_QT6_TESTS=OFF",
            "-DBUILD_CPP_TESTS=OFF",
            "-DENABLE_TESTS=OFF",
            "-DENABLE_UTILS=ON", # Or ON if you need pdftocairo, etc.
            "-DENABLE_CAIRO_OUTPUT=ON",
        ]

    def build(self):
        # Call the base class build method.
        # We can specify use_ninja=True as it's supported.
        CmakeProject.build(self, use_ninja=True)
        
        # You may need to add custom install steps, like for cairo
        # self.install(r".\COPYING share\doc\poppler")
