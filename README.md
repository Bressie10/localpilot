# LocalPilot

LocalPilot is a command-line computer assistant for checking system resources, inspecting files and processes, and running basic network diagnostics. It is a work in progress built for Hack Club Terra.

## Download and run on macOS

Download the **LocalPilot-macOS-arm64.zip** asset from the [latest release](https://github.com/Bressie10/localpilot/releases/latest). Unzip it, open Terminal in the extracted folder, and run:

```sh
chmod +x LocalPilot
./LocalPilot
```

This build is for Apple Silicon Macs. macOS may ask you to approve the unsigned download in **System Settings → Privacy & Security** before it opens. Type `help` to see the commands and `exit` to quit. File commands act on the directory where you launch LocalPilot, so try `pwd` and `ls` first; `rm` deletes files.

## Run from source

Python 3.14 is required. From the repository directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install psutil==7.2.2
.venv/bin/python main.py
```

The CLI has commands for CPU, RAM, disk, process, and network information, as well as `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cat`, `find`, `cp`, `mv`, and `rm`. Run `help` for syntax. The browser prototype in `streamlit_app.py` is experimental and is not the downloadable demo.
