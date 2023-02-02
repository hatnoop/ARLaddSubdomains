from app.services.dns_query import DNSQueryBase
from app import utils


class Query(DNSQueryBase):
    def __init__(self):
        super(Query, self).__init__()
        self.source_name = "sortSubdomain"
        self.api_key = None

    def init_key(self, api_key=None):
        self.api_key = api_key

    def sub_domains(self, target):
        
        auth = ('admin', '6fGuJdMGjN4tu1y')
        url = "{}?domain={}".format(self.api_key,target)
        
        results = []
        content = utils.http_req(url, 'get', auth=auth, timeout=(30.1, 50.1))
        content = content.text
        content = content.strip()
        results = content.split('\n')
        return (results)