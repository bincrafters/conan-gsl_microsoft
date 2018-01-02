#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os


class GslMicrosoftConan(ConanFile):
    name = "gsl_microsoft"
    version = "20171020"
    commit_id = "211e195d8f9dd6fa967a5741387fb5eae1ff351b"
    description = "Functions and types that are suggested for use by the C++ Core Guideline"
    url = "https://github.com/bincrafters/conan-gsl_microsoft"
    license = "MIT"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/Microsoft/GSL"
        self.run("git clone {0}.git".format(source_url))
        os.rename("GSL", self.source_subfolder)
        with tools.chdir(self.source_subfolder):
            self.run("git checkout -f {0}".format(self.commit_id))
            
    def package(self):
        include_folder = os.path.join("source_subfolder","include")
        self.copy(pattern="LICENSE", src="source_subfolder")
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
