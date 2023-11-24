public_dataset_info = {
    "Chicago City Salaries": {
        "project_id": "genai-prabha-learn",
        "dataset": "chicago",
        "table_name": "city_salary",
        "description": "Salaries of current chicago city employees with Employee Name and Titles",
        "column_descriptions": """
        Name: Name of the employee.
        job_titles: Title of the employee at the time when the data were updated.
        department: Department where the employee worked.
        full_or_part_time: Indicates whether the employee was employed full-time (F) or part-time (P).
        salary_or_hourly: (SALARY / HOURLY) Defines whether an employee is paid on an hourly basis or salary basis. Hourly employees are further defined by their typical hours, as detailed in the typical_hours column.
        typical_hours (Frequency Description): Describes the typical amount of work for hourly employees. This data does not apply to salary employees. Examples include: 40 hours - Employee paid on an hourly basis; works an 8-hour day; can be either full-time permanent or full-time temporary (seasonal employee); 35 hours - Employee paid on an hourly basis; works a 7-hour day; can be either full-time permanent or full-time temporary (seasonal employee); 20 hours - Employee paid on a part-time, hourly basis; typically works a 4-hour day, 5 days a week; 10 hours - Employee paid on a part-time, hourly basis; works 10 hours or less in a week.
        annual_salary: Annual salary rates. This only applies to employees whose pay frequency is "Salary". Hourly employees' rates are only shown in the hourly_rate column.
        hourly_rate: The hourly salary rates for individuals whose pay frequency is "hourly". The varying hours worked throughout the week by hourly employees are described in the typical_hours column
        """
    },


    "Chicago Crime": {
        "project_id": "bigquery-public-data",
        "dataset": "chicago_crime",
        "table_name": "crime",
        "description": "Crime incidents reported in the city of Chicago since 2001",
        "column_description": """
        unique_key: Unique identifier for the record.
        case_number: The Chicago Police Department RD Number (Records Division Number), which is unique to the incident.
        date: Date when the incident occurred. This is sometimes a best estimate.
        block: The partially redacted address where the incident occurred, placing it on the same block as the actual address.
        iucr: The Illinois Uniform Crime Reporting code. This is directly linked to the primary_type and description. See the list of IUCR codes at IUCR Codes.
        primary_type: The primary description of the IUCR code.
        description: The secondary description of the IUCR code, a subcategory of the primary description.
        location_description: Description of the location where the incident occurred.
        arrest: Indicates whether an arrest was made.
        domestic: Indicates whether the incident was domestic-related as defined by the Illinois Domestic Violence Act.
        beat: Indicates the beat where the incident occurred. A beat is the smallest police geographic area – each beat has a dedicated police beat car. Three to five beats make up a police sector, and three sectors make up a police district. The Chicago Police Department has 22 police districts. See the beats at Police Beats.
        district: Indicates the police district where the incident occurred. See the districts at Police Districts.
        ward: The ward (City Council district) where the incident occurred. See the wards at City Council Wards.
        community_area: Indicates the community area where the incident occurred. Chicago has 77 community areas. See the community areas at Community Areas.
        fbi_code: Indicates the crime classification as outlined in the FBI's National Incident-Based Reporting System (NIBRS). See the Chicago Police Department listing of these classifications at FBI Crime Classifications.
        x_coordinate: The x coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.
        y_coordinate: The y coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.
        year: Year the incident occurred.
        updated_on: Date and time the record was last updated.
        latitude: The latitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
        longitude: The longitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
        location: The location where the incident occurred in a format that allows for creation of maps and other geographic operations on this data portal. This location is shifted from the actual location for partial redaction but falls on the same block.
        """
    },

    "Chicago City 311 requests": {
        "project_id": "genai-prabha-learn",
        "dataset": "chicago",
        "table_name": "311_service_requests",
        "description": "311 Service Requests received by the City of Chicago. This dataset includes requests created after the launch of the new 311 system on 12/18/2018 and some records from the previous system, indicated in the LEGACY_RECORD column.",
        "column_descriptions": """
        SR_NUMBER: SR Number
        SR_TYPE: SR Type
        SR_SHORT_CODE: An internal code corresponding to the Service Request Type. This code allows for searching and filtering more easily than using the full SR_TYPE value.
        CREATED_DEPARTMENT: The department, if any, that created the service request.
        OWNER_DEPARTMENT: The department with initial responsibility for the service request.
        STATUS: Status
        ORIGIN: How the request was opened. Some values, such as Generated In House and Mass Entry result from the City's own operations.
        CREATED_DATE: Created Date
        LAST_MODIFIED_DATE: Last Modified Date
        CLOSED_DATE: Closed Date
        STREET_ADDRESS: Street Address
        CITY: City
        STATE: State
        ZIP_CODE: Zip Code
        STREET_NUMBER: Street Number
        STREET_DIRECTION: Street Direction
        STREET_NAME: Street Name
        STREET_TYPE: Street Type
        DUPLICATE: Is this request a duplicate of another request?
        LEGACY_RECORD: Did this request originate in the previous 311 system?
        LEGACY_SR_NUMBER: If this request originated in the previous 311 system, the original Service Request Number.
        PARENT_SR_NUMBER: Parent Service Request of the record if applicable. If the current Service Request record has been identified as a duplicate request, the record will be created as a child of the original request.
        COMMUNITY_AREA: Community Area
        WARD: Ward
        ELECTRICAL_DISTRICT: Electrical District
        ELECTRICITY_GRID: Electricity Grid
        POLICE_SECTOR: Police Sector
        POLICE_DISTRICT: Police District
        POLICE_BEAT: Police Beat
        PRECINCT: Precinct
        SANITATION_DIVISION_DAYS: Sanitation Division Days
        CREATED_HOUR: The hour of the day component of CREATED_DATE.
        CREATED_DAY_OF_WEEK: The day of the week component of CREATED_DATE. Sunday=1
        CREATED_MONTH: The month component of CREATED_DATE
        X_COORDINATE: The x coordinate of the location in State Plane Illinois East NAD 1983 projection.
        Y_COORDINATE: The y coordinate of the location in State Plane Illinois East NAD 1983 projection.
        LATITUDE: The latitude of the location.
        LONGITUDE: The longitude of the location.
        LOCATION: The location in a format that allows for creation of maps and other geographic operations on this data portal.
    """
    }
}
