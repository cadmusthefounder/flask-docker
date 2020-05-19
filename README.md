<h2 align="center">GovText Template Repo</h2>

<p align="center">
<img alt="Python: v3.7" src="https://img.shields.io/badge/python-v3.7-blue">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

GovText is a text analytics platform to help make sense of text data using state-of-the-art NLP techniques. We support a wide range of NLP capabilities, including like Sentiment Analysis, Topic Modelling, Text Summarisation and more!

## Table of Contents

1. [Setup](#setup)
2. [Contributing](#contributing)

## Setup <a name="setup"></a>

This project requires the following dev dependencies:

1. Python (>=3.7.5)
2. Docker (>=19.03.8)
3. Docker Compose (>=1.25.5)
4. Make (>=3.81)
5. NPM (>=6.14.2)
6. Poetry (>=1.0.5)
7. Git (>=2.21.1)

Next, run the following commands in the terminal at the root of the project:

```shell
> poetry env use <python_path> # only include this line if your system has multiple python versions
> make install # install dependencies
> make env # creates a .env file that is based on sample.env
```

Fill in the missing values in the `.env` file. For the full list of Make commands, run:

```shell
> make # or make help
```

To activate the python environment that poetry has setup, run:

```shell
> poetry shell # activates poetry environment
> which python # shows environment location
> exit # deactivates poetry environment
```

## Contributing <a name="contributing"></a>

Want to file a bug, contribute some code, or improve documentation? Great! Read up on our [contributing guidelines](CONTRIBUTING.md) and start coding away!
