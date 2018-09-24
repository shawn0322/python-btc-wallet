from flask import Flask
from transaction import TX

app = Flask(__name__)


@app.route('/bulidAndSignTx',methods=['POST','GET'])
def hello_world():

    TX.build_from_io(("prev_tx_id_1","prev_tx_id_2"),(0,0,21321))
    TX.sign()

    return "helloword"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
