def response_json(target):
    def decorator(*args, **kwargs):
        response = target(*args, **kwargs)

        # TODO: you can add your error handling in here
        return response.json()

    return decorator
