from .. import DixaResource, DixaVersion


class EndUserResource(DixaResource):
    """
    https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/
    """

    resource = "endusers"
    dixa_version: DixaVersion = "v1"

    def anonymize(self, end_user_id: str):
        """Anonymize an end user.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/patchEndusersUseridAnonymize
        """
        return self.client.patch(f"{self.url}/{end_user_id}/anonymize")

    def create(self, body):
        """Create an end user.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/postEndusers
        """
        return self.client.post(self.url, body)

    def create_bulk(self, body):
        """Create end users.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/postEndusersBulk
        """
        return self.client.post(f"{self.url}/bulk", body)

    def get(self, end_user_id: str):
        """Get an end user by id.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/getEndusersUserid
        """
        return self.client.get(f"{self.url}/{end_user_id}")

    def list_conversations(self, end_user_id: str, query: dict | None = None):
        """List conversations.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/getEndusersUseridConversations
        """
        return self.client.get(f"{self.url}/{end_user_id}/conversations", query)

    def list(self, query: dict | None = None):
        """List end users.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/getEndusers
        """
        return self.client.get(self.url, query)

    def patch(self, end_user_id: str, body):
        """Patch an end_user.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/patchEndusersUserid
        """
        return self.client.patch(f"{self.url}/{end_user_id}", body)

    def patch_end_user_custom_attributes(self, end_user_id: str, body):
        """Patch end user custom attributes.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/patchEndusersUseridCustom-attributes
        """
        return self.client.patch(f"{self.url}/{end_user_id}/custom-attributes", body)

    def patch_bulk(self, body):
        """Patch end users.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/patchEndusers
        """
        return self.client.patch(self.url, body)

    def update(self, end_user_id, body):
        """Update an end user.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/putEndusersUserid
        """
        return self.client.put(f"{self.url}/{end_user_id}", body)

    def update_bulk(self, body):
        """Update an end users.
        https://docs.dixa.io/openapi/dixa-api/v1/tag/End-Users/#tag/End-Users/operation/putEndusers
        """
        return self.client.put(self.url, body)