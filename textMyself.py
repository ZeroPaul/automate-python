#!/usr/bin/env python3
# -*- coding: utf-8 -*-

accountSID = 'ACzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
authToken = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
myNumber = '+099999999999999'
twilioNumber = '+077777777777'

from twilio.rest import TwilioRestClient as trc

def textmyself(message):
    """TODO: Docstring for textmyself.

    :message: TODO
    :returns: TODO

    """
    twilioCli = trc(accountSID, authToken)                        
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

