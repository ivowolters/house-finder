from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"    
    def ready(self):
        """
        Sync database from blob storage on app startup
        """
        try:
            from main.blob_storage import sync_database_from_blob
            print("Syncing database from blob storage...")
            sync_database_from_blob()
        except Exception as e:
            print(f"Warning: Could not sync database from blob storage: {e}")
            print("Using local database instead")