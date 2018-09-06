from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model.ui import SimpleCard
import random


class FirstOptionHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return is_intent_name("FirstOptionIntent")(handler_input)

    def handle(self, handler_input):
        # セッション変更
        first = handler_input.request_envelope.request.intent.slots['first'].value
        if handler_input.attributes_manager.session_attributes.get('first') is not None:
            second = first
            first = handler_input.attributes_manager.session_attributes['first']
            rand = random.randrange(2)
            choice = second
            if rand == 0:
                choice = first

            card = SimpleCard("気まぐれレコメンド", choice + 'がいいと思います。')
            handler_input.response_builder.speak(choice + 'がいいと思います。').set_card(card).set_should_end_session(True)
            return handler_input.response_builder.response
        else:
            handler_input.attributes_manager.session_attributes['first'] = first
            card = SimpleCard("気まぐれレコメンド？", 'もうひとつは？')
            return handler_input.response_builder.speak('もうひとつは？').ask('もうひとつは？').set_card(card).response
