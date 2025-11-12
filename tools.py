from smolagents import Tool



class CheckClientStatusTool(Tool):
    name = "check_client_status"
    description = """
    Check if a given company is an existing client of the bank.
    Returns a string indicating whether it is a client."""
    inputs = {
        "company_name": {
            "type": "string",
            "description": 
                "The name of the company to check."
        }
    }
    output_type = "string"

    def forward(self, company_name: str):
        client_list = ["renault", "bnp paribas", "arcelormittal", "stellantis"]
        if company_name.lower() in client_list:
            return f"{company_name} IS a client."
        return f"{company_name} is NOT a client."
