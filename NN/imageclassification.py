from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Imports
import numpy as np
import tensorflow as tf
flags = tf.app.flags
FLAGS = flags.FLAGS 
tf.logging.set_verbosity(tf.logging.INFO)

def main(args):
    flags.DEFINE_string('name', None,
                        'Append a name Tag to run.')

    flags.DEFINE_string('hypes', 'hypes/medseg.json',
                        'File storing model parameters.')
# Our application logic will be added here
print(tf)
if __name__ == "__main__":
  tf.app.run()
