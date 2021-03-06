# vim: set fileencoding=utf-8 :

import logging
from sys import exit, stderr

from yatetradki.arguments import parse_args
from yatetradki.command import fetch_word
from yatetradki.command import fetch
from yatetradki.command import export
from yatetradki.command import show
from yatetradki.command import list_words
from yatetradki.command import word

#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

FORMAT = '%(asctime)-15s %(levelname)-7s %(message)s'


logging.basicConfig(format=FORMAT, stream=stderr)
_logger = logging.getLogger()
_logger.setLevel(logging.DEBUG)
logging.getLogger("requests").setLevel(logging.WARNING)


def main():
    args = parse_args()
    dispatch = {
        'fetch_word': fetch_word,
        'fetch': fetch,
        'export': export,
        'show': show,
        'words': list_words,
        'word': word
    }
    return dispatch[args.command](args)


if __name__ == '__main__':
    exit(main())


'''
Things to implement

Usage:
    http://bnc.bl.uk/saraWeb.php?qy=gruesome

Thesaurus (synonims, antonims):
    http://www.thesaurus.com/browse/intact?s=ts

Many useful stuff:
    http://www.thefreedictionary.com/gruesome

No results from thesaurus: "no thesaurus results"

Sample output:

en -> ru | scrotum       мошонка       flawless perfect unblemished unbroken unharmed unhurt unscathed untouched
                                       broken damaged flawed harmed hurt imperfect injured

TODO:
    + read credentials from netrc
    + caching
        + download new words to file
        + download new syn&ant, usages, explanations to file
    + colorization (color tables)
    + usage (sample sentences, http://bnc.bl.uk/saraWeb.php?qy=gruesome)
    + explanation in English (http://www.thefreedictionary.com/gruesome)
    - all syn&ant groups (http://www.thesaurus.com/browse/intact?s=ts)
    - network timeouts
    - columns
        + break long output into columns
        - limit number of columns (--num-columns, conflicts with --num-words)
        + break by words, not by lines
    + trim wordsto
    + draw N random definitions/usages, but save them all
    - smart merge order from slovari, do not replace current one

    - split into commands:
        + fetch (download from everywhere to local storage)
            - support word as arguments (what to do with order?)
        + show (pretty-print local storage)
            - support word as arguments (basically word command)
        - both: make them chainable, so that there could be third script
          that could easily execute them both. do I really need that?
        + words: print all words in the cache
        + word: print specified words
        - remove: remove word from order and cache
        - add: add word to order and cache
        - random: print N random words from cache

    - draw from different sources depending on the language of wordfrom
    - timeout per command
    - logging system, timestamps
    + shape up tokens:
        + def -> def (token)
        + usage -> usage (token)
        + usage-1 -> usage color
        + definition-1 -> definition color
        - delimeters (screw that, though)
    + do not print section if content is not available
        + syn, ant, def, usage
    - redesign layout generation system, current one is awful
'''
