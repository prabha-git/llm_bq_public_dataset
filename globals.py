class GlobalConfig:
    def __init__(self):
        self.project_id = None
        self.dataset = None
        self.table_name = None

    def update_variable(self, var_name, new_value):
        if var_name == "project_id":
            self.project_id = new_value
        elif var_name == "dataset":
            self.dataset = new_value
        elif var_name == "table_name":
            self.table_name = new_value
        else:
            raise ValueError("Undefined Global Variable")

    def get_variable(self, var_name):
        if var_name == "project_id":
            return self.project_id
        elif var_name == "dataset":
            return self.dataset
        elif var_name == "table_name":
            return self.table_name
        else:
            raise ValueError("Undefined Global Variable")

# Usage
config = GlobalConfig()
def update_global_variable(var_name,new_value):
    config.update_variable(var_name, new_value)

def get_global_variable(var_name):
    return(config.get_variable(var_name))
