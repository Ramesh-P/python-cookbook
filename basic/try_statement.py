# Python 3.6.0
# Simple try statement
try:
    this_will_cause_an_error()
except Exception:
    print('I encountered an error!')
# OUT: I encountered an error!

# Python 3.6.0
# Listen for specific error
try:
    while 1: pass
    # Busy wait
except KeyboardInterrupt:
    print('You pressed Ctrl+C!')
# OUT: (Waits until interrupt) You pressed Ctrl+C!

# Python 3.6.0
# Get error value
try:
    this_will_cause_an_error()
except Exception as e:
    print('I encountered an error!', e)
# OUT: I encountered an error! name 'this_will_cause_an_error' is not defined
