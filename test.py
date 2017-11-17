
import simple_signal_handler as sh

from time import sleep


sleep_time = 300 # seconds = 5 minutes


sh.register_signals()

print("waiting for a signal ... ", end="", flush=True)
try:
    sleep(sleep_time)
except SystemExit as e:
    print()
    print("interrupted by SystemExit or Signal {} [{}]".format(sh.NUMBER_TO_SIGNAL[e.args[0]], e.args[0]))
else:
    print("hm, I didn't receive a signal. Are you sure you sent one?")
