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


class GetSectorCompaniesTool(Tool):
    name = "get_sector_companies"
    description = """
    Return major companies in a given sector.
    Useful when no companies are explicitly mentioned in the news."""
    inputs = {
        "sector": {
            "type": "string",
            "description": "The sector to retrieve companies from, e.g., Energy, Automotive."
        }
    }
    output_type = "string"

    def forward(self, sector: str):
        sectors = {
            "Energy": ["TotalEnergies", "Engie"],
            "Automotive": ["Renault", "Stellantis"]
        }
        comps = sectors.get(sector, [])
        if comps:
            return ", ".join(comps)
        return "No known companies for this sector."