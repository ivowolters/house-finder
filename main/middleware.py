"""
Middleware to sync database from blob storage (only periodically to avoid excessive requests)
"""
import time
from django.utils.deprecation import MiddlewareMixin
from main.blob_storage import sync_database_from_blob


class DatabaseSyncMiddleware(MiddlewareMixin):
    """
    Middleware that syncs the database from blob storage periodically.
    Only syncs if the database hasn't been synced recently to avoid excessive downloads and connection issues.
    """
    
    _last_sync_time = 0
    _sync_interval = 300  # Only sync every 5 minutes (300 seconds)
    
    def process_request(self, request):
        """
        Sync database from blob storage only if enough time has passed
        """
        current_time = time.time()
        
        # Only sync if enough time has passed since last sync
        if current_time - self._last_sync_time > self._sync_interval:
            try:
                sync_database_from_blob()
                self._last_sync_time = current_time
            except Exception as e:
                print(f"Warning: Could not sync database from blob storage: {e}")
                # Continue with local database if sync fails
        
        return None
