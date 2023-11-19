public_dataset_info = {
    "Chicago Crime": {
        "project_id":"bigquery-public-data",
        "dataset":"chicago_crime",
        "table_name":"crime",
        "description":"Crime incidents reported in the city of Chicago since 2001",
        "column_descriptions":"""
        Name: Name of employee.
        Job Titles: Title of employee at the time when the data were updated.
        Department: Department where employee worked.
        Full or Part-Time: Whether the employee was employed full- (F) or part-time (P).
        Salary or Hourly: Defines whether an employee is paid on an hourly basis or salary basis. Hourly employees are further defined by the number of hours they work in a week. See the "Frequency Description" column.
        Typical Hours: Describes the typical amount of work for hourly employees. This data does not apply to salary employees. 40 - Employee paid on an hourly basis; works an 8 hour day; can be either full-time permanent (FT/P) or full-time temporary (FT-T) which is a seasonal employee; 35 - Employee paid on an hourly basis; works a 7 hour day; can be either full-time permanent (FT/P) or full-time temporary (FT-T) which is a seasonal employee; 20 - Employee paid on a part-time, hourly basis; typically works a 4 hour day, 5 days a week; 10 - Employee paid on a part-time, hourly basis; works 10 hours or less in a week.
	    Annual Salary: Annual salary rates. Only applies for employees whose pay frequency is "Salary". Hourly employees rates are only shown in "Hourly Rates" column.
	    Hourly Rate: The hourly salary rates for individuals whose pay frequency is "hourly". Hourly employees have varying hours worked throughout the week, which is described in the "Frequency Description" column.
        """

    },

    "Chicago City Salaries": {
        "project_id":"bigquery-public-data",
        "dataset": "austin_financial",
        "table_name": "salary",
        "description": "Salaries of current chicago city employees with Employee Name and Titles",
        "column_description":"""
        ID: Unique identifier for the record.
        Case Number: The Chicago Police Department RD Number (Records Division Number), which is unique to the incident.
        Date: Date when the incident occurred. This is sometimes a best estimate.
        Block: The partially redacted address where the incident occurred, placing it on the same block as the actual address.
        IUCR: The Illinois Uniform Crime Reporting code. This is directly linked to the Primary Type and Description. See the list of IUCR codes at IUCR Codes.
        Primary Type: The primary description of the IUCR code.
        Description: The secondary description of the IUCR code, a subcategory of the primary description.
        Location Description: Description of the location where the incident occurred.
        Arrest: Indicates whether an arrest was made.
        Domestic: Indicates whether the incident was domestic-related as defined by the Illinois Domestic Violence Act.
        Beat: Indicates the beat where the incident occurred. A beat is the smallest police geographic area – each beat has a dedicated police beat car. Three to five beats make up a police sector, and three sectors make up a police district. The Chicago Police Department has 22 police districts. See the beats at Police Beats.
        District: Indicates the police district where the incident occurred. See the districts at Police Districts.
        Ward: The ward (City Council district) where the incident occurred. See the wards at City Council Wards.
        Community Area: Indicates the community area where the incident occurred. Chicago has 77 community areas. See the community areas at Community Areas.
        FBI Code: Indicates the crime classification as outlined in the FBI's National Incident-Based Reporting System (NIBRS). See the Chicago Police Department listing of these classifications at FBI Crime Classifications.
        X Coordinate: The x coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.
        Y Coordinate: The y coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.
        Year: Year the incident occurred.
        Updated On: Date and time the record was last updated.
        Latitude: The latitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
        Longitude: The longitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
        Location: The location where the incident occurred in a format that allows for creation of maps and other geographic operations on this data portal. This location is shifted from the actual location for partial redaction but falls on the same block.
        """
    }
}
