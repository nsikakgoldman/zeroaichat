import functools

from flask import (
    Blueprint
)
from . import chatintelligence

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/register', methods=['get','POST'])
def chat():
    return str(chatintelligence.aiResponse())