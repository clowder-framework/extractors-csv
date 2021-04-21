#!/usr/bin/env python3
import logging
import csv

from pyclowder.extractors import Extractor
import pyclowder.files

class csvHeaders(Extractor):
    def __init__(self):
        Extractor.__init__(self)
        logging.getLogger('pyclowder').setLevel(logging.DEBUG)
        logging.getLogger('__main__').setLevel(logging.DEBUG)

        self.setup()

    def extract(self,inputfile):
        logger = logging.getLogger(__name__)
        with open(inputfile) as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
        metadata = {'csv_headers': headers}
        logger.debug(metadata)        
        result = {
            'metadata': metadata
        }
        return result

    def process_message(self, connector,host, secret_key,resource, parameters):
        inputfile = resource["local_paths"][0]

        csv_metadata = self.extract(inputfile)
        metadata = self.get_metadata(csv_metadata, 'file', parameters['id'], host)

        # upload metadata
        pyclowder.files.upload_metadata(connector, host, secret_key, parameters['id'], metadata)

        logging.info("Uploaded metadata %s", metadata)

if __name__ == "__main__":
    extractor = csvHeaders()
    extractor.start()
