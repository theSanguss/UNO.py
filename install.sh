#!/bin/bash

                                                                                                                                          
#     88        88 888b      88   ,ad8888ba,                                                                  
#     88        88 8888b     88  d8"'    `"8b                                                                 
#     88        88 88 `8b    88 d8'        `8b                                                                
#     88        88 88  `8b   88 88          88    8b,dPPYba,  8b       d8                                     
#     88        88 88   `8b  88 88          88    88P'    "8a `8b     d8'                                     
#     88        88 88    `8b 88 Y8,        ,8P    88       d8  `8b   d8'                                      
#     Y8a.    .a8P 88     `8888  Y8a.    .a8P 888 88b,   ,a8"   `8b,d8'                                       
#      `"Y8888Y"'  88      `888   `"Y8888Y"'  888 88`YbbdP"'      Y88'                                        
#                                                 88              d8'                                         
#                                                 88             d8'        
# https://github.com/theSanguss/UNO.py

# Check for git
if ! command -v git &> /dev/null; then
    echo -e "\e[1;31mError: git is not installed. Please install git and try again.\e[0;34m\nhttps://git-scm.com/downloads/\e[0m"
    exit 1
fi

# Check for python or python3
if command -v python &> /dev/null; then
    PYTHON_CMD="python"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    echo -e "\e[1;31mError: Python is not installed. Please install Python and try again.\e[0;34m\nhttps://www.python.org/downloads/\e[0m"
    exit 1
fi

# Check for pip or use python -m pip
if command -v pip &> /dev/null; then
    PIP_CMD="pip"
elif $PYTHON_CMD -m pip --version &> /dev/null; then
    PIP_CMD="$PYTHON_CMD -m pip"
else
    echo -e "\e[1;31mError: pip is not installed. Please install pip and try again.\e[0;34m\nhttps://pip.pypa.io/en/stable/installation/\e[0m"
    exit 1
fi

# Clone repo and run
git clone https://github.com/theSanguss/UNO.py.git
cd UNO.py || exit 1
$PIP_CMD install -r requirements.txt
$PYTHON_CMD main.py
