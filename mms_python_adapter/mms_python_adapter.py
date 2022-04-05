from mms_python_client import ApiClient, Configuration
from mms_python_client.apis import AuthApi, ElementsApi
from mms_python_client.models import Element, ElementsRequest, ElementsResponse


class MMSAdapter(object):

    def __init__(self, server: str, project_id: str, ref_id: str) -> None:
        self.config = Configuration()
        self.config.host = server

        self.client = ApiClient(self.config)

        self.elem_api = ElementsApi(self.client)

        self.project_id = project_id
        self.ref_id = ref_id

    def login(self, username: str, password: str) -> str:
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
    def get_element(self, element_id: str) -> Element:
        return self.elem_api.get_element(self.project_id, self.ref_id, element_id)._data_store['elements'][0]

    def update_element_value(self, element_id: str, value: str) -> ElementsResponse:
        element = self.get_element(element_id)
        default_value: dict = element['defaultValue']
        default_value['value'] = value
        element.set_attribute('defaultValue', default_value)
        element_req = ElementsRequest([element])
        element_respo = self.elem_api.create_or_update_elements(self.project_id, self.ref_id,
                                                                element_req)

        return element_respo

    def update_element_default_value(self, element_id: str, default_value: dict) -> ElementsResponse:
        element = self.get_element(element_id)
        element.set_attribute('defaultValue', default_value)
        element_req = ElementsRequest([element])
        element_respo = self.elem_api.create_or_update_elements(self.project_id, self.ref_id,
                                                                element_req)

        return element_respo

    def get_documentation(self, element_id: str) -> str:
        element = self.get_element(element_id)
        return element['documentation']

    def update_element_documentation(self, element_id: str, documentation: str) -> ElementsResponse:
        element = self.get_element(element_id)
        element.set_attribute('documentation', documentation)
        element_req = ElementsRequest([element])
        element_respo = self.elem_api.create_or_update_elements(self.project_id, self.ref_id,
                                                                element_req)
        return element_respo


if __name__ == "__main__":
    pass
