from signplus_developer_api_v2_spec_sdk import SignplusDeveloperApiV2SpecSdk

sdk = SignplusDeveloperApiV2SpecSdk(access_token="YOUR_ACCESS_TOKEN", timeout=10000)

result = sdk.signplus.get_envelope(envelope_id="envelope_id")

print(result)
