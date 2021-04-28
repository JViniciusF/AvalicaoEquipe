from flask import Blueprint, request, jsonify
from src.controller.Authenticate import jwt_required
from src.controller.ValidateFieldsRequest import ValidateFieldsRequest
from src.model.answer_user import Answer_User
from datetime import datetime
from src import db

import jwt, json

validate = ValidateFieldsRequest()

bp = Blueprint('answers', __name__, url_prefix='/answers')

@bp.route('/registerAnswer', methods=['POST'])
@jwt_required
def registerAnswer(current_user):
    try:
        dataNow = datetime.now().strftime('%d/%m/%Y')
        data = request.json['data']

        for resposta in data:
            answer = Answer_User(fk_id_user=current_user.id, 
                                fk_id_question=resposta['id_question'], 
                                answer=resposta['answer'], 
                                created_at=dataNow
                            )
            db.session.add(answer)
            db.session.commit()


        return jsonify({ "status": "suas respostas foram salvas com sucesso" })
    
    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500