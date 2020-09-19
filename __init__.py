# -*- coding: utf-8 -*-
import requests
import json
from naomi import plugin


# The speechhandler plugin represents something that Naomi does
# in response to a request from the user. This is often a spoken
# response, but can also be an action like turning on a light or
# sending an email. It is the functional equivalent of a skill on
# most other assistant platforms.
# For details about writing a speech handler, see:
# https://projectnaomi.com/dev/docs/developer/plugins/speechhandler_plugin.html
class DadJokes(plugin.SpeechHandlerPlugin):
    # Intents describe how your plugin may be activated.
    # At the simplest level, just write all the things you think
    # someone might say if they wanted to activate your
    # plugin. Finally, supply a link to the handle method,
    # which Naomi will use when your intent is selected.
    def intents(self):
        return {
            'DadIntent': {
                'locale': {
                    'en-US': {
                        'templates': [
                            'TELL ME A DAD JOKE',
                            'WHAT IS A DAD JOKE'
                        ]
                    }
                },
                'action': self.handle
            }
        }

    # The handle method is where you pick up after Naomi has
    # identified your intent as the one the user was attempting
    # to activate.
    def handle(self, intent, mic):
        # The intent parameter is a structure with information about
        # the user request. intent['input'] will hold the transcription
        # of the user's request.
        #text = intent['input']

        url = "https://icanhazdadjoke.com/"
        response = requests.get(url)
        jsondoc = str(response.content, 'utf-8')
        jokedata = json.loads(jsondoc)
        response = jokedata["joke"]

        # The mic parameter is a microphone object that you can
        # use to respond to the user.
        mic.say(response)