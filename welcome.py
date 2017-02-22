# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

book_info = [
    {
        'b_id': 1,
        'category':1,
        'name': 'spindle',
        'price': 450, 
        'quantity':10
    },
    {
        'b_id': 2,
        'category':1,
        'name':'Lost Girl',
        'price': 350, 
        'quantity':20
    },
    {
        'b_id': 3,
        'category':1,
        'name':  'Black Moon',
        'price': 400, 
        'quantity':30
    },
    {
        'b_id': 4,
        'category':2,
        'name':  'my life',
        'price': 300, 
        'quantity':10
    },
    {
        'b_id': 5,
        'category':2,
        'name':  'Victoria the queen',
        'price': 600, 
        'quantity':10
    },
    {
        'b_id': 6,
        'category':2,
        'name': 'philosopher stone',
        'price': 390, 
        'quantity':2
    }
    
]

@app.route('/bookkart/book_info', methods=['GET'])
def get_bookinfo():
    return jsonify({'book_details': book_info})

@app.route('/bookkart/book_info/<int:category>', methods=['GET'])
def get_bookinfo_category(category):
    books = [i for i in book_info if i['category'] == category]
    if len(books) == 0:
        abort(404)
    return jsonify({'books': books})
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
