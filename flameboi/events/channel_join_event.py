from flameboi.common.IEvent import Event

class ChannelJoin(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self):
        pass
    
    # event = payload.get("event", {})

    # user_id = event.get("user")
    # channel_id = event.get("channel")
    
    # logger.info("Responding to member joined event")

    # name = theBot.get_user_info(user_id)
    # text = ":tada: Welcome to channel, %s!!! :tada:" % name['user']['real_name']
    
    # assert theBot.send_message(channel_id, text)["ok"]