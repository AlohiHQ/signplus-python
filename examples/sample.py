from signplus import Signplus

sdk = Signplus(access_token="YOUR_ACCESS_TOKEN", timeout=10000)

result = sdk.signplus.get_envelope(envelope_id="envelope_id")

print(result)
