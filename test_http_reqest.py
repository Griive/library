import requests as r
req = r.post(
    url='http://127.0.0.1:5000/add-book',
    data={
        'bookYear': '2020',
        'bookAuthor': 'ozozo',
        'bookName': 'xacs',
    })
print(req.text)
# req2 = r.get(
#     url='http://127.0.0.1:5000/add-book',
#     )
# print(req2.text)