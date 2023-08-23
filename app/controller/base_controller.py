from flask import jsonify
class BaseController():
    def success(message:str,data):
        return jsonify(
            {
                'respon_status' : {
                    "status" : "SUCCESS",
                    "code" : 200,
                    "message" : message
                },
                "data" : data
            }
            ) , 200

    def error(error_status:str,message:str,code:int):
        return jsonify({
                'respon_status' : {
                    "status" : error_status,
                    "code" : code,
                    "message" : message
                }
            }) , code