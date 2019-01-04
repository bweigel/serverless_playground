see Issue https://github.com/UnitedIncome/serverless-python-requirements/issues/209
===

In the example project `vendor2` is not packaged in `function-two` as should be.

##### serverless.yml

```yaml
...
package:
  individually: true
  exclude:
    - '**/*'
  include:
    - 'fn/**'

functions:
  function-one:
    handler: main.handler
    module: fn
    vendor: ./vendor
  function-two:
    handler: main.handler
    module: fn
    vendor: ./vendor2
```

##### `serverless package`

```bash
$ sls package
Serverless: Generated requirements from /home/bweigel/Projects/OSS/serverless_playground/sls_package/fn/requirements.txt in /home/bweigel/Projects/OSS/serverless_playground/sls_package/.serverless/requirements.txt...
Serverless: Copying from /home/bweigel/Projects/OSS/serverless_playground/sls_package/.serverless/requirements.txt into /home/bweigel/Projects/OSS/serverless_playground/sls_package/.serverless/fn/requirements.txt ...
Serverless: Installing requirements from /home/bweigel/Projects/OSS/serverless_playground/sls_package/.serverless/requirements/requirements.txt ...
Serverless: Copying vendor libraries from ./vendor to /home/bweigel/Projects/OSS/serverless_playground/sls_package/.serverless/requirements...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...

$ zipinfo -1 .serverless/fn-packaging_test-dev-function-one.zip | sort
dataclasses-0.6.dist-info/
dataclasses-0.6.dist-info/INSTALLER
dataclasses-0.6.dist-info/METADATA
dataclasses-0.6.dist-info/RECORD
dataclasses-0.6.dist-info/top_level.txt
dataclasses-0.6.dist-info/WHEEL
dataclasses.py
__init__.py
main.py
other_module.py
__pycache__/
__pycache__/__init__.cpython-36.pyc
__pycache__/other_module.cpython-36.pyc
__pycache__/yam.cpython-36.pyc
requirements.txt
vendor_lib_a.py
yam.py

$ zipinfo -1 .serverless/fn-packaging_test-dev-function-two.zip | sort
dataclasses-0.6.dist-info/
dataclasses-0.6.dist-info/INSTALLER
dataclasses-0.6.dist-info/METADATA
dataclasses-0.6.dist-info/RECORD
dataclasses-0.6.dist-info/top_level.txt
dataclasses-0.6.dist-info/WHEEL
dataclasses.py
__init__.py
main.py
other_module.py
__pycache__/
__pycache__/__init__.cpython-36.pyc
__pycache__/other_module.cpython-36.pyc
__pycache__/yam.cpython-36.pyc
requirements.txt
vendor_lib_a.py
yam.py
```
