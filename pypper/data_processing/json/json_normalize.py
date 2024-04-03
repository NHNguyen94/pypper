# import json
# import traceback
# import ndjson
#
# class JsonDataProcessing:
#   def __init__():
#         pass
#
#   def _handle_error(self):
#         message = 'Error streaming file. Cause: %s' % (traceback.format_exc())
#         print(message)
#
#   def json_nomarlize_(self, dictionary):
#         """Flatten a nested json file"""
#
#         def unpack(parent_key, parent_value):
#             """Unpack one level of nesting in json file"""
#
#             if isinstance(parent_value, dict):
#                 for key, value in parent_value.items():
#                     if key == "BOOL":
#                         temp1 = f"{parent_key}"
#                     elif key == "S":
#                         temp1 = f"{parent_key}"
#                     elif key == "N":
#                         temp1 = f"{parent_key}"
#                     # If type = M kepp iterating within the dictionary value
#                     elif key == "M":
#                         temp1 = f"{parent_key}"
#                         value = self.json_nomarlize_(value)
#                     else:
#                         temp1 = f"{parent_key}_{key}"
#                     yield temp1, value
#             elif isinstance(parent_value, list):
#                 i = 0
#                 for value in parent_value:
#                     temp2 = f"{parent_key}_{str(i)}"
#                     i += 1
#                     yield temp2, value
#             else:
#                 yield parent_key, parent_value
#         # Unpacking the element of dictionary then return to according to the pair key-value
#         dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
#         return dictionary

# flake8: noqa
