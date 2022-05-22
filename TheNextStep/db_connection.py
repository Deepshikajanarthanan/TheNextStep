import pymongo

def get_data_from_db(email,Password):
    print("In DB Connection")
    DEFAULT_CONNECTION_URL = "mongodb+srv://admin:admin@thenextstep.ynldq.mongodb.net/test"
    # Establish a connection with mongoDB
    client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
    my_db = client["TheNextStep"]
    my_collection = my_db["user"]
    query = {"email":email,"password":Password}
    data = my_collection.find_one(query)
    print(data)
    if data == None:
        return("Invalid Username or Password")
    else:
        return("Successfully Logged In")

def signup_connection(fullName,email,password,confirmPassword):
    print("In DB Connection")
    DEFAULT_CONNECTION_URL = "mongodb+srv://admin:admin@thenextstep.ynldq.mongodb.net/test"
    # Establish a connection with mongoDB
    client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
    my_db = client["TheNextStep"]
    my_collection = my_db["user"]
    query = {'email':email}
    data = my_collection.find_one(query)
    if data == None:
        my_collection.insert_one({'fullName':fullName,'email':email,'password':password,'confirmPassword':confirmPassword})
        return ("Successfully Signed Up")
    else:
        return ("Email Id already registered")

def get_recommendation(streamName):
    print("In DB Connection")
    DEFAULT_CONNECTION_URL = "mongodb+srv://admin:admin@thenextstep.ynldq.mongodb.net/test"
    # Establish a connection with mongoDB
    client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
    my_db = client["TheNextStep"]
    my_collection = my_db["recommendation"]
    query = {'streamName': streamName}
    data = my_collection.find_one(query)
    return data

def get_stream_info(streamName):
    print("In DB Connection")
    DEFAULT_CONNECTION_URL = "mongodb+srv://admin:admin@thenextstep.ynldq.mongodb.net/test"
    # Establish a connection with mongoDB
    client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
    my_db = client["TheNextStep"]
    my_collection = my_db["googleResponse"]
    query = {"What type of course or subject you are interested in (Area of Interest)":streamName}
    data = my_collection.count_documents(query)
    return data

def dump_data_to_db(data):
    print("In DB Connection")
    DEFAULT_CONNECTION_URL = "mongodb+srv://admin:admin@thenextstep.ynldq.mongodb.net/test"
    # Establish a connection with mongoDB
    client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
    my_db = client["TheNextStep"]
    my_collection = my_db["googleResponse"]
    my_collection.insert_one(data)
    return "Successfully inserted"
