from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Coreset, coreset_schema, coresets_schema, Wish, wish_schema, wishs_schema
from models import db, Set, set_schema, sets_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'naw'}

# @api.route('/data')
# def viewdata():
#     data = get_contact()
#     response = jsonify(data)
#     print(response)
#     return render_template('index.html', data = data)

@api.route('/coresets', methods = ['POST'])
@token_required
def create_coreset(current_user_token):
    name = request.json['name']
    rarity= request.json['rarity']
    size = request.json['size']
    release_date = request.json['release_date']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    coreset = Coreset(name, rarity, size, release_date, user_token = user_token )

    db.session.add(coreset)
    db.session.commit()

    response = coreset_schema.dump(coreset)
    return jsonify(response)

@api.route('/coresets', methods = ['GET'])
@token_required
def get_coreset(current_user_token):
    a_user = current_user_token.token
    coresets = Coreset.query.filter_by(user_token = a_user).all()
    response = coresets_schema.dump(coresets)
    return jsonify(response)

@api.route('/coresets/<id>', methods = ['GET'])
@token_required
def get_coreset_two(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        coreset = Coreset.query.get(id)
        response = coreset_schema.dump(coreset)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401

# UPDATE endpoint
@api.route('/coresets/<id>', methods = ['POST','PUT'])
@token_required
def update_coreset(current_user_token, id):
    coreset = Coreset.query.get(id) 
    coreset.name = request.json['name']
    coreset.rarity= request.json['rarity']
    coreset.size = request.json['size']
    coreset.release_date = request.json['release_date']
    user_token = current_user_token.token

    db.session.commit()
    response = coreset_schema.dump(coreset)
    return jsonify(response)


# DELETE car ENDPOINT
@api.route('/coresets/<id>', methods = ['DELETE'])
@token_required
def delete_coreset(current_user_token, id):
    coreset = Coreset.query.get(id)
    db.session.delete(coreset)
    db.session.commit()
    response = coreset_schema.dump(coreset)
    return jsonify(response)

# Wish form


@api.route('/wish', methods = ['POST'])
@token_required
def create_wish(current_user_token):
    name = request.json['name']
    rarity= request.json['rarity']
    size = request.json['size']
    release_date = request.json['release_date']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    wish = Wish(name, rarity, size, release_date, user_token = user_token )

    db.session.add(wish)
    db.session.commit()

    response = wish_schema.dump(wish)
    return jsonify(response)

@api.route('/wish', methods = ['GET'])
@token_required
def get_wish(current_user_token):
    a_user = current_user_token.token
    wish = Wish.query.filter_by(user_token = a_user).all()
    response = wishs_schema.dump(wish)
    return jsonify(response)

@api.route('/wish/<id>', methods = ['GET'])
@token_required
def get_wish_two(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        wish = Wish.query.get(id)
        response = wish_schema.dump(wish)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401


@api.route('/wish/<id>', methods = ['POST','PUT'])
@token_required
def update_wish(current_user_token, id):
    wish = Wish.query.get(id) 
    wish.name = request.json['name']
    wish.rarity= request.json['rarity']
    wish.size = request.json['size']
    wish.release_date = request.json['release_date']
    user_token = current_user_token.token

    db.session.commit()
    response = wish_schema.dump(wish)
    return jsonify(response)


@api.route('/wish/<id>', methods = ['DELETE'])
@token_required
def delete_wish(current_user_token, id):
    wish = Wish.query.get(id)
    db.session.delete(Wish)
    db.session.commit()
    response = wish_schema.dump(wish)
    return jsonify(response)

# @api.route('/sets', methods = ['POST'])
# @token_required
# def create_set(current_user_token):
#     name = request.json['name']
#     rarity= request.json['rarity']
#     size = request.json['size']
#     user_token = current_user_token.token

#     print(f'BIG TESTER: {current_user_token.token}')

#     set = Set(name, rarity, size, user_token = user_token )

#     db.session.add(set)
#     db.session.commit()

#     response = set_schema.dump(set)
#     return jsonify(response)

# @api.route('/sets', methods = ['GET'])
# @token_required
# def get_set(current_user_token):
#     a_user = current_user_token.token
#     sets = Set.query.filter_by(user_token = a_user).all()
#     response = sets_schema.dump(sets)
#     return jsonify(response)

# @api.route('/sets/<id>', methods = ['GET'])
# @token_required
# def get_set_two(current_user_token, id):
#     fan = current_user_token.token
#     if fan == current_user_token.token:
#         set = Set.query.get(id)
#         response = set_schema.dump(set)
#         return jsonify(response)
#     else:
#         return jsonify({"message": "Valid Token Required"}),401

# # UPDATE endpoint
# @api.route('/sets/<id>', methods = ['POST','PUT'])
# @token_required
# def update_set(current_user_token, id):
#     set = Set.query.get(id) 
#     set.name = request.json['name']
#     set.rarity= request.json['rarity']
#     set.size = request.json['size']
#     user_token = current_user_token.token

#     db.session.commit()
#     response = set_schema.dump(set)
#     return jsonify(response)