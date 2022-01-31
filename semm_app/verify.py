""" Verify credentials with SIWE """

import siwe
from siwe.siwe import SiweMessage


def verify_credentials(msg, sig):
  """ Pass EIP-4361 conforming message + MetaMask-facilitated signature (on that message) to SIWE to validate credentials. Returns true if validated, else false.

  NOTE BROKEN: not working
  """
  print(type(sig))
  print(sig)
  #msg[0]['signature'] = sig
  siwe_message = SiweMessage(msg[0])
  try:
    validation_outcome = siwe_message.validate(sig)
  #except siwe.ValidationError:
  #  print('siwe validation error')
  except:
    validation_outcome = False
  return validation_outcome