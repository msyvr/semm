# Demo: Flask app with Sign In With Ethereum for MetaMask users

`Flask` + `JavaScript` + `Python` + `MetaMask API` + `SIWE`

This demo Flask app enables authentication of [MetaMask](https://metamask.io/) users via [Sign In With Ethereum](https://login.xyz/) per [EIP 4361](https://eips.ethereum.org/EIPS/eip-4361).

A Python backend mediates the SIWE authentication. A JavaScript/HTML front end mediates communication with users via their MetaMask accounts. 

MetaMask injects an API into websites visited by logged-in MetaMask users; this API is leveraged to request a user signature on an EIP 4361 conforming message. The message and signature are then verified by SIWE to enable user login to the demo app: the user's decentralized identity is authenticated, eliminating the need for traditional username/password authentication.

## Use
- see deploy.sh

## Status
- login landing page
- retrieve user eth address
- build EIP-4316 conforming message for user signature
- generate MetaMask personal sign request
- instantiate SiweMessage with arg = message (from MetaMask sig request)
- redirect for unverified credentials (no 'login')
- info page (basics of how siwe works)

### Currently disabled
- final validation by siwe: tentative protocol (in process), a value error is currently raised during the decentralized identity authentication process
