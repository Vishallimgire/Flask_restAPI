from flask import Flask, jsonify, request
app = Flask(__name__)


stores = [
    {
        'name':'mystore',
        'items':[
            {
                'name': 'myitem',
                'price':15.99
            }
        ]
    }
]
# create store with post requests
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    data = {
        'name': request_data['name'],
        'items':[]
    }
    stores.append(data)
    return jsonify(data)

#Get a /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})
    

# get all stores
@app.route('/store')
def get_stores():
     return jsonify(stores)

#post a /store/<string:name>/item
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_store_by_name(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_data = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_data)
            return jsonify(new_data)
    return jsonify({'message':'no data found'})


#get a /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_store_by_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'messge':'items not found'})

app.run(port=4000, debug=True)