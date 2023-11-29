from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Movie-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "pankaj2412"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=pankaj2412,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{pankaj2412}/{recommendation-system}",
    author_email="pankajkumar807673@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
