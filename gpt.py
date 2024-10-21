# use whatever model you want to use
import logging
# Configure the logging module
logging.basicConfig(level=logging.DEBUG)
# Create a logger object
logger = logging.getLogger(__name__)
logger.debug("This is a debug message11")

from gpt4allj import Model
logger.debug("This is a debug message22")
import re
logger.debug("This is a debug message33")
model = Model('./model/gpt4all-installer-linux.run')
logger.debug("This is a debug message44")

def gen_response(prompt):
    response = model.generate(prompt)
    response = re.sub(r'( [1-9]\))', r'\\n\1', response)
    response = re.sub(r'\.( [1-9]\))', r'\.\\n\1', response)
    response = re.sub(r'\. ([1-9]\))', r'\.\\n\1', response)
    return response

logger.debug("This is a debug message54")
def simple_gen_response(prompt):
    return model.generate(prompt)
