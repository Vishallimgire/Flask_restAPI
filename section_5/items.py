import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
            'price',
            type=float,
            required=True,
            help='This field cannot be blank'
        )

    @jwt_required()
    def get(self, name):
        items = self.item_by_name(name)
        if items:
            return items
        return {'message':'item is not found'}, 404

    @classmethod
    def item_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM items where name=?'
        result = cursor.execute(query, (name,))
        print('result___',result)
        row = result.fetchone()
        print('row___', row)
        connection.close()
        if row:
            return {'item':{'name':row[0], 'price':row[1]}}
    
    @classmethod
    def add_item(cls, name, price):
        print(name, price)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'INSERT INTO items VALUES (?, ?)'
        cursor.execute(query, (name, price))
        connection.commit()
        connection.close()
    
    def post(self, name):
        try:
            print(name)
            items = self.item_by_name(name)
            print('items___',items)
            if items:
                return {'message': f'Item has already exists with {name} name'}, 400
            data = self.parser.parse_args()
            item = {
                'name':name,
                'price': data['price']
            }
            print(item)
            self.add_item(**item)
        except:
            return {'message':'Error occured'}, 500
        else:
            return item, 201

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'DELETE FROM items WHERE name=?'
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'items deleted'}
    
    @classmethod
    def update_item(cls, name, price):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'UPDATE items SET price=? WHERE name=?'
        cursor.execute(query, (price, name))
        connection.commit()
        connection.close()

    def put(self, name):
        items = self.item_by_name(name)
        print(items)
        data = Item.parser.parse_args()
        print('data____', data)
        item = {
                'name':name,
                'price': data['price']
                }
        if items is None:
            try:
                self.add_item(**item)
            except:
                return {'message':'Error occur during inserstion'}, 500
        else:
            try:
                self.update_item(**item)
            except:
                return {'message': 'Error occured during updation'}, 500
        return item

class ItemList(Resource):
    def get(self):
        try:
            items = self.all_items()
        except:
            return {'message':'Error occure in getting items'}, 500
        return {'items':items}


    @classmethod
    def all_items(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM items'
        results = cursor.execute(query)
        items = []
        for result in results:
            items.append({'name':result[0], 'price':result[1]})
        connection.close()
        return items

