#!/usr/bin/env python
import logging
import csv
import os


def csvheaders(input_file):
    logger = logging.getLogger(__name__)
    # Read image
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

    # Convert color image to grayscale


    metadata = {'headers': headers}
    logger.debug(metadata)        
    result = {
        'metadata': metadata
    }
    return result
