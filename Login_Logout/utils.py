import uuid
from django.conf import settings




def generate_ref_code():
    return str(uuid.uuid4()).replace('-', '')[:12]


    
