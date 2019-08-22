# <-- EXPAND to see the data classes
import fileinput
import math


class Message:
    def __init__(self, sender, recipient, conversation_id):
        self.sender = sender
        self.recipient = recipient
        self.conversation_id = conversation_id


"""
    Sample Input:
        biz_owner_id: 42
        all_messages: [
            {"sender": 1,  "recipient": 42, "conversation_id": 1},
            {"sender": 42, "recipient": 1,  "conversation_id": 1},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 3,  "recipient": 88, "conversation_id": 3},
            {"sender": 3,  "recipient": 42, "conversation_id": 4},
        ]

    Sample Output:
        33 (Business owner 42 received three conversations total (1, 2, and 4), but only
        responded to one conversation (conversation ID 1)).
"""


def business_responsiveness_rate(biz_owner_id, all_messages):
    owner_response, total_conversations = [], []
    for message in range(len(all_messages)):
        if all_messages[message]["sender"] == biz_owner_id:
            owner_response.append(all_messages[message]["conversation_id"])
        if all_messages[message]["recipient"] == biz_owner_id:
            total_conversations.append(
                all_messages[message]["conversation_id"])
    return math.floor(len(set(owner_response))/len(set(total_conversations)) * 100)


if __name__ == '__main__':

    # lines = list(fileinput.input())
    # biz_owner_id = lines[0].rstrip()

    # all_messages = []
    # for line in lines[1:]:
    #     if not line:
    #         break
    #     sender, recipient, conversation_id = line.split(' ')
    #     all_messages.append(
    #         Message(
    #             sender,
    #             recipient,
    #             conversation_id.rstrip(),
    #         ),
    #     )

    biz_owner_id = 42
    all_messages = [
        {"sender": 1,  "recipient": 42, "conversation_id": 1},
        {"sender": 42, "recipient": 1,  "conversation_id": 1},
        {"sender": 2,  "recipient": 42, "conversation_id": 2},
        {"sender": 2,  "recipient": 42, "conversation_id": 2},
        {"sender": 3,  "recipient": 88, "conversation_id": 3},
        {"sender": 3,  "recipient": 42, "conversation_id": 4},
    ]

    print(business_responsiveness_rate(biz_owner_id, all_messages))
