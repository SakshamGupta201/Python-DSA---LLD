from interfaces import ITarget


class XMLDataProvider:
    """Provides data in XML format."""
    def get_data(self, data: str) -> str:
        return f"<data>{data}</data>"



class XMLAdapter(ITarget):
    """Adapter to convert XML data to JSON format using the ITarget interface."""
    def __init__(self, xml_data_provider: XMLDataProvider):
        self.xml_data_provider = xml_data_provider

    def get_json_data(self) -> str:
        xml_data = self.xml_data_provider.get_data("Sample Data")
        # Simulate conversion from XML to JSON (for demo purposes)
        return f'{{"data": "{xml_data}"}}'



if __name__ == "__main__":
    adapter = XMLAdapter(XMLDataProvider())
    print(adapter.get_json_data())
