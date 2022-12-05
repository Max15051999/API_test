def resp_json_with_code_400_or_500(message, description):
    return {'status': 'Failure', 'status_details': {'message': message, 'description': description}}

