from ask_sdk_core.skill_builder import SkillBuilder
from Handler.LaunchRequestHandler import LaunchRequestHandler
from Handler.FirstOptionHandler import FirstOptionHandler

sb = SkillBuilder()
sb.request_handlers.extend([
    LaunchRequestHandler(),
    FirstOptionHandler()
])

handler = sb.lambda_handler()
