import srview.utils.dict as ud

PRIMITIVE_TYPES = {'null', 'boolean', 'int', 'long', 'float', 'double', 'bytes', 'string'}

def schema_type(schema):
    """Infer type from schema."""
    schematype = type(schema)
    if schematype == str:
        if schema in PRIMITIVE_TYPES:
            return "primitive"
        else:
            return "defined"
    elif schematype != dict:
        raise ValueError("Avro should yield strings / objects, got {0} of type {1}".format(schema, schematype))
    else:
        return schema['type']

def schema_name(schema):
    if ud.has_keys(schema, 'name', 'namespace'):
        return "{0}/{1}".format(schema['namespace'], schema['name'])
    elif 'name' in schema:
        return schema['name']
    else:
        return schema_type(schema)