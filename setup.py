import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()



__version__ = "0.0.1"

REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "Chandrashekhar"
SRC_REPO = "Text_Summarizer"
AUTHOR_EMAIL = "chandrashekhar130697@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer basic project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Chandrashekhar569/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/Chandrashekhar569/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
