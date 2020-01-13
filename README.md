# MMS-Python-Adapter

This is a collection of "quality of life" improvements for using the Python client for 
the Model Management System (MMS).

# Purpose

The purpose of the MMS-Python adapter is to wrap the complex REST API functions into easy to use
Python functions allowing users to interact with a system model in a familiar tool. Access to model 
elements can allow users to run analyses or even model in Python.

# Classes
## MMSAdapter(_server_, _ref id_, _project id_)
Initializing a project object allows the user to set the server, reference ID, and project ID
then run methods on that project.

### login()
This method prompts for the users MMS credentials (username/password) then requests and stores a 
ticket to allow the user to run operations without having to log in constantly. Note the username 
and password are destryed once the ticket is retrived.

### logout()
This function clears any stored tickets.

### check_login()
This function returns True if the user is logged in and False otherwise.

### get_element(_element id_,_depth=depth_)
Returns an Element() object (defined in the MMS client) with the given ID. This is a dictionary
of the attributes of the retrived element and can be used to get the elements name, ID, 
documentation, etc. The depth parameter is an optional input and its default value is set to '0'. 
Note: `depth= -1` is the same as `recurse=true` 

### update_element_documentation(_element id_, _content_)
Sets the given elements documentation to _content_.

### update_element_name(_element id_, _name_)
Sets the given elements name to _name_.

### publish_table(_element id_, _table_)
Posts a table to the given elements documentation. Here, _table_ should be an HTML table.

### update_element_value(_element id_, _content_)
Sets the given elements default value to _content_. Note, _content_ must be JSON which contatins all appropriate fields for 
default value (not just the one to be updated).

# Installation Instructions

for pip: `pip install mms-python-adapter`

## Update Conda to Latest Version
Ensure Conda is updated to its latest version on the BASE environment in order to prevent dependency discrepancies. Enter via terminal:

`conda update conda -y`

## Pulling from conda-forge and Installation
The mms-python-adapter conda package will be on conda-forge. In order to pull and install the package onto a desired platform, such as JupyterLabs, first add the channel via Terminal:

`conda config --add channels conda-forge`

After the channel has been added, install the mms-python-adapter package with:

`conda install mms-python-adapter -y`

## Using MMS-Python-Adapter
Within your python script, import the adapter with:

`from mms_python_adapter import MMSAdapter`

Note: Although the package is named "mms-python-adapter", the base script is "adapter," and the actual functions are called through the "Adapter" class.

Finally, the Adapter is initialized with:
  1. Server
  2. ProjectID
  3. RefID
  
`adap = MMSAdapter(server, projectID, refID)`

The functions are listed above under "Classes."
