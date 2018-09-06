from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_model.ui import SimpleCard


class LaunchRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.object_type == "LaunchRequest"

    def handle(self, handler_input):
        speech_text = "どっちがいいか私が決めてあげます。ひとつめを教えてください。"
        card = SimpleCard("気まぐれレコメンド", speech_text)
        return handler_input.response_builder.speak(speech_text).set_card(card).ask(speech_text).response
