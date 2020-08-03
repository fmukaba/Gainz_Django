from storages.backends.azure_storage import AzureStorage

class AzureStaticStorage(AzureStorage):
    account_name = 'getgainzstorage'
    account_key = 'K7V1Nsx0KU0XxXD0UjdUaaeT9mZQW4qbdHmhUJycrKce/+BTVpqNtxuUMAiGSAsgW69q7BM1KDCsgMz2XdtgpQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None