def require_role(required_roles):
    def checker(token_data):
        if token_data.role not in required_roles:
            raise Exception("Insufficient permissions")
    return checker