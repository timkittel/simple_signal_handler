## simple signal handler
A wrapper for handling signals in Python via exceptions.

### Installation

Clone the repository with
```
git clone https://github.com/timkittel/simple_signal_handler.git
```

and then change in the directory and install it with pip
```
pip install .
```

### Usage

As shown in `test.py`, you can simply register all signals
```python
import simple_signal_handler as sh
sh.register_signals()
```
Now, whenever a signal (except Terminal Resize (SIGWINCH) and direct stopping signals (SIGSTOP, SIGKILL)) is caucht, a SystemExit is raised that can be caucht with a `try` and     `except` statement. Please check the optional arguments of `register_signals` to adjust which signals are registered and the behavior when a signal is caught.