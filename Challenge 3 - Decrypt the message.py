encrypted_string = "PXDMn!?BdNhP!?eZcoEgBCau!?rxHTfSX!?ixhbV!?cCnlUhFv!?hJFDB!?tDgC!? Uox!?jZzTXPyKq!?uPxQ!?icToHOtRJ!?sscVwqvSfhh!?ttOe!? mAR!?vFzorM!?ebsDQfLcjgR!?rKo!?wnW!?eJGlOGG!?rCTP!?kpVZmoQxP e!?tMohfLBnYtm!?!Vkm"

split_string = encrypted_string.split("!?")

extracted_message = [segment[0] for segment in split_string if segment]

decoded_message = ''.join(extracted_message)

final_message = decoded_message[1:]

print("Gedecodeerd bericht:")
print(final_message)
