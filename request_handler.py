import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from entries import get_all_entries, get_single_entry, delete_entry



# Here's a class. It inherits from another class.


class HandleRequests(BaseHTTPRequestHandler):

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
            # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'email'
            value = pair[1]  # 'jenna@solis.com'

            return ( resource, key, value )

        # No query string parameter
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)

    def do_GET(self):
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

    #     # Response from parse_url() is a tuple with 2
    #     # items in it, which means the request was for
    #     # `/animals` or `/animals/2`
        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "entries":
                if id is not None:
                    response = f"{get_single_entry(id)}"
                else:
                    response = f"{get_all_entries()}"
    #         elif resource == "customers":
    #             if id is not None:
    #                 response = f"{get_single_customer(id)}"
    #             else:
    #                 response = f"{get_all_customers()}"
    #         elif resource == "employees":
    #             if id is not None:
    #                 response = f"{get_single_employee(id)}"
    #             else:
    #                 response = f"{get_all_employees()}"
    #         elif resource == "locations":
    #             if id is not None:
    #                 response = f"{get_single_location(id)}"
    #             else:
    #                 response = f"{get_all_locations()}"


        # # Response from parse_url() is a tuple with 3
        # # items in it, which means the request was for
        # # `/resource?parameter=value`
        # elif len(parsed) == 3:
        #     ( resource, key, value ) = parsed

        #     # Is the resource `customers` and was there a
        #     # query parameter that specified the customer
        #     # email as a filtering value?
        #     if key == "email" and resource == "customers":
        #         response = get_customer_by_email(value)
        #     if key == "location_id" and resource == "animals":
        #         response = get_animal_by_location(value)
        #     if key == "location_id" and resource == "employees":
        #         response = get_employee_by_location(value)
        #     if key == "status" and resource == "animals":
        #         response = get_animal_by_status(value)

        self.wfile.write(response.encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.

    # def do_POST(self):
    #     self._set_headers(201)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)

    #     # Convert JSON string to a Python dictionary
    #     post_body = json.loads(post_body)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Initialize new animal
    #     new_resource = None

    #     # Add a new animal to the list. Don't worry about
    #     # the orange squiggle, you'll define the create_animal
    #     # function next.
    #     if resource == "animals":
    #         new_resource = create_animal(post_body)

    #     if resource == "locations":
    #         new_resource = create_location(post_body)

    #     if resource == "employees":
    #         new_resource = create_employee(post_body)

    #     # Encode the new animal and send in response
    #     self.wfile.write(f"{new_resource}".encode())

    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

    #     # Delete a single entry from the list
        if resource == "entries":
            delete_entry(id)

    #     if resource == "locations":
    #         delete_location(id)

    #     if resource == "employees":
    #         delete_employee(id)
        
    #     if resource == "customers":
    #         delete_customer(id)

    #     # Encode the new entry and send in response
        self.wfile.write("".encode())

    # def do_PUT(self):
    #     self._set_headers(204)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)
    #     post_body = json.loads(post_body)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Delete a single animal from the list
    #     if resource == "animals":
    #         update_animal(id, post_body)

    #     if resource == "locations":
    #         update_location(id, post_body)

    #     if resource == "customers":
    #         update_customer(id, post_body)

    #     if resource == "employees":
    #         update_employee(id, post_body)

    #     # Encode the new animal and send in response
    #     self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()