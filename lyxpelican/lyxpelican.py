from pelican import signals
from pelican.readers import HTMLReader
from pelican.utils import pelican_open
from .elyxer_adapter import convert_lyx

class LyxReader(HTMLReader):
    enabled = True
    file_extensions = ['lyx']
    
    def read(self, filename):
        """Parse content and metadata of HTML files"""
        with pelican_open(filename) as content:
            parser = self._HTMLParser(self.settings, filename)
            parser.feed(convert_lyx(content))
            parser.close()

        metadata = {}
        for k in parser.metadata:
            metadata[k] = self.process_metadata(k, parser.metadata[k])
        if 'create-date' in metadata and 'date' not in metadata:
            metadata['date'] = self.process_metadata('date', parser.metadata['create-date'])
            
        return parser.body, metadata

def add_reader(readers):
    readers.reader_classes['lyx'] = LyxReader
    
def register():
    signals.readers_init.connect(add_reader)