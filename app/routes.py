from flask import Blueprint, request, jsonify

from .models import User, Post, Comment
from . import db

main = Blueprint('main', __name__)

@main.route("/users", methods=['POST'])
def create_user():
    try:
        data = request.get_json()

        # If data is a list
        if isinstance(data, list):
            new_users = []
            for item in data:
                username = item.get('username')
                email = item.get('email')
                if not username or not email:
                    continue
                new_user = User(username=username, email=email)
                db.session.add(new_user)
                new_users.append(username)
            db.session.commit()
            return jsonify({'message': f'{len(new_users)} users created', 'users': new_users}), 201

        # If data is only a one User
        else:
            username = data.get('username')
            email = data.get('email')
            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'User created', 'user': username}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@main.route("/users", methods=['GET'])
def get_users():
    username = request.args.get('username')
    if username:
        users = User.query.filter_by(username=username).all()
    else:
        users = User.query.all()

    return jsonify([{'id': u.id, 'username': u.username, 'email': u.email} for u in users])

@main.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@main.route("/users/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    user.username = request.json.get('username')
    user.email = request.json.get('email')

    try:
        db.session.commit()
        return jsonify({'message': 'User updated'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@main.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@main.route("/posts", methods=['POST'])
def create_post():
    try:
        data = request.get_json()

        # If data is a list
        if isinstance(data, list):
            new_posts = []
            for item in data:
                title = item.get('title')
                content = item.get('content')
                user_id = item.get('user_id')
                if not title or not content or not user_id:
                    continue
                new_post = Post(title=title, content=content, user_id=user_id)
                db.session.add(new_post)
                new_posts.append(title)
            db.session.commit()
            return jsonify({'message': f'{len(new_posts)} posts created', 'posts': new_posts}), 201

        # If data is only one Post
        else:
            title = data.get('title')
            content = data.get('content')
            user_id = data.get('user_id')
            db.session.add(Post(title=title, content=content, user_id=user_id))
            db.session.commit()
            return jsonify({'message': 'Post created'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@main.route("/posts", methods=['GET'])
def get_posts():
    title = request.args.get('title')
    try:
        if title:
            posts = Post.query.filter_by(title=title).all()
        else:
            posts = Post.query.all()
        return jsonify([{"Post ID: ":p.post_id,"Title": p.title, 'Content': p.content, 'User':p.author.username} for p in posts])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route("/users/<int:id>/posts", methods=['GET'])
def get_user_posts(id):
    user = User.query.get_or_404(id)
    try:
        if user.posts:
            return jsonify([{'Post ID':p.post_id,'Title': p.title, 'Content': p.content} for p in user.posts])
        else:
            return jsonify({'No Post':'This user has no posts.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route("/users/<int:id>/posts/<int:post_id>", methods=['PUT'])
def update_post(post_id):
    post = db.session.query(Post).filter_by(post_id=post_id).first()

    try:
        post.title = request.json.get('title')
        post.content = request.json.get('content')
        post.user_id = request.json.get('user_id')
        db.session.commit()
        return jsonify({'message': 'Post updated'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@main.route("/users/<int:id>/posts/<int:post_id>", methods=['DELETE'])
def delete_user_posts(post_id, id):
    post = Post.query.filter_by(post_id=post_id, user_id=id).first()

    try:
        db.session.delete(post)
        db.session.commit()
        return jsonify({'message': 'Post deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Post not found or does not belong to the user'}), 500

@main.route("/posts/<int:post_id>/comments", methods=['POST'])
def create_comment(post_id):

    data = request.get_json()

    try:
        if isinstance(data, list):
            comment_count = 0

            for item in data:
                user_id = item.get('user_id')
                content = item.get('content')
                parent_id = item.get('parent_id', None)

                if not user_id or not content or not parent_id:
                    continue
                new_comment = Comment(user_id=user_id, content=content, parent_id=parent_id, post_id=post_id)
                db.session.add(new_comment)
                comment_count += 1
            db.session.commit()
            return jsonify({'message': f'{comment_count} posts created'}), 201
        else:
            user_id = data.get('user_id')
            content = data.get('content')
            parent_id = data.get('parent_id', None)
            new_comment = Comment(user_id=user_id, content=content, parent_id=parent_id, post_id=post_id)
            db.session.add(new_comment)
            db.session.commit()
            return jsonify({'message': f'Comment created'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Get all comments in the database
@main.route("/comments", methods=['GET'])
def get_comments():
    try:
        comments = Comment.query.all()
        return jsonify([{'Content': c.content, 'User':c.user.username, 'Post':c.post.title} for c in comments])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get replies of a comment
@main.route("/comments/<int:comment_id>", methods=['GET'])
def get_replies(comment_id):
    try:
        comment = Comment.query.get_or_404(comment_id)
        replies = comment.replies

        return jsonify(
                {'Comment' : comment.content,
                 'Post' : comment.post.title,
                 'Replies' : [{
                    'id': r.id,
                    'content': r.content,
                    'replied user': r.user.username,
                    'user_id': r.user.id
                } for r in replies]
                }
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500