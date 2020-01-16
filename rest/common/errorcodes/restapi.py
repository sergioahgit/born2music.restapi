#!/usr/bin/env python3.7

# The MIT License (MIT)
#
# Copyright (c) 2019-2020 Sergio A. Hernandez, Jr.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name(s) of the above copyright holders shall not be used in
# advertising or otherwise to promote the sale, use or other dealings in this Software without prior
# written authorization.

"""
Descriptive Common REST API error codes, for code readability.

See RFC 2616 - https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
And RFC 6585 - https://tools.ietf.org/html/rfc6585
And RFC 4918 - https://tools.ietf.org/html/rfc4918
And Microsoft - https://docs.microsoft.com/en-us/rest/api/storageservices/common-rest-api-error-codes

"""
HTTP_UNDEFINED_STATUS_CODE = 0
HTTP_INFORMATIONAL_CODE = 1
HTTP_SUCCESS_CODE = 2
HTTP_REDIRECT_CODE = 3
HTTP_CLIENT_ERROR_CODE = 4
HTTP_SERVER_ERROR_CODE = 5

# Returns HTTP_UNDEFINED_STATUS_CODE if code is not defined
# Returns HTTP_INFORMATIONAL_CODE for error codes within the 100 - 199 range are informational codes.
# Returns HTTP_SUCCESS_CODE for error codes within the 200 - 299 range are defined as success codes.
# Returns HTTP_REDIRECT_CODE for error codes within the 300 - 399 range are redirectional error codes.
# Returns HTTP_CLIENT_ERROR_CODE for error codes within the 400 - 499 range are client side error codes.
# Returns HTTP_CLIENT_ERROR_CODE for error codes within the 500 - 599 range are server side error codes.
def getStatusCodeType( code ):

    # Error codes within the 100 - 199 range are informational codes.
    # Returns HTTP_INFORMATIONAL_CODE if code within range.  Otherwise, HTTP_UNDEFINED_STATUS_CODE.
    if 100 <= code <= 199:
        return 1;

    # Error codes within the 200 - 299 range are defined as success codes.
    # Returns HTTP_SUCCESS_CODE if code within range.  Otherwise, HTTP_UNDEFINED_STATUS_CODE.
    if 200 <= code <= 299:
        return 2;

    # Error codes within the 300 - 399 range are redirectional error codes.
    # Returns HTTP_REDIRECT_CODE if code within range.  Otherwise, HTTP_UNDEFINED_STATUS_CODE.
    if 300 <= code <= 399:
        return 3;

    # Error codes within the 400 - 499 range are client side error codes.
    # Returns HTTP_CLIENT_ERROR_CODE if code within range.  Otherwise, HTTP_UNDEFINED_STATUS_CODE.
    if 400 <= code <= 499:
        return HTTP_CLIENT_ERROR_CODE;

    # Error codes within the 500 - 599 range are server side error codes.
    # Returns HTTP_SERVER_ERROR_CODE if code within range.  Otherwise, HTTP_UNDEFINED_STATUS_CODE.
    if 500 <= code <= 599:
        return HTTP_SERVER_ERROR_CODE;

    return HTTP_UNDEFINED_STATUS_CODE

HTTP_304_NOT_MODIFIED_CODE = 304
HTTP_304_NOT_MODIFIED_MSG_CONDITION_NOT_MET = "The condition specified in the conditional header(s) was not met for read operation."

HTTP_400_BAD_REQUEST_CODE = 400
HTTP_400_BAD_REQUEST_MSG_MALFORMED_DATA = "Data in the body is malformed."
HTTP_400_BAD_REQUEST_MSG_CONDITION_HEADERS_NOT_SUPPORTED = "Condition headers are not supported."
HTTP_400_BAD_REQUEST_MSG_EMPTY_METADATA_KEY = "The key for one of the metadata key-value pairs is empty."
HTTP_400_BAD_REQUEST_MSG_INVALID_AUTHENTICATION_INFO = "The authentication was not provied in the correct format.  Verify the value of 'Authorization' header."
HTTP_400_BAD_REQUEST_MSG_INVALID_HEADER_VALUE = "The value provided for one of the HTTP headers was not in the correct format."
HTTP_400_BAD_REQUEST_MSG_INVALID_HTTP_VERB = "The HTTP verb specified was not recognized by the server."
HTTP_400_BAD_REQUEST_MSG_INVALID_INPUT = "One of the request inputs is not valid."
HTTP_400_BAD_REQUEST_MSG_INVALID_MD5 = "The MD5 value specified in the request is invalid.  The MD5 value must be 128 bits and Base64-encoded."
HTTP_400_BAD_REQUEST_MSG_INVALID_METADATA = "The specified metadata is invalid.  It includes characters that are not permitted."
HTTP_400_BAD_REQUEST_MSG_INVALID_QUERY_PARAMETER_VALUE = "An invalid value was specified for one of the query parameters in the request URI."
HTTP_400_BAD_REQUEST_MSG_INVALID_RESOURCE_NAME = "The specified resource name contains invalid characters."
HTTP_400_BAD_REQUEST_MSG_INVALID_URI = "The requested URI does not represent any resource on the server."
HTTP_400_BAD_REQUEST_MSG_INVALID_XML_DOCUMENT = "The specified XML is not syntactically valid."
HTTP_400_BAD_REQUEST_MSG_INVALID_XML_NODE_VALUE = "The value provided for one of the XML nodes in the request body was not in the correct format."
HTTP_400_BAD_REQUEST_MSG_MD5_MISMATCH = "The MD5 value specified in the request did not match the MD5 value calculated by the server."
HTTP_400_BAD_REQUEST_MSG_METADATA_TOO_LARGE = "The size of the specified metadata exceeds the maximum size permitted."
HTTP_400_BAD_REQUEST_MSG_MISSING_REQUIRED_QUERY_PARAMETER = "A required query parameter was not specified for this request."
HTTP_400_BAD_REQUEST_MSG_MISSING_REQUIRED_HEADER = "A required HTTP header was not specified."
HTTP_400_BAD_REQUEST_MSG_MISSING_REQUIRED_XML_NODE = "A required XML node was not specified in the request body."
HTTP_400_BAD_REQUEST_MSG_MULTIPLE_CONDITION_HEADERS_NOT_SUPPORTED = "Multiple condition headers are not supported."
HTTP_400_BAD_REQUEST_MSG_OUT_OF_RANGE_INPUT = "One of the request inputs is out of range."
HTTP_400_BAD_REQUEST_MSG_OUT_OF_RANGE_QUERY_PARAMETER_VALUE = "A query parameter specified in the request URI is outside the permissible range."
HTTP_400_BAD_REQUEST_MSG_REQUEST_URL_FAILED_TO_PARSE = "The URL in the request could not be parsed."
HTTP_400_BAD_REQUEST_MSG_UNSUPPORTED_HEADER = "One of the HTTP headers specified in the request is not supported."
HTTP_400_BAD_REQUEST_MSG_UNSUPPORTED_XML_NODE = "One of the XML nodes specified in the request body is not supported."
HTTP_400_BAD_REQUEST_MSG_UNSUPPORTED_QUERY_PARAMETER = "One of the query parameters specified in the request URI is not supported."


