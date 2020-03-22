from tinydb import TinyDB
from tinydb import where


def download_id(db_entry):
    print(db_entry["id"])
    print(db_entry.doc_id)

    db.update({"status": "done"}, doc_ids=[db_entry.doc_id])


    return




if __name__ == "__main__":

    db = TinyDB('db.json')

    db.insert({'id': "adasdasdasd", "status": "added"})

    added_stuff = db.search(where('status') == 'added')

    for s in added_stuff:
        download_id(s)

