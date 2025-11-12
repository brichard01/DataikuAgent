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
        client_list = ["google cloud", "dataiku"]
        if company_name.lower() in client_list:
            return f"{company_name} IS a client."
        return f"{company_name} is NOT a client."
    
class CheckClientRelationsTool(Tool):
    name = "check_client_relations"
    description = """
    Check if a given company has a directrelation with a client of the bank.
    Returns a string indicating all clients related to the company and the nature of the relation."""
    inputs = {
        "company_name": {
            "type": "string",
            "description": 
                "The name of the company to check relations."
        }
    }
    output_type = "string"

    def forward(self, company_name: str):
        relations_dict = {
            'stellantis': {
                'Peugeot': 'Peugeot is owned by Stellantis'
            }
        }
        res = ''
        if company_name.lower() in relations_dict.keys():
            relations = relations_dict[company_name.lower()]
            for client, relation in relations.items():
                res = res + f'Our client {client} is in relation with {company_name}. {client} must be in the final output\n'
                res = res + f'The relation is: {relation}\n'
        if not res:
            res = f'{company_name} is not linked to another client'
        return res
