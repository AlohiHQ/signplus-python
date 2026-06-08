python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\
pip install dist\signplus_developer_api_v2_spec_sdk-1.0.0-py3-none-any.whl --force-reinstall
