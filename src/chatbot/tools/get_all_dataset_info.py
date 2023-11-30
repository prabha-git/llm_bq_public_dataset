from src.dataset_info import public_dataset_info
from langchain.tools import tool
@tool
def get_all_dataset_info():
    """
    Provides details of all datasets to determine the feasibility of answering the user query.
    """
    formatted_output = ""

    for dataset_name, dataset_info in public_dataset_info.items():
        # Adding dataset name and basic info
        formatted_output += f"Dataset Name: {dataset_name}\n"
        formatted_output += f"Project ID: {dataset_info['project_id']}\n"
        formatted_output += f"Dataset: {dataset_info['dataset']}\n"
        formatted_output += f"Table Name: {dataset_info['table_name']}\n"
        formatted_output += f"Description: {dataset_info['description']}\n"

        # Adding column descriptions
        column_desc = dataset_info.get('column_descriptions') or \
                      dataset_info.get('column_description', '')
        formatted_output += "Column Descriptions:\n"
        for line in column_desc.strip().split('\n'):
            if line.strip():
                formatted_output += f"{line.strip()}\n"

        formatted_output += "\n"

    return formatted_output
