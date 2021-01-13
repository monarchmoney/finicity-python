Finicityapi
=================


This SDK uses the Requests library and will work for Python ```2 >=2.7.9``` and Python ```3 >=3.4```.

How to configure:
=================
The generated code might need to be configured with your API credentials. 
To do that, open the file "Configuration.py" and edit its contents.

How to resolve dependencies: 
===========================
The generated code uses Python packages named requests, jsonpickle and dateutil.
You can resolve these dependencies using pip ( https://pip.pypa.io/en/stable/ ).

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r requirements.txt```

Note: You will need internet access for this step.

How to use:
===========
After having resolved the dependencies, you can easily use the SDK following these steps.

  1. Create a "finicityapi_test.py" file in the root directory.
  2. Use any controller as follows:
```python
from __future__ import print_function
from finicityapi.finicityapi_client import FinicityapiClient

api_client = FinicityapiClient()
controller = api_client.deprecated
response = controller.generate_connect_url_all_types(<required parameters if any>)

print(response.link)

# Or you can print more information
print(vars(response))
```