from setuptools import setup

with open("./README.md") as fp:
    long_description = fp.read()

setup(
    name="adb_cloud_connector",
    author="Anthony Mahanna",
    author_email="anthony.mahanna@arangodb.com",
    description="Access to temporary ArangoDB Cloud instance provisioning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arangodb/adb_cloud_connector",
    keywords=["arangodb", "cloud", "connector"],
    packages=["adb_cloud_connector"],
    include_package_data=True,
    use_scm_version=True,
    python_requires=">=3.6",
    license="Apache Software License",
    install_requires=[
        "requests",
        "setuptools>=42",
        "setuptools_scm[toml]>=3.4",
    ],
    extras_require={
        "dev": [
            "black",
            "isort>=5.0.0",
            "mypy>=0.790",
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            # "coveralls>=3.3.1",
            "types-setuptools",
            "types-requests",
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
