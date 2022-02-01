# Demo: Flask app with Sign In With Ethereum for MetaMask users

## Working:
- MetaMask personal sign request
- redirect for unverified credentials (no 'login')

## Not working:
- message validation by siwe :(
- ? check message parsing in siwe.py

## Observations:
- helpful for user to know upfront that the MetaMask message for personal sign can't be a dict
    - here, that's handled by enclosing dict in an array then extracting array[0] to get back the dict message
- unexpected behaviours(?):
    - instantiating a SiweMessage message fails without a message argument that includes a 'signature' field (this may not be unexpected but seemed somehow unintuitive?)
    - SiweMessage.validate(sig) complains if the message keys of the original message aren't formatted as (all lower case) + (name words separated by underscore _)
