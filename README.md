# ytQt beta

A new way to watch youtube, focused, using an user-friendly Qt based GUI.

_"The code is well-structured and organized, with clear separation of concerns and modular components."_ -VirusTotal

## Installation
### Windows
##### Some virus scanners will false-positive this as a virus, more information on releases page.
1) Download and install the latest vlc version: [VLC](https://www.videolan.org/vlc/). If already installed, make sure it is updated.
2) Download the latest release: [ytQt installer](https://github.com/Delamox/ytQt/releases).
### GNU/Linux
##### WARNING: Make sure you are on x11 as Wayland does not support vlc embedded players at this moment.
1) install vlc using your package manager.
    * Arch: `pacman -S vlc` or `yay vlc`
    * Debian: `sudo apt install vlc` 
4) `git clone https://github.com/Delamox/ytQt.git`
5) `cd ytQt`
6) `python -m pip install -r requirements.txt`
7) `python search.py`
