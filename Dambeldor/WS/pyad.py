#Connecting to Active Directory

# import pyad

# pyad.set_defaults(ldap_server="Google.local", username="mohammadreza", password="P@ssw0rd")
# user = pyad.aduser.ADUser.from_cn("AliBase")

#or you use user = aduser.ADUser.from_cn("myuser", options=dict(ldap_server="dc1.domain.com"))




############################################
#Basic Object Manipulation

# user1 = aduser.ADUser.from_dn("cn=myuser, ou=staff, dc=domain, dc=com")
# user2 = aduser.ADUser.from_cn("myuser")
# user3 = aduser.ADUser.from_guid("XXX-XXX-XXX")


# #some user
# user1 = ADUser.from_cn("myuser1")
# user2 = ADUser.from_cn("myuser2")
# group = ADGroup.from_dn("staff")

# group.add_members([user1, user2])

# for user in group.get_members():
#     print user1.



#################################################

# user1 = ADUser.from_cn("myuser1")
# user.set_attribute("description", "new description")
# user.append_to_attribute("member", "cn=myuser1, ou=staff, dc=domain, dc=com")



##############################################
#Creating, Moving, and Deleting Objects

# ou = ADContainer.from_dn("ou=workstations, dc=domain, dc=com")

# # create a new group without any optional attributes
# new_computer = ADComputer.create("WS-489", ou)

# # create a new group with additional attributes
# new_group = ADGroup.create("IT-STAFF", security_enabled=True, scope='UNIVERSAL',
#                 optional_attributes = {"description":"all IT staff in our company"})

# ou = ADContainer.from_dn("ou=workstations, dc=domain, dc=com")
# computer = ou.create_computer("WS-490")

# computer = ADComputer.from_cn("WS-500")
# computer.move(ADContainer.from_dn("ou=workstations, ou=HR, dc=company, dc=com"))

# computer = ADComputer.from_cn("WS-500")
# computer.rename("WS-501")
# ADComputer.from_cn("WS-500").delete()



#################################################
#Searching Active Directory

# import pyad.adquery
# q = pyad.adquery.ADQuery()

# q.execute_query(
#     attributes = ["distinguishedName", "description"],
#     where_clause = "objectClass = '*'",
#     base_dn = "OU=users, DC=domain, DC=com"
# )

# for row in q.get_results():
#     print row["distinguishedName"]



# ADObject
# class pyad.adobject.ADObject(distinguished_name=None, adsi_ldap_com_object=None, options={})[source]
# Python object that represents any active directory object.

# add_to_group(group)[source]
# Adds current object to the specified group. group expects an ADGroup object.

# adsPath
# ADsPath of Active Directory object (such as ‘LDAP://cn=me,...,dc=com‘

# append_to_attribute(attribute, valuesToAppend)[source]
# Appends values in list valuesToAppend to the specified multi-valued attribute. valuesToAppend can contain a single value or a list of multiple values.

# clear_attribute(attribute)[source]
# Clears (removes) the specified LDAP attribute from the object. Identical to setting the attribute to None or [].

# clear_managedby()[source]
# Sets object to be managedBy nobody

# delete()[source]
# Deletes the object from the domain

# disable()[source]
# Disables the user or computer

# dn
# Distinguished Name (DN) of the object

# dump_to_xml(whitelist_attributes=[], blacklist_attributes=[])[source]
# Dumps object and all human-readable attributes to an xml document which is returned as a string.

# enable()[source]
# Enables the user or computer

# classmethod from_com_object(com_object)[source]
# Generates ADObject based on an existing ADSI com object

# classmethod from_dn(distinguished_name, options={})[source]
# Generates ADObject based on distinguished name

# classmethod from_guid(guid, options={})[source]
# Generates ADObject based on GUID

# get_allowed_attributes()[source]
# Returns a list of allowed attributes for the particular object. These attributes may be defined, but are not guaranteed to be.

# get_attribute(attribute, always_return_list=True, source='LDAP')[source]
# Returns the value of any allowable LDAP attribute of the specified object.

# Keyword arguments:
# attribute – any schema-allowed LDAP attribute (case insensitive). The attribute does not need to be defined. always_return_list – if an attribute has a single value, this specifies whether to return only the

# value or to return a list containing the single value. Similarly, if true, a query on an undefined attribute will return an empty list instead of a None object. If querying an attribute known to only contain at most one element, then it is easier to set to false. Otherwise, if querying a potentially multi-valued attribute, it is safest to leave at default.
# source – either ‘LDAP’ or ‘GC’

# Note to experienced ADSI users:
# If an attribute is undefined, getAttribute() will return None or [] and will not choke on the attribute.
# In regards to always_return_list, True has similar behavior to getEx() whereas False is similar to Get().
# get_domain()
# Returns the domain to which the object belongs.

# get_mandatory_attributes()[source]
# Returns a list of mandatory attributes for the particular object. These attributes are guaranteed to be defined.

# get_memberOfs(recursive=False, scope='all')
# Get the groups that this object is a member of

# get_optional_attributes()[source]
# Returns a list of optional attributes for the particular object. These attributes may be defined, but are not guaranteed to be.

# get_uSNChanged()
# Returns uSNChanged as a single integer from the current domain controller

# get_user_account_control_settings()[source]
# Returns a dictionary of settings stored within UserAccountControl. Expected keys for the dictionary are the same as keys in the ADS_USER_FLAG dictionary. Further information on these values can be found at http://msdn.microsoft.com/en-us/library/aa772300.aspx.

