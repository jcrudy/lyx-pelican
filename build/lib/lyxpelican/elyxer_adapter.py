import elyxer
from .elyxer import InOutParser, Options, eLyXerConverter as ElyxerConverter
from StringIO import StringIO

# Elyxer relies on type checking to determine whether to treat its
# input and output as files or file names.  Monkey patch the elyxer 
# module so that it will accept a StringIO instead of a file object.
elyxer.file = StringIO

# Elyxer closes its files.  When a StringIO is closed, it is no longer
# possible to retrieve its contents.  This subclass overrides the close 
# method to preserve the contents of the StringIO.
class UncloseableStringIO(StringIO):
    def close_(self):
        super(UncloseableStringIO, self).close()
    def close(self):
        return None
wrap_string = UncloseableStringIO

class StringInOutParser(InOutParser):
    '''
    An InOutParser with manual control of the input and output
    '''
    def __init__(self, instream, outstream):
        self.filein = instream
        self.fileout = outstream
        
def lyx_options(**kwargs):
    '''
    Convenience function for manipulating the Options singleton
    '''
    args = [__file__]
    for k, v in kwargs.iteritems():
        args.append('--'+str(k))
        args.append(str(v))
    Options().parseoptions(args)

def convert_lyx(lyx_string):
    '''
    Convert a string containing lyx code into a string containing the 
    equivalent html.
    '''
    outstream = wrap_string()
    instream = wrap_string(lyx_string)
    ioparser = StringInOutParser(instream, outstream)
    converter = ElyxerConverter().setio(ioparser)
    converter.convert()
    return outstream.getvalue()

lyx_options(mathjax='remote')
