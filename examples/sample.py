from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN", base_url=Environment.DEFAULT.value, timeout=10000
)

result = sdk.envelope_id.delete_envelope(envelope_id="envelope_id")

print(result)
