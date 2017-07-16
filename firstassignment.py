def nowtime():
    import datetime
    now = datetime.datetime.now()
    print()
    print ("Current date and time using datetime object")
    return now
print(nowtime())