HTTP_403_FORBIDDEN_CODE = 403
HTTP_403_FORBIDDEN_MSG_ACCOUNT_IS_DISABLED = "The specified account is disabled."
HTTP_403_FORBIDDEN_MSG_AUTHENTICATION_FAILED = "The Server failed to authenticate the request.  Make sure the value of the 'Authorization' header is formed correctly including the signature."
HTTP_403_FORBIDDEN_MSG_INSUFFICIENT_ACCOUNT_PERMISSIONS_FOR_READ = "Read operations are currently disabled."
HTTP_403_FORBIDDEN_MSG_INSUFFICIENT_ACCOUNT_PERMISSIONS_FOR_WRITE = "Write operations are not allowed."
HTTP_403_FORBIDDEN_MSG_INSUFFICIENT_ACCOUNT_PERMISSIONS_FOR_EXECUTE = "The account being accessed does not have sufficient permissions to execute this operation."

HTTP_404_NOT_FOUND_CODE = 404
HTTP_404_NOT_FOUND_MSG_RESOURCE_NOT_FOUND = "The specified resource does not exist."

HTTP_405_METHOD_NOT_ALLOWED_CODE = 405
HTTP_405_METHOD_NOT_ALLOWED_MSG_UNSUPPORTED_HTTP_VERB = "The resource doesn't support the specified HTTP verb."

HTTP_409_CONFLICT_CODE = 409
HTTP_409_CONFLICT_MSG_ACCOUNT_ALREADY_EXIST = "The specified account already exists."
HTTP_409_CONFLICT_MSG_ACCOUNT_BEING_CREATED = "The specified account is in the process of being created."
HTTP_409_CONFLICT_MSG_RESOURCE_TYPE_MISMATCH = "The specified resource type does not match the type of the existing resource."
HTTP_409_CONFLICT_MSG_RESOURCE_ALREADY_EXISTS = "The specified resource already exists."

HTTP_411_LENGTH_REQUIRED_CODE = 411
HTTP_411_LENGTH_REQUIRED_MSG_MISSING_CONTENT_LENGHT_HEADER = "The 'Content-Length' header was not specified."
HTTP_411_LENGTH_REQUIRED_MSG_CONTENT_LENGHT_IS_ZERO = "The 'Content-Length' is zero."

HTTP_412_PRECONDITION_FAILED_CODE = 412
HTTP_412_PRECONDITION_FAILED_MSG_CONDITION_NOT_MET = "The condition specified in the conditional header(s) was not met for a write operation."

HTTP_413_REQUEST_ENTITY_TOO_LARGE_CODE = 413
HTTP_413_REQUEST_ENTITY_TOO_LARGE_MSG_REQUEST_BODY_TOO_LARGE = "The size of the request body exceeds the maximum size permitted."

HTTP_416_REQUEST_RANGE_NOT_SATISFIED_CODE = 416
HTTP_416_REQUEST_RANGE_NOT_SATISFIED_MSG_INVALID_RANGE = "The range specified is invalid for the current size of the resource."

HTTP_500_INTERNAL_SERVER_ERROR_CODE = 500
HTTP_500_INTERNAL_SERVER_ERROR_MSG_INTERNAL_ERROR = "The server encountered an internal error.  Please retry the request."
HTTP_500_INTERNAL_SERVER_ERROR_MSG_OPERATION_TIMED_OUT = "The operation could not be completed within the permitted time."

HTTP_503_SERVICE_UNAVAILABLE_CODE = 503
HTTP_503_SERVICE_UNAVAILABLE_MSG_SERVER_BUSY_UNABLE_TO_RECEIVE_REQUESTS = "The server is currently unable to receive requests.  Please retry your request."
HTTP_503_SERVICE_UNAVAILABLE_MSG_SERVER_BUSY_INGRESS_OVER_ACCOUNT_LIMIT = "Ingress is over the account limit."
HTTP_503_SERVICE_UNAVAILABLE_MSG_SERVER_BUSY_EGRESS_OVER_ACCOUNT_LIMIT = "Egress is over the account limit."
HTTP_503_SERVICE_UNAVAILABLE_MSG_SERVER_BUSY_OPERATIONS_PER_SEC_OVER_ACCOUNT_LIMIT = "Operations per second is over the account limit."