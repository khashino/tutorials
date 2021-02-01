#1) COLLECTION_EXISTS Function
Use this function to determine if a collection exists. A TRUE is returned if the specified collection exists for the current user in the current session for the current Application ID, otherwise FALSE is returned.

Syntax
```
APEX_COLLECTION.COLLECTION_EXISTS (
    p_collection_name IN VARCHAR2)
RETURN BOOLEAN;
```
Parameters
describes the parameters available in the COLLECTION_EXISTS function.

Parameter	Description
p_collection_name

The name of the collection. Maximum length is 255 bytes. The collection name is not case sensitive and is converted to upper case.


####Example
The following example shows how to use the COLLECTION_EXISTS function to determine if the collection named CART exists.
```
Begin
    l_exists := APEX_COLLECTION.COLLECTION_EXISTS (
        p_collection_name => 'CART';
End;
```


#2) CREATE_COLLECTION Procedure
Use this procedure to create an empty collection that does not already exist. If a collection exists with the same name for the current user in the same session for the current Application ID, an application error is raised.

Syntax
APEX_COLLECTION.CREATE_COLLECTION(
    p_collection_name IN VARCHAR2);
Parameters
Describes the parameters available in the CREATE_COLLECTION procedure.

Parameter	Description
p_collection_name

The name of the collection. The maximum length is 255 characters. An error is returned if this collection exists with the specified name of the current user and in the same session.


####Example
```
This example shows how to use the CREATE_COLLECTION procedure to create an empty collection named CART.

Begin
    APEX_COLLECTION.CREATE_COLLECTION(
        p_collection_name => 'CART');
End;
```


ADD_MEMBERS Procedure
Use this procedure to add an array of members to a collection. An error is raised if the specified collection does not exist for the current user in the same session for the current Application ID. Gaps are not used when adding a new member, so an existing collection with members of sequence IDs (1,2,5,8) adds the new member with a sequence ID of 9. The count of elements in the p_c001 PL/SQL table is used as the total number of items across all PL/SQL tables. For example, if p_c001.count is 2 and p_c002.count is 10, only 2 members are added. If p_c001 is null an application error is raised.

Syntax
```
APEX_COLLECTION.ADD_MEMBERS (
    p_collection_name IN VARCHAR2,
    p_c001 IN APEX_APPLICATION_GLOBAL.VC_ARR2 default empty_vc_arr,
    p_c002 IN APEX_APPLICATION_GLOBAL.VC_ARR2 default empty_vc_arr,
    p_c003 IN APEX_APPLICATION_GLOBAL.VC_ARR2 default empty_vc_arr,
    ...
    p_c050 IN APEX_APPLICATION_GLOBAL.VC_ARR2 default empty_vc_arr,
    p_n001 IN APEX_APPLICATION_GLOBAL.N_ARR default empty_n_arr,
    p_n002 IN APEX_APPLICATION_GLOBAL.N_ARR default empty_n_arr,
    p_n003 IN APEX_APPLICATION_GLOBAL.N_ARR default empty_n_arr,
    p_n004 IN APEX_APPLICATION_GLOBAL.N_ARR default empty_n_arr,
    p_n005 IN APEX_APPLICATION_GLOBAL.N_ARR default empty_n_arr,
    p_d001 IN APEX_APPLICATION_GLOBAL.D_ARR default empty_d_arr,
    p_d002 IN APEX_APPLICATION_GLOBAL.D_ARR default empty_d_arr,
    p_d003 IN APEX_APPLICATION_GLOBAL.D_ARR default empty_d_arr,
    p_d004 IN APEX_APPLICATION_GLOBAL.D_ARR default empty_d_arr,
    p_d005 IN APEX_APPLICATION_GLOBAL.D_ARR default empty_d_arr,
    p_generate_md5 IN VARCHAR2 default 'NO');
    ```
##Parameters

Describes the parameters available in the ADD_MEMBERS procedure.

###Note:
```
Any character attribute exceeding 4,000 characters is truncated to 4,000 characters. Also, the number of members added is based on the number of elements in the first array.
Parameter	Description
p_collection_name

The name of an existing collection. Maximum length is 255 bytes. Collection names are not case sensitive and are converted to upper case.

p_c001 through p_c050

Array of character attribute values to be added.

p_n001 through p_n005

Array of numeric attribute values to be added.

p_d001 through p_d005

Array of date attribute values to be added.

p_generate_md5

Valid values include YES and NO. YES to specify if the message digest of the data of the collection member should be computed. Use this parameter to compare the MD5 of the collection member with another member or to see if that member has changed.
```
###Example
The following example shows how to add two new members to the CART table.
```
Begin
    APEX_COLLECTION.ADD_MEMBERS(
        p_collection_name => 'CART',
        p_c001 => l_arr1,
        p_c002 => 1_arr2);
End;
```
