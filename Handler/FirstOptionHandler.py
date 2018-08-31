from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_model.ui import SimpleCard


class FirstOptionHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.object_type == "FirstOptionIntent"

    def handle(self, handler_input):
        # セッション変更
        first = handler_input.request_envelope.request.intent.slots['first'].value
        handler_input.attributes_manager.session_attributes['first'] = first
        card = SimpleCard("どっちがいい？", 'もう片方は？')
        return handler_input.response_builder.ask('もう片方は？').set_card(card).response
