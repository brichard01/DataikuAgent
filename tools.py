from smolagents import Tool
import re

class ExtractCompaniesTool(Tool):
    name = "extract_companies"
    description = """
    Extract company names mentioned in a news article.
    If no company is explicitly mentioned, try to infer the sector.
    Returns a comma-separated list of company names or a sector string."""
    inputs = {
        "news_text": {
            "type": "string",
            "description": "The news article or headline text to analyze."
        }
    }
    output_type = "string"

    def forward(self, news_text: str):
        companies = ["Renault", "TotalEnergies", "BNP Paribas", "ArcelorMittal", "Stellantis"]
        found = [c for c in companies if c.lower() in news_text.lower()]
        if found:
            return ", ".join(found)
        if "energy" in news_text.lower():
            return "Sector: Energy"
        if "automotive" in news_text.lower():
            return "Sector: Automotive"
        return "No company detected"

class CheckClientStatusTool(Tool):
    name = "check_client_status"
    description = """
    Check if a given company is an existing client of the bank.
    Returns a string indicating whether it is a client."""
    inputs = {
        "company_name": {
            "type": "string",
            "description": "The name of the company to check."
        }
    }
    output_type = "string"

    def forward(self, company_name: str):
        client_list = ["Renault", "BNP Paribas", "ArcelorMittal"]
        if company_name in client_list:
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