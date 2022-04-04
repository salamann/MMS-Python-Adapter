from mms_python_client import ApiClient, Configuration
from mms_python_client.apis import AuthApi, ElementsApi
from mms_python_client.models import Element, ElementsRequest, ElementsResponse


class MMSAdapter(object):

    def __init__(self, server, project_id, ref_id):
        self.config = Configuration()
        self.config.host = server

        self.client = ApiClient(self.config)

        self.elem_api = ElementsApi(self.client)

        self.project_id = project_id
        self.ref_id = ref_id

    def login(self, username, password):
        self.config.username = username
        self.config.password = password
        self.client = ApiClient(self.config)
        auth_instance = AuthApi(self.client)
        self.token = auth_instance.get_authentication_token()
        self.config = Configuration(access_token=self.token['token'])
        self.client = ApiClient(self.config)

        return "Logged in as " + username

    def logout(self):
        self.config.api_key.clear()

    # depth= -1 same as recurse=true
    def get_element(self, element_id):
        return self.elem_api.get_element(self.project_id, self.ref_id, element_id)

    def update_element_value(self, element_id, value):
        # hardcoding this because the Element class doesn't commit properly
        element: ElementsResponse = self.get_element(element_id)
        default_value: dict = element._data_store['elements'][0]['defaultValue']
        default_value['value'] = value
        element.set_attribute('defaultValue', default_value)
        element_req = ElementsRequest([element])
        element_respo = self.elem_api.create_or_update_elements(self.project_id, self.ref_id,
                                                                element_req)

        return element_respo


if __name__ == "__main__":
    pass
