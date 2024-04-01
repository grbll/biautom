import json
from jsonschema import RefResolver, Draft202012Validator

address="""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/schemas/address",
  "type": "object",
  "properties": {
    "test1": {
      "type": "string"
    },
    "test2": {
      "type": "string"
    }
  },
  "required": [
    "test1"
  ]
}
"""

customer="""
{
  "$id": "https://example.com/schemas/customer",
  "type": "object",
  "properties": {
    "first_name": { "type": "string" },
    "last_name": { "type": "string" },
    "shipping_address": { "$ref": "/schemas/address" },
    "billing_address": { "$ref": "/schemas/address" }
  },
  "required": ["first_name", "last_name", "shipping_address", "billing_address"],
  "additionalProperties": false
}
"""

data = """
{
  "first_name": "John",
  "last_name": "Doe",
  "shipping_address": {
    "street_address": "1600 Pennsylvania Avenue NW",
    "city": "Washington",
    "state": "DC"
  },
  "billing_address": {
    "street_address": "1st Street SE",
    "city": "Washington"
  }
}
"""

address_schema = json.loads(address)
customer_schema = json.loads(customer)
schema_store = {
    address_schema['$id'] : address_schema,
    customer_schema['$id'] : customer_schema,
}

resolver = RefResolver.from_schema(customer_schema, store=schema_store)
validator = Draft202012Validator(customer_schema, resolver=resolver)

jsonData = json.loads(data)
validator.validate(jsonData)
