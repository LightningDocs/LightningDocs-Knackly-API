## Quick-start

A static, web hosted rendering of the Jupyter Notebook can be found [here][NBViewer-url] if you just want to quickly read the notebook.

## About The Project

The goal of this repository is to outline the various ways to interact with both the LightningDocs and Knackly API for your document automation needs. Examples are given in Python, but the underlying RESTful requests will work the same in any programming language.

### Built with

This project was built using...

[![Python][Python-url]][Python-url]
[![Jupyter Notebook][Jupyter-url]][Jupyter-url]
[![Visual Studio Code][VSCode-url]][VSCode-url]

## Getting Started

In order to run the majority of the cells in the notebook, you must have various pieces of information given to you by LightningDocs. This will includes a `version`, `tenancy`, `keyID`, `secret`, and `refresh_token`.

### Prerequisites

* [Anaconda][Anaconda-url] / [Jupyter Notebook][Jupyter.com]
* Optionally, [Visual Studio Code][VSCode.com]

### Installation

1. Clone or manually download the repo
   ```sh
   git clone https://github.com/LightningDocs/LightningDocs-Knackly-API.git
   ```
2. Start a Jupyter Server by running the Anaconda Prompt terminal and entering the following commands
   ```sh
   cd "YOUR_DIRECTORY_LOCATION"
   ```

   ```sh
   jupyter notebook
   ```
3. From the browser, open `main.ipynb`
4. Optionally, you can view / run this notebook using Visual Studio Code instead
   1. Make sure the Jupyter extension is installed in VS Code
   2. From the File menu, open the folder wherein the Notebook is stored
   3. Click on the Python Kernel in the upper right corner of VS Code
   4. Choose **Select Another Kernel**
   5. Choose **Existing Jupyter Server** _(The Jupyter Server from Step 3 must still be running)_
   6. Choose **Enter the URL of the running Jupyter Server**
   7. Press **Enter**
   8. Give the server a display name or leave it as "localhost"

[VSCode.com]: https://code.visualstudio.com/
[VSCode-url]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[Jupyter.com]: https://jupyter.org/
[Jupyter-url]: https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white
[Python.com]: https://www.python.org/
[Python-url]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Anaconda-url]: https://www.anaconda.com/download
[NBViewer-url]: https://nbviewer.org/github/LightningDocs/LightningDocs-Knackly-API/blob/master/main.ipynb
