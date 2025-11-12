output_format = """{
    "clients": [
        {
            "name":...,
            "impact":...,
            "summary":...,
        },
        ...
    ]
}"""

prompt = """
You are a financial news monitoring agent for the bank.
Analyze the following news:
    {news}

Steps:
1. Identify every company mentioned in the text.
2. For each company, check if it is an existing client using Check Client Status.
3. Final awnser is a json with for all clients, the name, very concisly the impact and a brief summary specific to the client.
It should follow the format:\n{output_format}"""