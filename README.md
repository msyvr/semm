# Demo: Flask app with Sign In With Ethereum for MetaMask users

## Use
- instructions in deploy.sh

## Working:
- login landing page
- retrieve user eth address
- build EIP-4316 conforming message for user signature
- generate MetaMask personal sign request
- instantiate SiweMessage with arg = message (from MetaMask sig request)
- redirect for unverified credentials (no 'login')
- info page (basics of how siwe works)
- logged-in page (only if accessed directly by URL; the app doesn't redirect there as siwe isn't validating the metamask data)

## Not working:
- message validation by siwe :(
    - ? check message parsing in siwe.py

## Observations:
- helpful for user to know upfront that the MetaMask message for personal sign can't be a dict
    - here, that's handled by enclosing dict in an array then extracting message[0] to get back the dict message
- unexpected behaviours(?):
    - instantiating a SiweMessage message fails without a message argument that includes a 'signature' field (this may not be unexpected but seemed somehow unintuitive?)
    - SiweMessage.validate(sig) complains if the message keys of the original message aren't formatted as (all lower case) + (name words separated by underscore _)

## Current 'got stuck' point
```
...verify.py", line 20, in verify_credentials

validation_outcome = siwe_message.validate(sig)

File "/Users/mspisar/.pyenv/versions/3.9.7/lib/python3.9/site-packages/siwe/siwe.py", line 209, in validate

raise InvalidSignature

siwe.siwe.InvalidSignature
```

- siwe.py line 209 corresponds to:
```
if address != self.address:

raise InvalidSignature
```

- so, let's comment out the .validate method and check the value of siwe_message['address'] that would be passed to that validation and compare with the original message dict value for 'address'
    -  (caveat: expecting the values from the original message and SiweMessage-generated message should match but, based on what I've seen in the codebase so far, I'm not 100% sure that's how siwe works, and the following may not be the appropriate vector for troubleshooting this issue):

```
print(siwe_message.address == msg[0]['address'])

True
```

- hmmm, this is going to take some more digging
- ... I stopped troubleshooting at this point (probably makes sense to confer with someone working on siwe-py)

## TODO
### get siwe to work! 
- next steps: check arg formats vs spec expectations

### tests
- the test are patchy: biased effort toward getting .validate() to work but was uncertain about tests that might help, wasn't clear on how TDD might help resolve

### set up user/session management for setting up routes with @login_required
- the restricted page can currently be accessed by entering that URL directly: unacceptable in production; for now, the app itself doesn't render that template unless the siwe credential verification is successful

### message for MetaMask signature
- let user know what they're signing (currently blank - didn't troubleshoot this, but it's important for UX and transparency generally)
