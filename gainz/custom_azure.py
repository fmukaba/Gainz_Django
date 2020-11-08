from storages.backends.azure_storage import AzureStorage

class AzureStaticStorage(AzureStorage):
    account_name = 'getgainzstorage'
    account_key = '' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
