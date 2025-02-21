# Basics of HTTP/HTTPS

## 1 - Differentiating HTTP and HTTPS:

HTTP (HyperText Transfer Protocol)  transfers data between a web browser and a server in plain text, so everyone can read user's information. HTTPS (HyperText Transfer Protocol Secure) is similar with http but the data's are encrypted, that make the informations remains unreadable to a human. It's crucial to protecting user's information.

## 2 - Depiction of the structure of an HTTP request and response

#### HTTP Request Structure:
* Request line : Give the HTTP method/HTTP version and the URL
* Headers : Give additional information like the host, the user-agent etc..
* Body : It's used in differents method to send data

#### HTTP Response Struture:
* Statut line : HTTP version, status code and status message
* Headers : Give metadata about the response
* Body : The actual content of the response like the html

## 3 - Some common HTTP methods

* GET :  
    * Description : get data from a server
    * Use Case (example) :  get a web page or data from an API

* DELETE :  
    * Description: remove a ressource from the server
    * Use Case (example) : removing a user account or comment

* POST :  
    * Description: send data to a server to create a resource
    * Use Case (example) : uploading a file

* PUT :  (similar to post)
    * Description: update an existing resource or create a new resource if it doesn't exist
    * Use Case (example) : updating user information

## 3 - Some HTTP status codes

### There are 5 type of status code :

* 1xx who are informational
* 2xx means a success request
* 3xx for a redirection
* 4xx are for clients errors
* 5xx for the servers errors

### Some exemple of statut codes and their use cases : 

* **200 OK (success)** - Request successful

* **201 Created (success)** - New ressource created

* **301 Moved Permanently (the requested resource has been permanently moved to a new URL)** - Redirecting old URL's to a new website

* **403 Forbidden (the server denies access to the resource)** - User doesn't have access to the data

* **404 Not found (the server cannot find the requested resource)** - Requested data doesn't exist

* **500 Internal Server Error (a generic server-side error)** - crashes due to an application bug

* **502 Bad Gateway (invalid response from an upstream server)** - Invalid response of a server from an another server