# guid
# Object GUID of the object

# guid_str
# Object GUID of the object

# is_member_of(group, recursive=False)
# Check whether this object is a member of the given group

# move(new_ou_object)[source]
# Moves the object to a new organizationalUnit.

# new_ou_object expects a ADContainer object where the current object will be moved to.

# parent_container
# Object representing the container in which this object lives

# parent_container_path
# Returns the DN of the object’s parent container.

# prefixed_cn
# Prefixed CN (such as ‘cn=mycomputer’ or ‘ou=mycontainer’ of the object

# remove_from_attribute(attribute, valuesToRemove)[source]
# Removes any values in list valuesToRemove from the specified multi-valued attribute.

# remove_from_group(group)[source]
# Removes current object from the specified group. group expects an ADGroup object to which the current object belongs.

# rename(new_name, set_sAMAccountName=True)[source]
# Renames the current object within its current organizationalUnit. new_name expects the new name of the object (just CN not prefixed CN or distinguishedName).

# set_managedby(user)[source]
# Sets managedBy on object to the specified user

# set_user_account_control_setting(userFlag, newValue)[source]
# Sets a single setting in UserAccountControl.

# UserFlag must be a value from ADS_USER_FLAG dictionary keys. More information can be found at http://msdn.microsoft.com/en-us/library/aa772300.aspx. newValue accepts boolean values

# sid
# Get the SID of the Active Directory object

# type
# pyAD object type (user, computer, group, organizationalUnit, domain).

# update_attribute(attribute, newvalue, no_flush=False)[source]
# Updates any mutable LDAP attribute for the object. If you are adding or removing values from a multi-valued attribute, see append_to_attribute and remove_from_attribute.

# update_attributes(attribute_value_dict)[source]
# Updates multiple attributes in a single transaction attribute_value_dict should contain a dictionary of values keyed by attribute name

# ADUser
# class pyad.aduser.ADUser(distinguished_name=None, adsi_ldap_com_object=None, options={})[source]
# classmethod create(name, container_object, password=None, upn_suffix=None, enable=True, optional_attributes={})[source]
# Creates and returns a new active directory user

# force_pwd_change_on_login()[source]
# Forces the user to change their password the next time they login

# get_password_last_set()[source]
# Returns datetime object of when user last reset their password.

# set_expiration(dt)[source]
# Sets the expiration date of the password to the given value

# set_password(password)[source]
# Sets the users password

# ADComputer
# class pyad.adcomputer.ADComputer(distinguished_name=None, adsi_ldap_com_object=None, options={})[source]
# Python class representing a computer object in Active Directory.

# classmethod create(name, container_object, enable=True, optional_attributes={})[source]
# Creates and returns a new computer object.

# get_creator()[source]
# returns ADUser object of the user who added the computer to the domain. Returns None if user no longer exists.

# ADGroup
# class pyad.adgroup.ADGroup(distinguished_name=None, adsi_ldap_com_object=None, options={})[source]
# add_members(members)[source]
# Accepts a list of pyAD objects or a single pyAD object and adds as members to the group.

# check_contains_member(check_member, recursive=False)[source]
# Checks whether a pyAD object is a member of the group. check_member expects a pyAD object to be checked. recursive expects True/False which determines whether the group membership will be searched recursively.

# classmethod create(name, container_object, security_enabled=True, scope='GLOBAL', optional_attributes={})[source]
# Creates and returns a new group

# get_group_scope()[source]
# Returns the group scope GLOBAL, UNIVERSAL, or LOCAL.

# get_group_type()[source]
# Returns group type DISTRIBUTION or SECURITY.

# get_members(recursive=False, ignoreGroups=False)[source]
# Returns a list of group members. recursive - True/False. Determines whether to recursively traverse through nested groups. ignoreGroups - True/False. Determines whether or not to return an ADGroup objects in list or to ignore them.

# remove_all_members()[source]
# Removes all members of the group.

# remove_members(members)[source]
# Accepts a list of pyAD objects or a single pyAD object and removes these as members from the group.

# set_group_scope(new_scope)[source]
# Sets group scope. new_scope expects GLOBAL, UNIVERSAL, or LOCAL.

# set_group_type(new_type)[source]
# Sets group type. new_type expects DISTRIBUTION or SECURITY.

# sync_membership(new_population)[source]
# Synchronizes membership of group so that it matches the list of entries in new_population

# ADContainer
# class pyad.adcontainer.ADContainer(distinguished_name=None, adsi_ldap_com_object=None, options={})[source]
# create_computer(name, enable=True, optional_attributes={})[source]
# Create a new computer object in the container

# create_container(name, optional_attributes={})[source]
# Create a new organizational unit in the container

# create_group(name, security_enabled=True, scope='GLOBAL', optional_attributes={})[source]
# Create a new group object in the container

# create_user(name, password=None, upn_suffix=None, enable=True, optional_attributes={})[source]
# Create a new user object in the container

# get_children(recursive=False, filter_=None)[source]
# Iterate over the children objects in the container.

# remove_child(child)[source]
# Rremoves the child object from the domain

# ADDomain
# NOTE: ADDomain subclasses ADContainer.

# class pyad.addomain.ADDomain(distinguished_name=None, adsi_ldap_com_object=None, options={})[source]
# get_default_upn()[source]
# Returns the default userPrincipalName for the domain.
