from setuptools import setup, find_packages
setup(
    name = "fastlogger",
    version = "1.0",
    packages = find_packages(),
    scripts = [],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires = ['docutils>=0.3'],

    # package_data = {
        # # If any package contains *.txt or *.rst files, include them:
        # '': ['*.txt', '*.rst'],
        # # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    # },

    # metadata for upload to PyPI
    author = "6767",
    #author_email = "me@example.com",
    description = "fast logging Package",
    license = "MIT",
    keywords = "logging",
    url = "http://github.com/6769",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)