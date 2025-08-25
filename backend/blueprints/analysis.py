from flask import Blueprint, request, jsonify
import random
from datetime import datetime, timedelta
import string

analysis_bp = Blueprint('analysis', __name__)

# Mock data structure
dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
visits = [random.randint(100, 1000) for _ in range(7)]
messages = [random.randint(10, 100) for _ in range(7)]
purchases = [random.randint(5, 50) for _ in range(7)]
shoppings = [random.randint(20, 200) for _ in range(7)]

SUCCESS_CODE = 200

@analysis_bp.route('/userAccessSource', methods=['GET'])
def get_uas_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': [
          { 'value': 10, 'name': 'analysis.directAccess' },
          { 'value': 30, 'name': 'analysis.mailMarketing' },
          { 'value': 24, 'name': 'analysis.allianceAdvertising' },
          { 'value': 15, 'name': 'analysis.videoAdvertising' },
          { 'value': 18, 'name': 'analysis.searchEngines' }
        ]
    })

@analysis_bp.route('/weeklyUserActivity', methods=['GET'])
def get_wua_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': [
          { 'value': 132, 'name': 'analysis.monday' },
          { 'value': 342, 'name': 'analysis.tuesday' },
          { 'value': 26, 'name': 'analysis.wednesday' },
          { 'value': 12, 'name': 'analysis.thursday' },
          { 'value': 24, 'name': 'analysis.friday' },
          { 'value': 132, 'name': 'analysis.saturday' },
          { 'value': 14, 'name': 'analysis.sunday' }
        ]
    })

@analysis_bp.route('/monthlySales', methods=['GET'])
def get_ms_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': [
          { 'estimate': 100, 'actual': 120, 'name': 'analysis.january' },
          { 'estimate': 120, 'actual': 82, 'name': 'analysis.february' },
          { 'estimate': 161, 'actual': 91, 'name': 'analysis.march' },
          { 'estimate': 134, 'actual': 154, 'name': 'analysis.april' },
          { 'estimate': 105, 'actual': 162, 'name': 'analysis.may' },
          { 'estimate': 160, 'actual': 140, 'name': 'analysis.june' },
          { 'estimate': 165, 'actual': 145, 'name': 'analysis.july' },
          { 'estimate': 114, 'actual': 250, 'name': 'analysis.august' },
          { 'estimate': 163, 'actual': 134, 'name': 'analysis.september' },
          { 'estimate': 185, 'actual': 56, 'name': 'analysis.october' },
          { 'estimate': 118, 'actual': 99, 'name': 'analysis.november' },
          { 'estimate': 123, 'actual': 123, 'name': 'analysis.december' }
        ]
    })

@analysis_bp.route('/visit', methods=['GET'])
def get_visit_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'dates': dates,
            'visits': visits
        }
    })

@analysis_bp.route('/message', methods=['GET'])
def get_message_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'dates': dates,
            'messages': messages
        }
    })

@analysis_bp.route('/purchase', methods=['GET'])
def get_purchase_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'dates': dates,
            'purchases': purchases
        }
    })

@analysis_bp.route('/shopping', methods=['GET'])
def get_shopping_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'dates': dates,
            'shoppings': shoppings
        }
    })

@analysis_bp.route('/panel', methods=['GET'])
def get_panel_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'visits': sum(visits),
            'messages': sum(messages),
            'purchases': sum(purchases),
            'shoppings': sum(shoppings)
        }
    })

@analysis_bp.route('/total', methods=['GET'])
def get_total_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
          'users': 11,
          'messages': 22,
          'moneys': 33,
          'shoppings': 44
        }
    })
