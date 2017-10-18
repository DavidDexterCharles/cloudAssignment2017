# CloudAssignment2017

## Entities

1.Transaction

2.Bank

3.Customer

## Build Instructions

### The following below has to be done because the version of the sdk in the docs is not the same as the latest version

* Check the version of azure using pip:
    * ```pip freeze```

* If version is not azure==0.30.0 , uninstall it first then  install version=0.30.0
    * ```pip uninstall azure```

* [Azure Stack supported version](https://docs.microsoft.com/uk-UA/azure/azure-stack/user/azure-stack-storage-dev/)
     * ```pip install -v azure-storage==0.30.0```
* [No module named azure.common](https://github.com/Azure/blobxfer/issues/25), please run both of the following commands below (yes they are duplicates)
    * ```sudo pip install --upgrade --force-reinstall blobxfer```
    * ```sudo pip install --upgrade --force-reinstall blobxfer```

* Run the app
    * ```python app.py```