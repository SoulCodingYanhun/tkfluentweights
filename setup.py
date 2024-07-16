from setuptools import setup, find_packages
with open("README.md", "r") as f:
    long_description = f.read()
setup(
    name="tkfluentweights",
    version="1.0.0",
    author="SoulCodingYanhun",
    author_email="zhuzhishengzhu6@outlook.com",
    description="我们让Tkinter UI样式编写美化成Fluent UI样式而且使用一些调用方法时变的更加建议",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SoulCodingYanhun/tkfluentweights",
    packages=find_packages(),
    install_requires=[
        "tkinter",
        "ttkbootstrap",
        "ttkthemes"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
