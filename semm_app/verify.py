# semm/semm_app/verify.py

""" Verify credentials with SIWE """

import json
import siwe
from siwe.siwe import SiweMessage


def verify_credentials(msg, sig):
  """ Pass EIP-4361 conforming message + its MetaMask-facilitated signature to SIWE to validate credentials. Returns true if validated, else false.

  NOTE BROKEN: not working :( "Invalid signature"
  """
  
  msg_dict = json.loads(msg)
  msg_dict['signature'] = sig
  siwe_message = SiweMessage(msg_dict)
  try:
    validation_outcome = siwe_message.validate(sig)
  # except siwe.ValidationError: # no ValidationError attribute
  #   print('siwe validation error')
  except:
    validation_outcome = False # TODO inappropriate handling - included to allow redirect to 'credentials_not_verified.html'

  return validation_outcome