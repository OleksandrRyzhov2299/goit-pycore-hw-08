import os
import pickle

from address_book import AddressBook


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            data = pickle.load(file)
        return data
    return {"contacts": AddressBook()}


def save_data(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
