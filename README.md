# The Ultimate PDF to Text Converter
An application that can extract editable as well as scanned text from PDF files.

## Execution
Execute `main.py` using Python 3.8+.
```
python main.py
```

## Prerequisites and Dependencies
- PyPI requirements can be installed via `requirements.txt`.
  ```
  pip3 install -r requirements.txt
  ```
  `sudo` might be required for modifying the PATH environment variable.
- [Tesseract](https://github.com/tesseract-ocr/tesseract) must be installed for text recognition. If not found in PATH, its binary will be searched for in the TESSERACT_CMD environment variable. It can be downloaded and installed [here](https://github.com/tesseract-ocr/tesseract/releases).
  
  If not added to PATH, its binary must be assigned to TESSERACT_CMD.
  - Bash/Terminal
    ``` bash
    export TESSERACT_CMD='/path/to/tesseract'
    ```
  - PowerShell
    ``` powershell
    $Env:Tesseract_Cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```
  - Command Prompt (Windows)
    ``` cmd
    set "TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```
- [Poppler](https://poppler.freedesktop.org/) must be installed and added to PATH. Below are instructions for various operating systems.
  - Windows users can download and install it [here](https://blog.alivate.com.au/poppler-windows/).
  - MacOS users can install it using Homebrew.
    ```
    brew install poppler
	```
  - Most Linux distributions already ship with Poppler. If absent, it can manually be installed.
    ```
    sudo apt install poppler-utils
	```

## Behind the idea
- [Tesseract PDF OCR](https://github.com/Manvendra2000/Reader) : A simple application that reads a PDF file and parses the text using the Tesseract OCR. _– [Manvendra](https://github.com/Manvendra2000), [Param](http://www.paramsid.com/)._
- [PDF File Reader](https://github.com/HarshMarolia/Pdf-File-Reader) : A simple Python application that reads out textual PDF files. _– [Harsh](https://github.com/HarshMarolia), [Param](http://www.paramsid.com/)._

### Made with ❤ by [Manvendra](https://github.com/Manvendra2000), [Harsh](https://github.com/HarshMarolia), and [Param](http://www.paramsid.com/).