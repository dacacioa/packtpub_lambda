from __future__ import print_function

import commands

def lambda_handler(event, context):
    if commands.getstatusoutput('sh ./packtpub.sh')[0] == 0 :
        return "Ok, enjoy your free book"
