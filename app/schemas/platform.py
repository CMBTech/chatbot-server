from marshmallow import Schema, fields, validate, pre_load


class PlatformSchema(Schema):

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, error_message={
        "required": "name is required"},
        validate=[
            validate.Regexp(
                regex=r'^(?!\s*$)', error='name should be a valid string'
            ),
        ])
    url = fields.String()
    status_date = fields.String()
    category_id = fields.Integer()
    status = fields.Bool()
    report_id = fields.String()
    menu_value = fields.Integer()
