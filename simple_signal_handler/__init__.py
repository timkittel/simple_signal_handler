
import signal
import sys


ALL_SIGNALS = { x: getattr(signal, x)  for x in dir(signal)
               if x.startswith("SIG")
               and not x.startswith("SIG_")  # because they are just duplicates
               and not getattr(signal, x) == 0  # can register only for signals >0
               and not getattr(signal, x) == 28 # SIGWINCH [28] is sent when resizing the terminal ...
               and not x in ["SIGSTOP", "SIGKILL"]  # can't register these because you can't actually catch them (:
               }
NUMBER_TO_SIGNAL = { val: key for key, val in ALL_SIGNALS.items() }

def signal_handler(sig, frame):
    sys.exit(sig)

def register_signals(sigs = set(ALL_SIGNALS), handler=signal_handler, verbose=True):
    """
    register a signal handler for all given signals
    sigs:       (set-like) providing all the signals to be registered
                default: all possible signals 'ALL_SIGNALS'
    handler:    (function) the signal handler to be used
                default: signal_handler, which just raises a 'sys.exit(sig)' for the signal 'sig'
    verbose:    (bool) print a notification to stderr if the signal registering failed
    """
    sigs = set(sigs)
    # register all possible signals
    for sig in ALL_SIGNALS:
        sigclass = getattr(signal, sig)
        signum = sigclass.value
        # the line below checks whether the signal has been given for
        # registering in the form of either the name, the signal class or the
        # signal number
        if set([sig, sigclass, signum]).intersection(sigs):
            try:
                signal.signal(getattr(signal, sig), handler)
            except Exception as e:
                if verbose:
                    print(
                        f"ignoring signal registration: [{ALL_SIGNALS[sig]:>2d}] {sig} (because {e.__class__.__name__}: {e!s})",
                        file=sys.stderr
                    )

