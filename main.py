import prehook
import logging

logging.basicConfig(
    filename="execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


from prehook import execute_prehook
from hook import *
from posthook import *


execute_prehook()
execute_hook()
execute_posthook()
