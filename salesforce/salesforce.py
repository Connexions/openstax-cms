from simple_salesforce import Salesforce as SimpleSalesforce
from django.conf import settings
from contextlib import ContextDecorator
import sys
from django.contrib.sessions.backends.db import SessionStore
from importlib import import_module
from django.conf import settings


class Salesforce(SimpleSalesforce, ContextDecorator):
    _default_session_key = 0

    def __init__(self, *args, **kwargs):
        session_store = SessionStore(session_key=self._default_session_key)
        if 'sf_instance' in session_store.keys() and 'sf_session_id' in session_store.keys():
            try:
                super(Salesforce, self).__init__(instance=session_store['sf_instance'],
                                                 session_id=session_store['sf_session_id'])
            except:
                raise RuntimeError("salesforce session failed")
        else:
            try:
                super(Salesforce, self).__init__(**settings.SALESFORCE)
            except AttributeError:
                super(Salesforce, self).__init__(*args, **kwargs)
            except TypeError:
                raise RuntimeError("salesforce init failed")
            session_store['sf_instance'] = self.sf_instance
            session_store['sf_session_id'] = self.session_id
            session_store.save()
            self.update_session_key(session_store.session_key)

    @classmethod
    def update_session_key(cls, key):
        cls._default_session_key = key

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        if not exc == (None, None, None):
            session_store = SessionStore(session_key=self._default_session_key)
            session_store.delete()
            self.update_session_key(None)
        return False

    def faculty_status(self, accounts_id=None):
        if accounts_id or accounts_id == 0:
            command = "SELECT Faculty_Verified__c FROM Contact "\
                "WHERE Accounts_ID__c = '{0}'".format(accounts_id)
            response = self.query(command)
            # each accounts key should be unique
            if response['totalSize'] == 1:
                status = response['records'][0]['Faculty_Verified__c']
                return status
        else:
            command = "SELECT Accounts_ID__c FROM Contact "\
                "WHERE Faculty_Verified__c = 'Confirmed' AND Accounts_ID__c != null"
            response = self.query(command)
            faculty_status_list = response['records']
            while 'nextRecordsUrl' in response.keys():
                response = self.query_more(response['nextRecordsUrl'], True)
                faculty_status_list = faculty_status_list + response['records']
            return faculty_status_list

    def adopters(self):
        # Field 'Id' is generated by salesforce 
        command = "SELECT Id, Name, Description, Website FROM Account WHERE Number_of_Adoptions__c > 0"
        response = self.query(command)
        adopters_list = response['records']
        while 'nextRecordsUrl' in response.keys():
            response = self.query_more(response['nextRecordsUrl'],True)
            adopters_list = adopters_list + response['records']
        return adopters_list

