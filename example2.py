#!/usr/bin/env python

# Try this with neither file extant
# Try with no source but with target
# Try this with target set no write permissions
#    e.g., $ touch squiggle.2 ; chmod 000 squiggle.2
# Try with source and writable target
# Try with source and no target
# Try with source, no target, and no write permissions in the folder

import subprocess as sp
import sys

source_file = 'squiggle.1'
target_file = 'squiggle.2'

def my_cp(src, tgt):
    try:
        out = sp.check_output(['/bin/cp', src, tgt],
                stderr=sp.STDOUT)
    except sp.CalledProcessError, err:
        print "Return code from attempting to"
        print "  cp", src, "to", tgt
        print "was", err.returncode
        print "with error message:"
        print err.output

my_cp(source_file, target_file)
