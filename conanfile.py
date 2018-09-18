#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class GslMicrosoftConan(ConanFile):
    name = "gsl_microsoft"
    version = "2.0.0"
    description = "Functions and types that are suggested for use by the C++ Core Guideline"
    url = "https://github.com/bincrafters/conan-gsl_microsoft"
    license = "MIT"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/Microsoft/GSL"
        tools.get("{0}/archive/v{1}.zip".format(source_url, self.version))
        extracted_dir = "GSL-" + self.version
        os.rename(extracted_dir, self.source_subfolder)
            
    def package(self):
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="LICENSE", src=self.source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
