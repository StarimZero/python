from flask import Blueprint, render_template, request
from dao import bbsDAO
import json

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('/')
def list():
    return render_template('index.html', title="게시판", pageName='bbs/list.html')

@bp.route('/list.json')
def listJSON():
    return bbsDAO.list();

@bp.route('/insert')
def insert():
    return render_template('index.html', title="글쓰기페이지", pageName='bbs/insert.html')

@bp.route('/insert', methods=['POST'])
def insertPost():
    req = json.loads(request.get_data())
    #print(req)
    result = bbsDAO.insert(req)
    return result

@bp.route('/<int:bbs_id>')
def read(bbs_id):
    vo=bbsDAO.read(bbs_id)
    return render_template('index.html', bbs=vo, title='게시글정보', pageName='bbs/read.html')

@bp.route('/<int:bid>', methods=['DELETE'])
def delete(bid):
    result = bbsDAO.delete(bid)
    return result
        