import sys
import getopt
import logging


# less demo.log opens the demo.log file in the terminal
# log_demo.py --log warning or log_demo.py --l warning
# will result in a demo.log containing only the 'Finished sequence'
# log_demo.py--log debug or log_demo.py --l debug
# => showing all the debug, info & warning messages
# log_demo.py --log info or log_demo.py --l info
# => showing only the info & warning messages

opts, args = getopt.getopt(sys.argv[1:], "l:", ["log="])

log_level="INFO"
for opt, arg in opts:
    if opt in ("-l", "--log"):
        log_level = getattr(logging, arg.upper())

logging.basicConfig(filename='./demo.log', level=log_level, format='%(asctime)s %(levelname)s:%(message)s')

for i in range(0, 100):
    if i % 5 == 0:
        logging.debug('Found a number divisible by 5: {0}'.format(i))
    else:
        logging.info('At number {0}'.format(i))
logging.warning('Finished sequence')


# logging.basicConfig(filename='./demo.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# for i in range(0, 100):
#     if i % 5 == 0:
#         logging.debug('Found a number divisible by 5: {0}'.format(i))
#     else:
#         logging.info('At number {0}'.format(i))
# logging.warning('Finished sequence')