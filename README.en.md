# IPTV_analysis

#### Description
This project collects open-source IPTV source files or possibly valid links, and converts them into channels recognizable by the Synology IPTV management system, outputting to a new M3U file.

#### Software Architecture
The software runs in a Python 3 environment. The personal version used is Python 3.11.4. If there are any issues with running the program, please refer to the changes in the relevant version.

#### Installation

1.  Install the Python 3.11 runtime environment.
2.  The code execution requires libraries such as requests, random, time, re. Therefore, before running the program, execute the following command to install the libraries: `pip install requests`.

#### Instructions

1.  Prepare the original `ipty.py` file and the original M3U file in the current directory where the code is stored.
2.  Run directly: `python ipty.py`.
3.  If the program runs for a long time without further execution, please close it and collect the newly generated M3U file in the current directory.

#### Contribution

1.  None.
