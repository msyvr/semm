# semm/semm_app/verify.py

""" Verify credentials with SIWE """

import json
import siwe
from siwe.siwe import SiweMessage


def verify_credentials(msg: str, sig: str):
  """ Pass EIP-4361 conforming message + its MetaMask-facilitated signature to SIWE to validate credentials. Returns true if validated, else false.
  """
  
  msg_dict = {}
  msg_dict['message'] = msg
  msg_dict['signature'] = sig
  print(msg_dict)
  siwe_message = SiweMessage(msg)
  print(siwe_message)
  print(siwe_message.validate(sig))
  try:
    validation_outcome = siwe_message.validate()
  # except siwe.ValidationError: # no ValidationError attribute
  #   print('siwe validation error')
  except:
    print('validation unsuccessful')
    validation_outcome = False # TODO inappropriate handling - included to allow redirect to 'credentials_not_verified.html'

  return validation_outcome