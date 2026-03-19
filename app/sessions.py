sessions = {}

def create_session(user):
    sessions[user] = {
        "requests": 0
    }

def update_session(user):

    if user not in sessions:
        create_session(user)

    sessions[user]["requests"] += 1

def get_session(user):
    return sessions.get(user, {})