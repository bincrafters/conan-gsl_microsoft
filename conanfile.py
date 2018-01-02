#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os


class GslMicrosoftConan(ConanFile):
    name = "gsl_microsoft"
    version = "20171020"
    description = "Functions and types that are suggested for use by the C++ Core Guideline"
    url = "https://github.com/bincrafters/conan-gsl_microsoft"
    license = "MIT"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/Microsoft/GSL"
        self.run("git clone --depth=1 {0}.git".format(source_url))
        os.rename("GSL", self.source_subfolder)

    def package(self):
        include_folder = os.path.join("source_subfolder","include")
        self.copy(pattern="LICENSE", src="source_subfolder")
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
