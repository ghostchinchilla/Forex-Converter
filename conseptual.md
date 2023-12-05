### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is used for backend development (server side). Javascript can be used for both frontend (client side) and backend.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
You can use if-else condition to check if the key is present or not. Or, you could use a try-except block to check whether the key is present or not.

- What is a unit test?
  Testing individual units or components of code to ensure their proper functioning.

- What is an integration test?
Splits the code up into blocks consisting of a number of units so that parts of the software can be checked progressively before they are joined together to become a whole system.

- What is the role of web application framework, like Flask?
Flask is desgned to enable developers to create and scale web apps quickly and simply.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from the query string using Flask?
You can pass the value as part of the query string, and get it from the request.

- How do you collect data from the body of the request using Flask?
You could us request.args.get('name'), or you can use the jsonify() function.

- What is a cookie and what kinds of things are they commonly used for?
Cookies are small files of information that a web server generates and sends to a web browser.They help that website remember information about your visit.

- What is the session object in Flask?
session object works like a dictionary but it can also keep track modifications. When we use sessions the data is stored in the browser as a cookie.

- What does Flask's `jsonify()` do?
jsonify() function returns a Response object.