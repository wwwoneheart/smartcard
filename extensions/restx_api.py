from flask import jsonify
from flask_restx import Api
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
from extensions.blockchain_error import ApiError
from flask import current_app


class MyApi(Api):

    """
    重新實作handle_error, 可以掌管所有api raise error
    """
    def handle_error(self, err):
        """It helps preventing writing unnecessary
        try/except block though out the application
        """
        # 只針對ApiError做特殊處理
        # 如果發生其他未預期錯誤
        #   Flask debug == true, 直接 raise
        #   Flask debug == false, 統一回覆 Server has encountered some error
        if isinstance(err, ApiError):
            print(err)  # log every exception raised in the application

            # Handle HTTPExceptions
            if isinstance(err, HTTPException):
                return jsonify({
                    'message': getattr(
                        err, 'description', HTTP_STATUS_CODES.get(err.code, '')
                    )
                }), err.code

            # Handle application specific custom exceptions
            return err.make_error_message()

        elif current_app.debug:
            raise err
        else:
            print(err)
            return jsonify({
                'message': 'Server has encountered some error'
            }), 500


api = MyApi(doc='/doc',
            version="1.0",
            title="SmartCard-APIs",
            description="Manage resources of the smartcard")
