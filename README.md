# MMS-Python-Adapter

This is a collection of "quality of life" improvements for using the Python client for 
the Model Management System (MMS).

# Purpose

The purpose of the MMS-Python adapter is to wrap the complex REST API functions into easy to use
Python functions allowing users to interact with a system model in a familiar tool. Access to model 
elements can allow users to run analyses or even model in Python.

# Classes
## MMSAdapter(_server_, _project id_, _ref id_)
Initializing a project object allows the user to set the server, reference ID, and project ID
then run methods on that project.

### login()
This method prompts for the users MMS credentials (username/password) then requests and stores a 
ticket to allow the user to run operations without having to log in constantly. Note the username 
and password are destryed once the ticket is retrived.

### logout()
This function clears any stored tickets.


### get_element(_element id_)
Returns an Element() object (defined in the MMS client) with the given ID. This is a dictionary
of the attributes of the retrived element and can be used to get the elements name, ID, 
documentation, etc. The depth parameter is an optional input and its default value is set to '0'. 

### get_documentation(_element id_)
Returns a documentation string specified in speciifed Element as a tag.

### update_element_documentation(_element id_, _content_)
Sets the given elements documentation to _content_.

### update_element_default_value(_element id_, _content_)
Sets the given elements default value to _content_. Note, _content_ must be JSON which contatins all appropriate fields for 
default value (not just the one to be updated).

### update_element_value(_element id_, _value_)
Sets the given element value to _value_.
