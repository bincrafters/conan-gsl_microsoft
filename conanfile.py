from conans import ConanFile, tools, os


class GslMicrosoftConan(ConanFile):
    name = "gsl_microsoft"
    version = "20171020"
    url = "https://github.com/bincrafters/conan-gsl_microsoft"
    description = "Functions and types that are suggested for use by the C++ Core Guideline"
    license = "https://github.com/Microsoft/GSL/blob/master/LICENSE"
    source_url = "https://github.com/Microsoft/GSL"
    
    def source(self):
        self.run("git clone --depth=1 {0}.git".format(self.source_url))
        
    def package(self):
        self.copy(pattern="*", dst="include", src=os.path.join("GSL","include"))

    def package_id(self):
        self.info.header_only()

