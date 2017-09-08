import operator
class call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display(self):
        print "unique id is:",self.unique_id
        print "caller name is:",self.caller_name
        print "caller phone number is:",self.caller_phone_number
        print "The time of call is",self.time_of_call,'minutes.'
        print "The reason for call is",self.reason_for_call
        print '*' * 100
        return self

class callCenter(object):

    def __init__(self):

        self.calls_dict = []
        self.call_list_size = len(self.calls_dict)

    def remove_the_first_call_in_calling_list(self):
        if len(self.calls_dict) is 0:
            return self
        else:
                del self.calls_dict[0]
                return self

    def add_to_call_list_dict(self, name, number, time):
        key = ['Name', 'Phone number', 'Duration time']
        caller = [name,number,time]
        self.calls_dict.append(dict(zip(key, caller)))
        self.calls_dict.sort(key = operator.itemgetter('Duration time'))
        return self

    def remove_the_number_by_name(self,name):
        for index in range(0, len(self.calls_dict)):
            if name is self.calls_dict[index].get('Name'):
                self.calls_dict.pop(index)
                return self

    def remove_the_number_by_number(self,number):
        for index in range(0, len(self.calls_dict)):
            if number is self.calls_dict[index].get('Phone number'):
                self.calls_dict.pop(index)
                return self

    def display_call_list(self):
        for item in self.calls_dict:
            print item
        return self


def caller_input(unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):    # handle the caller information
    caller = call(unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call)
    # caller.display()

    callCenterStore.add_to_call_list_dict(caller_name, caller_phone_number, time_of_call)

callCenterStore = callCenter()

caller_input("President", "Donald Trump0", "999-999-9999", 30, "for asked")
caller_input("President", "Donald Trump1", "888-999-9999", 20, "for asked")
caller_input("President", "Donald Trump2", "777-999-9999", 10, "for asked")
caller_input("President", "Donald Trump3", "666-999-9999", 40, "for asked")
caller_input("President", "Donald Trump4", "555-999-9999", 90, "for asked")
caller_input("President", "Donald Trump5", "444-999-9999", 80, "for asked")
caller_input("President", "Donald Trump6", "333-999-9999", 70, "for asked")
caller_input("President", "Donald Trump7", "222-999-9999", 60, "for asked")

callCenterStore.display_call_list()
print '*' * 100
callCenterStore.remove_the_first_call_in_calling_list()
callCenterStore.remove_the_number_by_name('Donald Trump7')
callCenterStore.remove_the_number_by_number('333-999-9999')
callCenterStore.display_call_list()


