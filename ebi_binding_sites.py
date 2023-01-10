import requests
import json

def json_parser(inner_dict):
    results = []
    for dictionary in inner_dict:
        residue_number = dictionary.get('residue_number', 'ND')
        chem_comp_id = dictionary.get('chem_comp_id', 'ND')
        chain_id = dictionary.get('chain_id', 'ND')
        results.append((residue_number, chem_comp_id, chain_id))
    return results

def format_header(text: str) -> str:
    concat = '=-' * 40 + '\n'
    concat += f"{text : ^{len(concat)}}" + '\n'
    concat += '=-' * 40 + '\n'
    return concat

protein_id = '1cbs'
adress = "https://www.ebi.ac.uk/pdbe/api/pdb/entry/binding_sites/" + protein_id

# Send a request to the PDBe Binding Sites API
response = requests.get(adress)
print(response)
# Check the status code of the response to make sure the request was successful
if response.status_code == 200:
    # Parse the response data as a JSON object
    data = response.json()
    # print(json.dumps(data, indent=4, sort_keys=True))
    list_result = json_parser(data.get(protein_id)[0]["site_residues"])
    text = f"Residue\tChem\tChain"
    text = format_header(text)
    print(text)
    for term in list_result:
        residue_number, chem_comp_id, chain_id = term
        print(f"{residue_number:^20}\t{chem_comp_id:^20}\t{chain_id:^20}")
else:
    print("Request failed with status code", response.status_code)
