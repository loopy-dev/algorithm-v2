def record_nickname(record):
    id_dict = {}
    for l in record:
        log = l.split(" ")
        if log[0] == "Enter" or log[0] == "Change":
            uid = log[1]
            nickname = log[2]
            id_dict[uid] = nickname
    return id_dict


def log_message(ids, record):
    messages = []
    for l in record:
        log = l.split(" ")

        if log[0] == "Change":
            continue

        uid = log[1]
        message = [f"{ids[uid]}님이"]

        if log[0] == "Enter":
            message.append("들어왔습니다.")
        elif log[0] == "Leave":
            message.append("나갔습니다.")

        messages.append(" ".join(message))
    return messages


def solution(record):
    id_dict = record_nickname(record)
    return log_message(id_dict, record)


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]

print(solution(record))
