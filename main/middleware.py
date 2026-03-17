"""
Middleware to sync database from blob storage before processing requests
"""
from django.utils.deprecation import MiddlewareMixin
from main.blob_storage import sync_database_from_blob


class DatabaseSyncMiddleware(MiddlewareMixin):
    """
    Middleware that syncs the database from blob storage before each request.
    This ensures the application always queries the latest version from blob storage.
    """
    
    def process_request(self, request):
        """
        Sync database from blob storage before processing the request
        """
        try:
            sync_database_from_blob()
        except Exception as e:
            print(f"Warning: Could not sync database from blob storage: {e}")
            # Continue with local database if sync fails
        
        return None
