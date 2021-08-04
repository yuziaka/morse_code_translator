import os

from setuptools import find_packages, setup

ROOT = os.path.dirname(__file__)


with open("README.md", encoding="utf-8") as f:
    README = f.read()


setup(
    name="morse-code-translator2",
    version="0.0.3",
    description="Morse Code Translator",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Yurii Bondarenko",
    author_email="ybondarenko.job@gmail.com",
    url="https://github.com/yuziaka/morse_code_translator",
    packages=find_packages(
        exclude=[
            "*tests*",
            "poetry.lock",
            "pyproject.toml",
            "TOPIC.md",
            "conftest.py",
            ".venv",
            ".github",
            "images"
        ]
    ),
    package_dir={"morse_code_translator": "morse_code_translator"},
    python_requires=">=3.6.*",
    license="MIT",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Documentation": "https://github.com/yuziaka/morse_code_translator",
        "Source Code": "https://github.com/yuziaka/morse_code_translator",
    },
    tests_require=[],
)
