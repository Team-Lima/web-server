"""
    A sightly modified implementation of the original run_inference.

    Instead of running the NN using a image from disk, it takes directly the image
    as a bytes object. It also returns the prediction results instead of
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os

import tensorflow as tf

from im2txt import configuration

from im2txt import inference_wrapper
from im2txt.inference_utils import caption_generator
from im2txt.inference_utils import vocabulary

CHKPNT_PATH = r"chk_point/model.ckpt-2000000" #path to checkpoint
VOBAB_PATH = r"word_counts.txt" #path to the vocabulary file


def predict(img):
    """
    :param img:     The 'raw' image. has to be a 'bytes' object
    :return:
    """

    #Starting to build the inference graph
    g = tf.Graph()
    with g.as_default():
        model = inference_wrapper.InferenceWrapper()
        restore_fn = model.build_graph_from_config(configuration.ModelConfig(),
                                                   CHKPNT_PATH)
    g.finalize()

    #setting up the vocabulary
    vocab = vocabulary.Vocabulary(VOBAB_PATH)

    with tf.Session(graph=g) as sess:
        #Loading the model
        restore_fn(sess)

        #Initializing the captions generator
        gen = caption_generator.CaptionGenerator(model, vocab)

        #Getting the resulting sentence
        caption = gen.beam_search(sess, img)[0]




        #Getting the sentence and probability out of the caption
        prob = math.exp(caption.logprob)

        sentence = [vocab.id_to_word(w) for w in caption.sentence[1:-1]]
        sentence = " ".join(sentence)
            
    return sentence, prob

