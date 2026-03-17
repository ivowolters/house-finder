"""
Azure Blob Storage utility functions for reading and querying data
"""
import os
import json
from azure.storage.blob import BlobServiceClient
from django.conf import settings


def get_blob_service_client():
    """
    Get Azure Blob Service Client configured for local development (Azurite) or Azure
    """
    connection_string = getattr(settings, 'AZURE_STORAGE_CONNECTION_STRING', None)
    
    if not connection_string:
        # Default to Azurite for local development
        connection_string = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
    
    return BlobServiceClient.from_connection_string(connection_string)


def list_blobs(container_name='houses'):
    """
    List all blobs in a container
    """
    try:
        client = get_blob_service_client()
        container_client = client.get_container_client(container_name)
        
        blobs = []
        for blob in container_client.list_blobs():
            blobs.append({
                'name': blob.name,
                'size': blob.size,
                'last_modified': blob.last_modified
            })
        
        return blobs
    except Exception as e:
        print(f"Error listing blobs: {e}")
        return []


def read_blob_text(blob_name, container_name='houses'):
    """
    Read text content from a blob
    """
    try:
        client = get_blob_service_client()
        blob_client = client.get_blob_client(container=container_name, blob=blob_name)
        
        download_stream = blob_client.download_blob()
        return download_stream.readall().decode('utf-8')
    except Exception as e:
        print(f"Error reading blob {blob_name}: {e}")
        return None


def read_blob_json(blob_name, container_name='houses'):
    """
    Read and parse JSON content from a blob
    """
    content = read_blob_text(blob_name, container_name)
    if content:
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON from blob {blob_name}: {e}")
    return None


def read_blob_binary(blob_name, container_name='houses'):
    """
    Read binary content from a blob
    """
    try:
        client = get_blob_service_client()
        blob_client = client.get_blob_client(container=container_name, blob=blob_name)
        
        download_stream = blob_client.download_blob()
        return download_stream.readall()
    except Exception as e:
        print(f"Error reading blob {blob_name}: {e}")
        return None


def blob_exists(blob_name, container_name='houses'):
    """
    Check if a blob exists
    """
    try:
        client = get_blob_service_client()
        blob_client = client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.get_blob_properties()
        return True
    except Exception:
        return False


def upload_blob(file_path, blob_name=None, container_name='houses'):
    """
    Upload a file to blob storage
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if blob_name is None:
        blob_name = os.path.basename(file_path)
    
    try:
        client = get_blob_service_client()
        blob_client = client.get_blob_client(container=container_name, blob=blob_name)
        
        with open(file_path, 'rb') as data:
            blob_client.upload_blob(data, overwrite=True)
        
        return f"{container_name}/{blob_name}"
    except Exception as e:
        print(f"Error uploading blob: {e}")
        return None
