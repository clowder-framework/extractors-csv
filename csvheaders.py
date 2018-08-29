#!/usr/bin/env python
import logging
import csv


def csvheaders(input_file):
    logger = logging.getLogger(__name__)
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
    metadata = {'csv_headers': headers}
    logger.debug(metadata)        
    result = {
        'metadata': metadata
    }
    return result
