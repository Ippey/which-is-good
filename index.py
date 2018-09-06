from ask_sdk_core.skill_builder import SkillBuilder
from Handler.LaunchRequestHandler import LaunchRequestHandler
from Handler.FirstOptionHandler import FirstOptionHandler
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_model.ui import SimpleCard

sb = SkillBuilder()
sb.request_handlers.extend([
    LaunchRequestHandler(),
    FirstOptionHandler()
])


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    speech_text = '私が2つのうちどちらがいいか決めてあげます。まずは1つめを教えてください。続いて2つめを教えていただけると、どちらか決めます'
    card = SimpleCard('気まぐれレコメンド', speech_text)
    return handler_input.response_builder.speak(speech_text).set_card(card).ask(speech_text).response


@sb.request_handler(
    can_handle_func=lambda input:
    is_intent_name("AMAZON.CancelIntent")(input) or
    is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    speech_text = "またつかってください。"

    handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("気まぐれレコメンド", speech_text))
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    # Log the exception in CloudWatch Logs
    print(exception)

    speech = "すいません、わかりませんでした。"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response


handler = sb.lambda_handler()
